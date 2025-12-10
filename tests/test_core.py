import pytest
from gendiff import generate_diff


def test_generate():
    result = generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json')
    assert len(result) > 0
    assert isinstance(result, str)
    assert result[0] == '{'
    assert result[-1] == '}'


def test_generate_yaml():
    result = generate_diff('tests/test_data/file1.yaml', 'tests/test_data/file2.yaml')
    assert len(result) > 0
    assert isinstance(result, str)
    assert result[0] == '{'
    assert result[-1] == '}'
    assert result == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def read_file(path):
    with open(path, 'r') as f:
      return f.read()
    
@pytest.mark.parametrize('file3, file4, expected_file', [
    ('tests/test_data/file3.json', 'tests/test_data/file4.json', 'tests/test_data/expected_result_stylish.txt'),
    ('tests/test_data/file3.yaml', 'tests/test_data/file4.yaml', 'tests/test_data/expected_result_stylish.txt'),
])
def test_stylish(file3, file4, expected_file):
    result = generate_diff(file3, file4, 'stylish')
    expected = read_file(expected_file)
    assert result.strip() == expected.strip()


@pytest.mark.parametrize('file3, file4, expected_file', [
    ('tests/test_data/file3.json', 'tests/test_data/file4.json', 'tests/test_data/expected_result_plain.txt'),
    ('tests/test_data/file3.yaml', 'tests/test_data/file4.yaml', 'tests/test_data/expected_result_plain.txt'),
])
def test_plain(file3, file4, expected_file):
    result = generate_diff(file3, file4, 'plain')
    expected = read_file(expected_file)
    assert result.strip() == expected.strip()


@pytest.mark.parametrize('file3, file4, expected_file', [
    ('tests/test_data/file3.json', 'tests/test_data/file4.json', 'tests/test_data/expected_result_json.txt'),
    ('tests/test_data/file3.yaml', 'tests/test_data/file4.yaml', 'tests/test_data/expected_result_json.txt'),
])
def test_json(file3, file4, expected_file):
    result = generate_diff(file3, file4, 'json')
    expected = read_file(expected_file)
    assert result.strip() == expected.strip()