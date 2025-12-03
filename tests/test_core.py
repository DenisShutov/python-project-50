from gendiff import generate_diff


def test_generate():
    result = generate_diff('file1.json', 'file2.json')
    assert len(result) > 0
    assert isinstance(result, str)
    assert result[0] == '{'
    assert result[-1] == '}'


def test_generate_yaml():
    result = generate_diff('file1.yaml', 'file2.yaml')
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