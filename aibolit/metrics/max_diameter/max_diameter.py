# The MIT License (MIT)
#
# Copyright (c) 2020 Aibolit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from aibolit.ast_framework import AST, ASTNode, ASTNodeType

from typing import List, Tuple


class MaxDiameter:
    """
    Max diameter of class methods.
    """

    def value(self, ast: AST) -> int:
        method_diameters: List[int] = [
            self._calcalute_diameter(method_ast)
            for method_ast in ast.get_subtrees(ASTNodeType.METHOD_DECLARATION)
        ]

        return max(method_diameters, default=0)

    def _calcalute_diameter(self, ast: AST) -> int:
        distant_node_from_root, _ = self._find_distant_node(ast, ast.get_root(), False)

        # traverse undirected graph, because we need to ba able to traverse from child to parent in general
        # it is not needed at previous call, because the most distant node of a tree is anyway a child of root
        # and there is no need to traverse from child to parent, which simply safe time
        _, diameter = self._find_distant_node(ast, distant_node_from_root, True)
        return diameter

    def _find_distant_node(self, ast: AST, source_node: ASTNode, undirected: bool) -> Tuple[ASTNode, int]:
        distance = 0

        max_distance = 0
        distant_node = source_node

        def on_node_entering(node: ASTNode) -> None:
            nonlocal distance
            distance += 1

        def on_node_leaving(node: ASTNode) -> None:
            nonlocal distance, max_distance, distant_node
            if distance > max_distance:
                max_distance = distance
                distant_node = node

            distance -= 1

        ast.traverse(on_node_entering, on_node_leaving, source_node, undirected)

        return (distant_node, max_distance)
