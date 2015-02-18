import pytest


@pytest.fixture
def poo_testdir(testdir):
    testdir.tmpdir.join('test_poo.py').write('''
import pytest

def test_success_without_poo():
    assert 1

def test_fail_with_poo():
    assert 0

''')

    return testdir


def test_verbose_mode_no_poo(poo_testdir):
    result = poo_testdir.runpytest('-v', '--strict')

    result.stdout.fnmatch_lines(['*test_fail_with_poo FAILED*'])
    result.stdout.fnmatch_lines(['*test_success_without_poo PASSED*'])

def test_verbose_mode_with_poo(poo_testdir):
    result = poo_testdir.runpytest('-v', '--poo', '--strict')

    result.stdout.fnmatch_lines(['*test_fail_with_poo FAILED (\\U0001f4a9 )*'])
    result.stdout.fnmatch_lines(['*test_success_without_poo PASSED*'])


def test_quiet_mode_no_poo(poo_testdir):
    result = poo_testdir.runpytest('-q', '--strict')
    outcome_line = result.stdout.lines[0]

    assert outcome_line.count('.') == 1
    assert outcome_line.count('F') == 1


def test_quiet_mode_with_poo(poo_testdir, request):
    result = poo_testdir.runpytest('-q', '--poo', '--strict')
    outcome_line = result.stdout.lines[0]

    assert outcome_line.count(u'.') == 1
    assert outcome_line.count(u'\\U0001f4a9') == 1
