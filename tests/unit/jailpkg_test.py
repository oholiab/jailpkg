import pytest
from jailpkg import run as j

def test_generate_command_expected_output():
    assert j.generate_command('python27', '/some/jail') == 'pkg install python27 -c /some/jail '

def test_yaml_load_fine_on_hash_load():
    assert j.parse_yaml_packages("tests/unit/fixtures/test_yaml_load_fine_on_hash_load.yaml")\
            == {"somejail": ["some", "packages"],}
