#!/usr/bin/env python3

import os

# Using environ() method to get the path of environment variable
print("SHELL:" + os.environ.get("SHELL",""))
print("LOGNAME:" + os.environ.get("LOGNAME", ""))
print("PWD:" + os.environ.get("PWD", ""))
print("HOME:" + os.environ.get("HOME", ""))

# We will export a new environment variable called Fruit=Apple in the CLI
print("FRUIT:" + os.environ.get("FRUIT", ""))
