from aibolit.ast_framework import ASTNodeType


def get_last_line(node: ASTNodeType):
    last_line = -1
    if not len(list(node.children)):
        return last_line

    for each_child in node.children:
        if each_child.line > last_line:
            last_line = each_child.line
    return last_line
