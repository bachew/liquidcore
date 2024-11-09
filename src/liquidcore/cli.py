from . import logconf
from .app import Application
from click import argument, group, option, pass_context, pass_obj
import click
import subprocess


@group('liquidcore', context_settings={
    'show_default': True,
    'help_option_names': ['-h', '--help'],
})
@pass_context
@option('--json', is_flag=True, help='Output log events in json')
@option('-v', 'verbosity',
        default=0,
        count=True,
        help='Logging verbosity, multiple allowed')
def cli(ctx, json, verbosity):
    ctx.obj = Application()
    logconf.init(json=json)
    logconf.set_verbosity(verbosity)


@cli.command('test-logging')
def cli_test_logging():
    '''
    Test logging with liquidcore -v and --json options.
    '''
    logger_names = [
        'liquidcore.sh',
        'botocore',
        # Add logger names you wish to output to console, see also liquidcore.logconf:set_verbosity()
    ]

    for name in logger_names:
        logconf.log_all_levels(name)


@cli.command('run', context_settings={
    'help_option_names': [],
    'ignore_unknown_options': True,
})
@argument('command', nargs=-1, type=click.UNPROCESSED,
          metavar='PROGRAM [ARGS]...')
def cli_run(command):
    '''
    Run a command within Python virtual environment.
    '''
    if not command:
        raise click.UsageError('program is required')

    res = subprocess.run(command, check=False)
    raise SystemExit(res.returncode)


@cli.command('lint')
@pass_obj
def cli_lint(app):
    '''
    Scan Python code for syntax and typing errors.
    '''
    try:
        app.lint()
    except subprocess.CalledProcessError:
        raise SystemExit(1)


@cli.command('do-something')
@pass_obj
def cli_do_something(app):
    app.do_something()
