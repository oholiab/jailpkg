import pytest
from jailpkg import run as j

basic_yaml = "tests/unit/fixtures/test_yaml_load_fine_on_hash_load.yaml"

def test_generate_command_expected_output():
    assert j.generate_command('python27', '/some/jail') == 'pkg install python27 -c /some/jail '

def test_yaml_load_fine_on_hash_load():
    assert j.parse_yaml_packages(basic_yaml)\
            == {"somejail": ["some", "packages"],}

def test_yaml_to_commands_expected_commands():
    assert j.yaml_to_commands(basic_yaml)\
            == ("pkg install some -c somejail", "pkg install packages -c somejail")
