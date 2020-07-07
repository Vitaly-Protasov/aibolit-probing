from aibolit.utils.ast import ASTNodeType
from aibolit.utils.java_package import JavaPackage
from typing import List


class CountIfReturn:
    '''
    Returns lines with if statement which has also return statement
    and other conditions with else.
    '''
    def __init__(self):
        pass

    def value(self, filename: str) -> List[int]:
        detected_lines = []
        ast = JavaPackage(filename).java_classes
        for class_name in ast:
            java_class = ast[class_name]
            for index, if_node in enumerate(java_class.nodes_by_type(ASTNodeType.IF_STATEMENT)):
                all_childs = [i for i in java_class.tree.succ[if_node]]
                if len(all_childs) == 3:
                    for i in java_class.tree.succ[all_childs[1]]:
                        if java_class.get_type(i) == ASTNodeType.RETURN_STATEMENT:
                            detected_lines += [java_class.get_attr(if_node, 'source_code_line')]
        return detected_lines
