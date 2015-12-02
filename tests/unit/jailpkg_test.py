import pytest
from jailpkg import jailpkg as j

def test_generate_command_expected_output():
    assert j.generate_command('python27', '/some/jail') == 'pkg install python27 -c /some/jail '
