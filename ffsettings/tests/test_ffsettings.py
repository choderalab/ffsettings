"""
Unit and regression test for the ffsettings package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import ffsettings


def test_ffsettings_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("importing ", ffsettings.__name__)
    assert "ffsettings" in sys.modules


# Assert that a certain exception is raised
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
