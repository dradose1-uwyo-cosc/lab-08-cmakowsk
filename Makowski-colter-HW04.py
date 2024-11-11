# Colter Makowski
# UWYO COSC 1010
# Submission Date 11/12/24
# HW 04
# Lab Section:15
# Sources, people worked with, help given to:
# your
# comments
# here

# use this to split from colon split_str = Calc_str.split(operator)
from pathlib import Path
path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()
with open("out.txt", "w") as out_file:
    for line in lines:
        code_string = line.strip()
        list_of_amounts = code_string.split(" ")
        space_amount = 0
        star_amount = 0
        for amount in list_of_amounts:
            if amount.startswith("w:"):
                space_amount = int(amount[2:])
            if amount.startswith("*:"):
                star_amount = int(amount[2:])
        output_line = (space_amount * " ") + (star_amount * "*") + "\n"
        out_file.write(output_line)

