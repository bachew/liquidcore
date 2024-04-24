from liquidcore import logconf
from liquidcore.constants import ENV_INCLUDE_MANUAL_TESTS
from pathlib import Path
import os
import pytest


logconf.set_verbosity(1)


@pytest.fixture
def tmp_dir(tmpdir):
    yield Path(tmpdir)  # easier to work with Path objects


def manual_test(func):
    include = os.environ.get(ENV_INCLUDE_MANUAL_TESTS)

    if include:
        return func

    return pytest.mark.skip('manual test')(func)
