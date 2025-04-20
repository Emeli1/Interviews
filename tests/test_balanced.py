import pytest

from balanced import balanced

def generate_expression():
    yield '(((([{}]))))', True
    yield '[([])((([[[]]])))]{()}', True
    yield '{{[()]}}', True
    yield '}{}', False
    yield '{{[(])]}}', False
    yield '[[{())}]', False

@pytest.mark.parametrize('expression, expected', generate_expression())
def test_balanced(expression, expected):
    assert balanced(expression) == expected
