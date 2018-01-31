# goptimizer
Tool to use the Gaussian 09 geometry optimizer with far superior programs, by calling external scripts to retrieve energy and gradients from an external source.

# How to use:
Use the keyword `external="/full/path/to/python_script.py"` e.g.

    # force external="/home/andersx/dev/goptimizer/dummy_example.py"

in your `.com` file.

The `dummy_example.py` in an example of how to supply energy and gradients.

You probably need to `pip install fortranformat` to use this. Good luck.


# License:
MIT Licensed.

