#!/usr/bin/env python2
#
# MIT License
#
# Copyright (c) 2018 Anders Steen Christensen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import numpy as np
from goptimizer import parse_ifile, write_ofile

if __name__ == "__main__":

    # The input and output filenames from gaussian (don't change).
    ifile = sys.argv[2]
    ofile = sys.argv[3]

    # What you get out from Gaussian.
    # Cartesian coordinates in angstrom, use 0.52917721092 to get Bohr.
    (natoms, deriv, charge, spin, atomtypes, coordinates) = parse_ifile(ifile)

    # Make som artificial gradient and energies -- change to ML energy/grads, etc.

    # Energy in Hartree - conversion unit doesn't matter, 
    # as long as it is consistent with the gradient energy unit.
    energy = 666.00 

    # Gradient in Hartree/Bohr, use 0.52917721092 for converting Angstrom to Bohr.
    gradient_dummy = np.array([[1.0, 2.0, 3.0],
                               [4.0, 5.0, 6.0],
                               [7.0, 8.0, 9.0]])

    # Produce the Gaussian input file with the supplied data
    write_ofile(ofile, energy, natoms, gradient=gradient_dummy)
