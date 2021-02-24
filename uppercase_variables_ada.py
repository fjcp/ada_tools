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
        ]
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
                    line = line.replace(word, upper_word, 1)

        file_lines_out.append(line)

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