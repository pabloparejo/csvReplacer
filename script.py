from __future__ import unicode_literals

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Name of file to transform", type=str)
args = parser.parse_args()

with open(args.file, 'rb') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        row.pop(2)
        print ','.join(row)