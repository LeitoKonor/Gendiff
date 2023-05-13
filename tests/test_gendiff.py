from gendiff import generate_diff  # noqa
from gendiff.gendiff import extract_data, make_diff
from gendiff.output_views.json import json_output
from gendiff.output_views.plain import plain_output
from gendiff.output_views.stylish import stylish_output
from tests.fixtures.data import EXTRACT_RESULT, MAKE_DIFF_RESULT

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'

PATH_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_FILE2_JSON = 'tests/fixtures/file2.json'
PATH_FILE1_YML = 'tests/fixtures/file1.yml'
PATH_FILE2_YML = 'tests/fixtures/file2.yml'

PATH_RESULT_STYLISH = 'tests/fixtures/result_stylish'
PATH_RESULT_PLAIN = 'tests/fixtures/result_plain'


def test_extract_data():
    assert extract_data(PATH_FILE1_JSON) == EXTRACT_RESULT
    assert extract_data(PATH_FILE1_YML) == EXTRACT_RESULT


def test_generate_diff():

    with open(PATH_RESULT_STYLISH) as f:
        result_stylish = f.read()
    with open(PATH_RESULT_PLAIN) as f:
        result_plain = f.read()

    assert result_stylish == \
        generate_diff(PATH_FILE1_JSON, PATH_FILE2_JSON)
    assert result_stylish == \
        generate_diff(PATH_FILE1_YML, PATH_FILE2_YML)

    assert result_stylish == \
        generate_diff(PATH_FILE1_JSON, PATH_FILE2_JSON, STYLISH)
    assert result_stylish == \
        generate_diff(PATH_FILE1_YML, PATH_FILE2_YML, STYLISH)

    assert result_plain == \
        generate_diff(PATH_FILE1_JSON, PATH_FILE2_JSON, PLAIN)
    assert result_plain == \
        generate_diff(PATH_FILE1_YML, PATH_FILE2_YML, PLAIN)


def test_output_format():
    assert type(json_output(EXTRACT_RESULT)) == str
    assert type(plain_output(EXTRACT_RESULT)) == str
    assert type(stylish_output(extract_data)) == str


def test_make_diff():
    file1 = extract_data(PATH_FILE1_JSON)
    file2 = extract_data(PATH_FILE2_JSON)

    result = make_diff(file1, file2)
    assert result == MAKE_DIFF_RESULT
