from importlib.util import find_spec


def test_import():

    if find_spec("cmake_detection") is None:
        msg = "Unable to import cmake_detection"
        raise AssertionError(msg)
