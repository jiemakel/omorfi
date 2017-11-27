#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts TSV formatted tests to yaml formatted tests
"""


# Author: Tommi A Pirinen <flammie@iki.fi> 2014

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import csv
from sys import argv, exit, stderr
from time import strftime

from omorfi.omor_formatter import OmorFormatter
from omorfi.apertium_formatter import ApertiumFormatter


# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Convert Finnish dictionary TSV data into xerox/HFST lexc format")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--input", "-i", action="append", required=True,
                    metavar="INFILE", help="read tests from INFILEs")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", "--one-file", "-1",
                    type=argparse.FileType("w"), required=True,
                    metavar="OFILE", help="write output to OFILE")
    ap.add_argument("--fields", "-F", action="store", default=2,
                    metavar="N", help="read N fields from master")
    ap.add_argument("--separator", action="store", default="\t",
                    metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
                    metavar="COMMENT", help="skip lines starting with COMMENT that"
                    "do not have SEPs")
    ap.add_argument("--strip", action="store",
                    metavar="STRIP", help="strip STRIP from fields before using")


    ap.add_argument("--format", "-f", action="store", default="omor",
                    help="use specific output format for lexc data",
                    choices=['omor', 'apertium'])
    args = ap.parse_args()
    quoting = csv.QUOTE_NONE
    quotechar = None
    # setup files
    formatter = None
    if args.format == 'omor':
        formatter = OmorFormatter()
    elif args.format == 'apertium':
        formatter = ApertiumFormatter()
    if args.verbose:
        print("Writing yaml to", args.output.name)
    # print test cases
    for tsv_filename in args.input:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        print("# Omorfi tests generated from", tsv_filename,
              "date:", strftime("%Y-%m-%d %H:%M:%S+%Z"),
              "params: ", ' '.join(argv), file=args.output,
              sep='\n# ')
        print("Tests:\n  All tests:", file=args.output)
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                                    quoting=quoting, quotechar=quotechar, escapechar='%', strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 3:
                    print(tsv_filename, linecount,
                          "Too few tabs on line",
                          "skipping following fields:", tsv_parts,
                          file=stderr)
                    continue
                # format output
                print('   "', tsv_parts[1], sep='', file=args.output,
                      end='')
                print(formatter.analyses2lexc(tsv_parts[2],
                                           args.format).replace('% ', ' '),
                      file=args.output, end='')
                print('": "', tsv_parts[0], '"', sep='', file=args.output)
    exit(0)


if __name__ == "__main__":
    main()
