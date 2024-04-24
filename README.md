# liquidcore

Template repo for Python tool, a tool where developer is expected to just clone and use it immediately:

```console
$ git clone git@github.com:bachew/liquidcore.git
$ liquidcore/bin/lc do-something
```

For Python library template repo, use [solidcore](https://github.com/bachew/liquidcore) instead.


# Bootstrapping

When `bin/lc` is run for the first time, Python virtual environment will be created.

Dependencies are specified in `src/bootstrap.py::Venv.pip_installs`, changes to `Venv` instance (e.g. `Venv.pip_installs` causes virtual environment to be recreated on next `bin/lc`.

To run a command inside virtual environment:

```console
$ bin/lc run which python
```

Spawn a shell to enter virtual environment:

```console
$ bin/lc run which pytest
$ bin/lc run bash
$ which pytest  # same as first command
$ lc --help  # same as running 'bin/lc --help'
```


# Tests

To run unit tests:

```console
pytest tests/test_example.py
```

To include manual tests (decorated with `@manual_test`):

```console
$ MANUAL_TESTS=1 pytest tests/test_example.py --capture no
```
