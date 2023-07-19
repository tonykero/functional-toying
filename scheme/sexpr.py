from lark import Lark

class SexprParser:
    def __init__(self):
        self._internal_obj = Lark.open("sexpr.lark", rel_to=__file__)
        
    def parse(self, text):
        return self._internal_obj.parse(text)

