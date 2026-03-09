# Generated from punto5.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .punto5Parser import punto5Parser
else:
    from punto5Parser import punto5Parser

# This class defines a complete generic visitor for a parse tree produced by punto5Parser.

class punto5Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by punto5Parser#stat.
    def visitStat(self, ctx:punto5Parser.StatContext):
        return self.visitChildren(ctx)



del punto5Parser