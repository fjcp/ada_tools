import re
import string
import sys
import glob
import os
import shutil
import re

def split_into_words(line):
    return re.findall(r"\w+", line)

def is_keyword(word):
    keyword_list = [
        'if', 
        'with',
        'use',
        'begin',
        'end',
        'procedure',
        'is',
        'Text_IO',
        'Put_Line',
        ]
    return word in keyword_list

def split_in_code_and_comment(line):
    if "--" not in line:
        return line,""
    else:    
        splits = line.split("--")
        return splits[0], splits[1]

def uppercase_variables(file_lines ):
    file_lines_out = []

    for line in file_lines:
        code, comments = split_in_code_and_comment(line)
        words = split_into_words(code)
        print(words)
        for word in words:
            if not is_keyword(word):
                upper_word = word.upper()    
                code = code.replace(word, upper_word, 1)
        line_out = code
        if len(comments) > 0:
            line_out += "--" + comments

        file_lines_out.append(line_out)

    return file_lines_out

if __name__ == "__main__":
    rootDir = "."

    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Found directory: %s" % dirName)
        for file in fileList:
            if file.endswith(".ada"):
                full_file_name = os.path.join(dirName, file)
                print("\t%s" % full_file_name)
                try:
                    input_file = open(full_file_name)
                    input_lines = input_file.readlines()
                    input_file.close()
                    output_file = open(full_file_name, "w")

                    output_lines = uppercase_variables( input_lines )
                    output_file.writelines(output_lines)
                    output_file.close()

                except:
                    print("Error processing: " + full_file_name)