#!/usr/bin/env python
#
# Ali BARIN
#
# Example:  
##  
##  Sample file list: \example\a.txt, \example\b.txt, \example\c.txt,
##                      \example\d.txt, \example\e.jpg
##
##  root path: \example
##  file prefix: example-prefix-
##
##  after proccessing:  \example\example-prefix-1.txt, \example\example-prefix-2.txt,
##                      \example\example-prefix-3.txt, \example\example-prefix-4.txt,
##                      \example\example-prefix-5.jpg
##

import os

root_path = input("Root path: ")
file_prefix = input("File prefix: ")

paths = []
for (root, paths, files) in os.walk(root_path):
		for index, file in enumerate(files):
				index += 1
				full_path_file = root + "/" + file
				file = file.split(".")
				if not len(file) == 1:
					file = { "name": file[0], "ext": file[1] }
					full_path_new_file = root + "/" + file_prefix + str(index) + "." + file["ext"]
					os.rename(full_path_file, full_path_new_file)

print("All file names changed with its new names.")
