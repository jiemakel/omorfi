#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""This script creates a reweighting rulesets that match the current tag format.
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
from sys import exit

from omorfi.ftb3_formatter import Ftb3Formatter
from omorfi.no_tags_formatter import NoTagsFormatter
from omorfi.omor_formatter import OmorFormatter
from omorfi.apertium_formatter import ApertiumFormatter
from omorfi.settings import stuff_weights


# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Create FST reweighter for tags")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o",
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
                    choices=["omor", "ftb3", "giella", "apertium", "boundary"])
    args = ap.parse_args()
    if args.format == "omor":
        formatter = OmorFormatter(True)
    elif args.format == "ftb3":
        formatter = Ftb3Formatter(True)
    elif args.format == 'boundary':
        formatter = NoTagsFormatter(True)
    elif args.format == 'apertium':
        formatter = ApertiumFormatter(True)
    else:
        print("Not implemnetd formatters", args.format)
        exit(1)
    # setup files
    if args.verbose:
        print("Writing some weights to", args.output.name)
    for stuff, weight in stuff_weights.items():
        if formatter.stuff2lexc(stuff) and formatter.stuff2lexc(stuff) != '0':
            print(formatter.stuff2lexc(stuff), weight,
                  sep='\t', file=args.output)
    exit(0)


if __name__ == "__main__":
    main()
