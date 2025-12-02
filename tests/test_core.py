from gendiff import generate_diff


def test_generate():
    result = generate_diff('file1.json', 'file2.json')
    assert len(result) > 0
    assert isinstance(result, str)
    assert result[0] == '{'
    assert result[-1] == '}'
