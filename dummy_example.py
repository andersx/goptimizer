#!/usr/bin/env python2

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
