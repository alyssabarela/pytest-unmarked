from _pytest.mark import matchmark
import py


def pytest_addoption(parser):
    group = parser.getgroup('Unmarked', 'Unmarked')
    group._addoption('--unmarked',
                     action="store_true", dest="unmarked", default=False,
                     help="Run unmarked tests.")


