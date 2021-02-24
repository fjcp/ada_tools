import re
import string
import sys
import glob
import os
import shutil

from uppercase_variables_ada import uppercase_variables

def string_to_string_list(string):
    str_list_out = []
    str_list_aux = string.split("\n")
    for string in str_list_aux:
        string += "\n"
        str_list_out.append(string)
    return str_list_out

def string_list_to_string(string_list):
    return "".join(string_list)

def process_code(ada_code_in):
    file_lines_in = string_to_string_list(ada_code_in)
    file_lines_out= uppercase_variables(file_lines_in)
    return string_list_to_string(file_lines_out)

def test_method_comment_first_column_simple_sentence():
    ada_code_in = """\
-- comments
if (my_variable)"""

    ada_code_out = """\
-- comments
if (MY_VARIABLE)
"""
    assert process_code(ada_code_in) == ada_code_out

def test_method_commend_middle_line_and_literal_string():
    ada_code_in = """
-- Ada Hello, World! program.
with Text_IO; use Text_IO;      -- This gets the IO facility.
procedure Hello is              -- Main, but no special name is needed.
begin
   Put_Line("HELLO, WORLD!");   -- Put_Line is from Text_IO.
end Hello;"""

    ada_code_out = """
-- Ada Hello, World! program.
with Text_IO; use Text_IO;      -- This gets the IO facility.
procedure HELLO is              -- Main, but no special name is needed.
begin
   Put_Line("HELLO, WORLD!");   -- Put_Line is from Text_IO.
end HELLO;
"""
    assert process_code(ada_code_in) == ada_code_out