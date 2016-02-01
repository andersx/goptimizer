#!/usr/bin/env python2


import fortranformat as ff
import sys


if __name__ == "__main__":


    print sys.argv

    ifile = sys.argv[2]
    ofile = sys.argv[3]


    head = [-200.0, 0.0, 1.0, 0.0]
    force = [0.0, 0.0, 0.0]



    headformat = ff.FortranRecordWriter("4D20.12")
    forceformat = ff.FortranRecordWriter("3D20.12")

    f = open(ofile, "w")


    headstring = headformat.write(head)
    f.write(headstring + "\n")


    lol = forceformat.write(force)

    f.write(lol + "\n")
    f.write(lol + "\n")
    f.write(lol + "\n")

    f.close()
