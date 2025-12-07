# Write a program, which will read csv file, then update csv file and print its content in the terminal and finally save the file in chosen location.

# Running the program through terminal:
# python matrix_transform.py <input_file> <output_ file> <transformation_1> <transformation_2> .... <transformation_n>
#
#  <input_file> - name of the file that is going to be read, i.e. in.csv
#  <output_file> - name of the file, to which the new content will be saved, i.e. out.csv
# <transformation_x> - transformation in values "x,y,value" - x (column) and y (row) they are linear coordinates from 0, meanwhile "value" is the changed value, which should "come" in the given "place".
#


import sys
from file_handler_for_csv import FileHandler

arguments = sys.argv[1:]
print(arguments)

file_handler = FileHandler(input_file_path=arguments[0], output_file_path=arguments[1], transformations=arguments[2:])
file_handler.do_transformations()
file_handler.save_data()



