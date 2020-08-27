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

from aibolit.patterns.joined_validation.joined_validation import JoinedValidation
from aibolit.ast_framework import AST
from aibolit.utils.ast_builder import build_ast


class JoinedValidationTestCase(TestCase):
    current_directory = Path(__file__).absolute().parent

    def test_canFindSimpleJoinedValidation(self):
        filepath = self.current_directory / "SimpleJoinedValidation.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([3], lines, "Could not find simple joined validation")

    def test_canFindJoinedValidationAndOr(self):
        filepath = self.current_directory / "JoinedValidationAndOr.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([3], lines, "Could not find joined validation in AndOr condition")

    def test_canFindJoinedValidationOrAnd(self):
        filepath = self.current_directory / "JoinedValidationOrAnd.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([3], lines, "Could not find joined validation in OrAnd condition")

    def test_canFindJoinedValidationOrOr(self):
        filepath = self.current_directory / "JoinedValidationOrOr.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([3], lines, "Could not find joined validation in OrOr condition")

    def test_canFindJoinedValidationOrFunctionCall(self):
        filepath = self.current_directory / "JoinedValidationOrFunctionCall.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([8], lines, "Could not find joined validation in function call")

    def test_canFindJoinedValidationOrFieldAccess(self):
        filepath = self.current_directory / "JoinedValidationOrFieldAccess.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([6], lines, "Could not find joined validation in field access")

    def test_canFindNoBracketsJoinedValidation(self):
        filepath = self.current_directory / "NoBracketsJoinedValidation.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([3], lines, "Could not find joined validation when using no brackets")

    def test_canSkipEmptyJoinedValidation(self):
        filepath = self.current_directory / "EmptyJoinedValidation.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([], lines, "Could not skip empty joined validation")

    def test_canSkipNoJoinedValidation(self):
        filepath = self.current_directory / "NoJoinedValidation.java"
        ast = AST.build_from_javalang(build_ast(filepath))
        pattern = JoinedValidation()
        lines = pattern.value(ast)
        self.assertEqual([], lines, "Could not skip when there is no joined validation")
