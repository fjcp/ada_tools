import re
import string
import sys
import glob
import os
import shutil

def string_to_string_list(string):
    str_list_out = []
    str_list_aux = string.split("\n")
    for string in str_list_aux:
        string += "\n"
        str_list_out.append(string)
    return str_list_out


def string_list_to_string(string_list):
    return "".join(string_list)


def add_cpp_include(str_list, include_name):
    str_list.insert(0, '#include "' + include_name + '"\n')
    return str_list

def split_into_words(line):
    import re
    word_regex_improved = r"(\w[\w']*\w|\w)"
    word_matcher = re.compile(word_regex_improved)
    return word_matcher.findall(line)

def is_keyword(word):
    keyword_list = ['if', 'call']
    return word in keyword_list


def uppercase_variables(file_lines ):
    file_lines_out = []

    for line in file_lines:
        if not line.startswith("--"):
            words = split_into_words(line)
            print(words)
            for word in words:
                if not is_keyword(word):
                    upper_word = word.upper()    
                    line = line.replace(word, upper_word)

        file_lines_out.append(line)

    return file_lines_out

if __name__ == "__main__":
    rootDir = "."

    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Found directory: %s" % dirName)
        for file in fileList:
            #        for file in ['SortWireDataOp.cpp']:
            if file.endswith(".ada"):
                full_file_name = os.path.join(dirName, file)
                # full_file_name = file
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