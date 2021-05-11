#!/usr/bin/env python3

import os
import sys

# TO return error code as 1 if error and 0 for non-eror.
filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file is created!\n")
        # By default the error code returned is 0 when successful.
else:
    print("Error, the {} already exists".format(filename))
    sys.exit(1) # returning value 1 for error
