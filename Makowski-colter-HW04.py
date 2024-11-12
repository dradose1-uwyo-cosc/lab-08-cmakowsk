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
with open("out.txt", "w") as out_file:
    lines = contents.splitlines()
    for line in lines:
        output_line = ""
        for amount in line.split():
            if amount.startswith("w:"):
                output_line += " " * int(amount[2:])
            elif amount.startswith("*:"):
                output_line += "*" * int(amount[2:])
        out_file.write(output_line + "\n")

