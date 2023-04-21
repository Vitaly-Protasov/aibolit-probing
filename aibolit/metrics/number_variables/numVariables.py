from aibolit.utils.ast_builder import build_ast
from aibolit.ast_framework import AST, ASTNodeType
from aibolit.metrics.utils import get_last_line

from typing import Dict
from collections import OrderedDict
from javalang.tree import VariableDeclarator, MemberReference


class NumVars:
    '''
    This class count number variables in class
    input: filename
    output: number of variables
    '''

    def value(self, filename: str) -> int:
        tree = build_ast(filename)
        count_variables = set()
        for _, var_body in tree.filter(VariableDeclarator):
            count_variables.add(var_body.name)

        for _, var_body1 in tree.filter(MemberReference):
            count_variables.add(var_body1.member)

        return len(count_variables)
    
    def count_variables(self, method_ast: AST) -> int:
        assert method_ast.get_root().node_type == ASTNodeType.METHOD_DECLARATION

        variables = set()
        for node_ast in method_ast.get_subtrees(ASTNodeType.VARIABLE_DECLARATOR):
            title = node_ast.get_root().name
            variables.add(title)

        for node_ast in method_ast.get_subtrees(ASTNodeType.ASSIGNMENT):
            assigment_children = node_ast.get_root().children
            for child in assigment_children:
                if child.node_type == ASTNodeType.MEMBER_REFERENCE:
                    title = child.member
                    variables.add(title)

        return len(variables)  

    def probing_values(self, ast: AST) -> Dict[str, int]:
        """
        Number of variables inside each method
        """
        values_dict = OrderedDict()
        for method_ast in ast.get_subtrees(ASTNodeType.METHOD_DECLARATION):
            method_name = method_ast.get_root().name
            start_line = method_ast.get_root().line
            end_line = get_last_line(method_ast.get_root())
            end_line = end_line + 1 if end_line == start_line else end_line

            method_value = self.count_variables(method_ast)
            values_dict[f"{method_name}:{start_line}:{end_line}"] = method_value
        return values_dict
