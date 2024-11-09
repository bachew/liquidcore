from liquidcore import logconf
from pathlib import Path
import os
import pytest


logconf.set_verbosity(1)


@pytest.fixture
def tmp_dir(tmpdir):
    yield Path(tmpdir)  # easier to work with Path objects


def manual_test(func):
    if os.environ.get('include_manual') == '1':
        return func

    return pytest.mark.skip('manual test')(func)
