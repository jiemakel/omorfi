#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script generates edit distance.
"""


# Author: Omorfi contributors, 2014

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


# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Generate Xerox twolcs for Finnish")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--deletion", "-d", type=float, default=1.0,
                    metavar="DW", help="weight each deletion DW")
    ap.add_argument("--addition", "-a", type=float, default=1.0,
                    metavar="AW", help="weight each addition AW")
    ap.add_argument("--swap", "-s", type=float, default=1.0, metavar="SW",
                    help="weight each swap SW")
    ap.add_argument("--change", "-c", type=float, default=1.0, metavar="CW",
                    help="weight each change CW")
    ap.add_argument("--repeat", "-r", type=int, default=2, metavar="REP",
                    help="repeat REP")
    ap.add_argument("--output", "-o", type=argparse.FileType("w"),
                    required=True, metavar="OFILE", help="write output to OFILE")

    args = ap.parse_args()
    # check args
    # setup files
    if args.verbose:
        print("Writing everything to", args.output.name)
    # print definitions to rootfile
    if args.verbose:
        print("Creating EDs")
    out = "?*"
    for i in range(args.repeat):
        out += " ([?:0::1000 - 0]) ?*"
    print(out, file=args.output)
    exit(0)


if __name__ == "__main__":
    main()
