#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:17:28 2022

@author: dhuffman
"""

import os

def gather_files_and_names(path_to_data, filename):
    starting_dir = os.getcwd()
    os.chdir(path_to_data)
    f = open(filename, 'r')
    for each_line in f:
        if (".pdf:" in each_line):
            curr_pdf = each_line.split(":")[0]
        elif (":name:" in each_line):
            curr_name = each_line.split("\n")[0].split("name: ")[1]
            curr_name = "_".join(curr_name.split(" ")) + ".pdf"
            print("Ranaming files as follows:")
            print(curr_pdf)
            print(curr_name)
            print()
            os.rename(curr_pdf, curr_name)
    f.close()
    os.chdir(starting_dir)

