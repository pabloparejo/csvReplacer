from __future__ import unicode_literals

import argparse
import csv
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Name of file to transform", type=str)
args = parser.parse_args()

with open(args.file, 'rb') as input_file:
    with open('output.csv', 'wb') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        pattern = re.compile(r"e(\w)e")

        for row in reader:
            row.pop(2)
            index = 0
            for col in row:
                row[index] = re.sub(pattern, r'a\1a', row[index])
                index += 1
                if index >= 2:
                    break

            writer.writerow(row)