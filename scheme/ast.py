from lark import Transformer, Token
from functools import reduce

class Symbol:
    def __init__(self,sym: str):
        self._symbol = sym
    
    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self._symbol == other._symbol
        raise NotImplementedError
    
    def __repr__(self):
        return f"Symbol({self._symbol})"

class Constant:
    def __init__(self, cst):
        self._constant = cst
    
    def __eq__(self, other):
        if isinstance(other, Constant):
            return self._constant == other._constant
        raise NotImplementedError
    
    def __repr__(self):
        return f"Constant({self._constant})"

class Sexpr:
    def __init__(self, l):
        self._list = l
    
    def __eq__(self, other):
        if isinstance(other, Sexpr):
            if len(self._list) == len(other._list):
                return all(map(lambda tup: tup[0] == tup[1],zip(self._list, other._list)))
            else:
                return False
        raise NotImplementedError

    def __repr__(self):
        _strs = map(repr,self._list)
        _str = reduce(lambda x1, x2: x1 + " " + x2,_strs,"")
        return f"Sexpr({_str} )"

class ASTTransform(Transformer):
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
    def boolean(self, l):
        return l[0]
    def start(self, l):
        return l[0]
    def atom(self, l):
        return l[0]
