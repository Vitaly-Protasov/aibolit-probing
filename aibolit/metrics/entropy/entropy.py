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

import javalang
from typing import Dict, List, Union
import numpy as np  # type: ignore
from scipy.stats import entropy  # type: ignore
from pathlib import Path
from collections import OrderedDict

from aibolit.utils.encoding_detector import read_text_with_autodetected_encoding
from aibolit.ast_framework import AST, ASTNodeType
from aibolit.utils.ast_builder import build_ast
from aibolit.metrics.utils import get_last_line


class Entropy:
    def __file_to_tokens(self, filename: str) -> List[str]:
        '''Takes path to java class file and returns tokens'''
        source_code = read_text_with_autodetected_encoding(filename)
        tokens = javalang.tokenizer.tokenize(source_code)
        return [token.value for token in tokens]

    def value(self, filename: str):
        tokens = self.__file_to_tokens(filename)
        _, counts = np.unique(tokens, return_counts=True)
        return entropy(counts)
    
    def probing_values(self, filepath: Union[Path, str]) -> Dict[str, int]:
        """
        Entropy of class's methods
        """
        methods_list: List[str] = []
        ast = AST.build_from_javalang(build_ast(filepath))
        for method_ast in ast.get_subtrees(ASTNodeType.METHOD_DECLARATION):
            method_name = method_ast.get_root().name
            start_line = method_ast.get_root().line
            end_line = get_last_line(method_ast.get_root())
            end_line = end_line + 1 if end_line == start_line else end_line
            methods_list.append(f"{method_name}:{start_line}:{end_line}")
        
        source_code = read_text_with_autodetected_encoding(filepath)
        tokens = javalang.tokenizer.tokenize(source_code)
        tokens_list = list(tokens)
        
        values_dict = OrderedDict()
        for method_name_line in methods_list:
            _, start_line, end_line = method_name_line.split(":")
            
            method_tokens_body = [l.value for l in tokens_list if int(start_line) <= l.position.line < int(end_line)]
            _, counts = np.unique(method_tokens_body, return_counts=True)
            value = entropy(counts)
            
            values_dict[method_name_line] = value
        return values_dict
