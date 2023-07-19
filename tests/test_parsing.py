from scheme.sexpr import SexprParser
from scheme.ast import ASTTransform, Symbol, Constant, Sexpr

import pytest

@pytest.fixture
def text_to_ast():
    return lambda text: ASTTransform().transform(SexprParser().parse(text))

def test_int(text_to_ast):
    text="2"

    ast = text_to_ast(text)
    assert ast == Constant(2)


def test_float(text_to_ast):
    text="2.75"

    ast = text_to_ast(text)
    assert ast == Constant(2.75)

def test_boolean(text_to_ast):
    text_f="#f"
    text_t="#t"

    ast = text_to_ast(text_f)
    assert ast == Constant(False)
    ast = text_to_ast(text_t)
    assert ast == Constant(True)

def test_define_int(text_to_ast):
    text="(define i 2)"

    ast = text_to_ast(text)
    print(ast)
    assert ast == Sexpr([Symbol("define"), Symbol("i"), Constant(2)])


def test_define_float(text_to_ast):
    text="(define f 2.75)"

    ast = text_to_ast(text)
    assert ast == Sexpr([Symbol("define"), Symbol("f"), Constant(2.75)])