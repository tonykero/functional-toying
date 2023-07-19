from lark import Lark, Transformer, Token

class SexprParser:
    def __init__(self):

        self.lark = Lark(r"""

    start: atom | sexpr

    sexpr: WS* "(" WS* (atom|sexpr) ((WS* (atom|sexpr))+)? WS* ")" WS*
    atom: symbol | constant
                    
    true: "#t"
    false: "#f"
    boolean: true | false
    integer: INT
    float: FLOAT
    constant: integer | float | boolean
    symbol: WORD
                    
%import common.WS
%import common.WORD
%import common.INT
%import common.FLOAT

""", start="start")
        
    def parse(self, text):
        return self.lark.parse(text)


class Symbol:
    def __init__(self,sym: str):
        self._symbol = sym
    
    def __repr__(self):
        return f"Symbol({self._symbol})"

class Constant:
    def __init__(self, cst):
        self._constant = cst
    
    def __repr__(self):
        return f"Constant({self._constant})"

from functools import reduce
class Sexpr:
    def __init__(self, l):
        self._list = l
    
    def __repr__(self):
        _strs = map(repr,self._list)
        _str = reduce(lambda x1, x2: x1 + " " + x2,_strs,"")
        return f"Sexpr({_str} )"

class SexprTransformer(Transformer):
    # Constants
    def float(self, l):
        fval = l[0]
        return float(fval)
    def integer(self, l):
        ival = l[0]
        return int(ival)
    def true(self, l):
        return True
    def false(self, l):
        return False
    
    # Final objects
    def symbol(self, l):
        str = l[0].value
        return Symbol(str)
    def sexpr(self, l):
        filter_ws = lambda x: x.type != 'WS' if isinstance(x, Token) else True
        return Sexpr(list(filter(filter_ws,l)))
    def constant(self, l):
        return Constant(l[0])
    
    # rule skip
    def start(self, l):
        return l[0]
    def atom(self, l):
        return l[0]
    
parser = SexprParser()
transformer = SexprTransformer()
text = " ( define lst (list 5.0 1 a) ) "
tree = parser.parse(text)
from pprint import pprint
pprint(tree)
print("\n\n")
transformed_tree = transformer.transform(tree)
print(transformed_tree)
