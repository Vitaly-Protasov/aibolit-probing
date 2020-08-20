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

from pathlib import Path
from unittest import TestCase

from aibolit.patterns.var_middle.var_middle import VarMiddle
from aibolit.ast_framework import AST
from aibolit.utils.ast_builder import build_ast


class VarMiddleTestCase(TestCase):
    current_directory = Path(__file__).absolute().parent

    def test_good_class(self):
        filepath = self.current_directory / "1.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_bad_class(self):
        filepath = self.current_directory / "2.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [9, 16])

    def test_case_with_multiline_method_declaration(self):
        filepath = self.current_directory / "3.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_case_with_empty_lines(self):
        filepath = self.current_directory / "4.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_case_autoclosable(self):
        filepath = self.current_directory / "5.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_case_nested_class(self):
        filepath = self.current_directory / "6.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [30, 33])

    def test_declaration_after_super_class_method_call(self):
        filepath = self.current_directory / "7.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [14])

    def test_for_scope_good(self):
        filepath = self.current_directory / "8.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_for_scope_bad(self):
        filepath = self.current_directory / "9.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [11])

    def test_variable_declared_after_for(self):
        filepath = self.current_directory / "10.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [11])

    def test_11(self):
        filepath = self.current_directory / "11.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_catch_good(self):
        filepath = self.current_directory / "12.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_catch_bad(self):
        filepath = self.current_directory / "13.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [38])

    def test_else_bad(self):
        filepath = self.current_directory / "14.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [88])

    def test_variable_after_curly_braces(self):
        filepath = self.current_directory / "15.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_variable_inside_lambda(self):
        filepath = self.current_directory / "16.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [])

    def test_annotation_with_parameters(self):
        filepath = self.current_directory / "17.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = VarMiddle()
        lines = pattern.value(ast)
        self.assertEqual(lines, [22])
