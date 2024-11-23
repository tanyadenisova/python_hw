import pytest
from stringUtils import StringUtils

@pytest.mark.parametrize(
     "input_text, expected_output",
     [
         ("привет", "Привет"),
         ("как дела?", "Как дела?"),
         ("роза", "Роза"),
    ],
 )
def test_capitilize_positive(input_text, expected_output):
     string = StringUtils()
     assert string.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("999", "999"), (" ", " ")])

def test_capitilize_negative(input_text, expected_output):
    string = StringUtils()
    assert string.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
     [
         ("  цветок", "цветок"),
         (" красиво", "красиво"),
         ("   сколько стоит", "сколько стоит"),
    ],)

def test_trim_pozitive(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("  ", ""), (".", ".")])

def test_trim_negative(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, delimeter, expected_output",
     [
         ("черный,красный", ",", ["черный", "красный"]),
         ("1,2,3", ",", ["1", "2", "3"]),
         ("а,б", ",", ["а", "б"]),
    ],)

def test_to_list_pozitive(input_text, delimeter, expected_output):
    string = StringUtils()
    assert string.to_list(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, delimeter, expected_output",
     [
         ("", ",", []),
         ("1,2,3", ",", ["1", "2", "3"])
    ],)

def test_to_list_negative(input_text, delimeter, expected_output):
    string = StringUtils()
    assert string.to_list(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("привет", "т", True),
         ("солнце", "ц", True),
         ("кот", "о", True),
    ],)

def test_contains_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [("белый", "щ", False), ("квадрат", "я", False)])

def test_contains_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("фонарь", "ь", "фонар"),
         ("ветка", "ве", "тка"),
         ("трек", "к", "тре"),
    ],)

def test_delete_symbol_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [("мед", "р", "мед"), ("яд", "рот", "яд")])

def test_delete_symbol_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("привет андрей", "п", True),
         ("яблоко", "я", True),
         ("пот", "п", True),
    ],)

def test_starts_with_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [(" dady", "d", False), (" ", "a", False)])

def test_starts_with_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
     [
         ("мама", "а", True),
         ("чай", "й", True),
         ("торт с вареной сгущенкой", "й", True),
    ],)

def test_end_with_pozitive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [("fail.", "l", False), (".", ",", False)])

def test_end_with_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
     [
         ("   ", True),
         (" ",True),
         ("",True),
    ],)

def test_is_empty_pozitive(input_text, expected_output):
    string = StringUtils()
    assert string.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("дог", False), ("хот", False)])

def test_is_empty_negative(input_text, expected_output):
    string = StringUtils()
    assert string.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
     [
         ([1,2,3,4], ", ", "1, 2, 3, 4"),
         (["a", "b", "c", "d"], ", ", "a, b, c, d"),
         (["love", "is"], "," , "love, is"),
    ],)

def test_list_to_string_pozitive(input_text, joiner, expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
    [(["1", "2"], ", ", "1,2"), (["a", "b"], "-", "a,b")]
)
def test_list_to_string_negative(input_text, joiner, expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text, joiner) != expected_output