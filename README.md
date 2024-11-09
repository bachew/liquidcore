# liquidcore

Template repo for Python tool, a tool where developer is expected to just clone and use it immediately:

```console
$ git clone git@github.com:bachew/liquidcore.git
$ liquidcore/bin/liquidcore do-something
```

For Python library template repo, use [solidcore](https://github.com/bachew/liquidcore) instead.


## Bootstrapping

When `bin/liquidcore` is run for the first time, Python virtual environment will be created.

Dependencies are specified in `src/bootstrap.py::Venv.pip_installs`, changes to `Venv` instance (e.g. `Venv.pip_installs`) causes virtual environment to be recreated on next `bin/liquidcore`.

To run a command inside virtual environment:

```console
$ bin/liquidcore run which python
```

To enter virtual environment, spawn a subshell:

```console
$ bin/liquidcore run which pytest
$ bin/liquidcore run bash  # subshell
$ which pytest  # same as first command
$ liquidcore --help  # same as running 'bin/liquidcore --help'
```


# Tests

To run unit tests:

```console
$ pytest tests/test_example.py
```

To include manual tests (those decorated with `@manual_test`):

```console
$ include_manual=1 pytest tests/test_example.py --capture no
```
