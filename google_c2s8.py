#!/usr/bin/env python3

import re

with open("FileLog.txt") as file:
    regex = re.findall(r"([a-zA-Z-]{10}),(.py)", file.read())
    print(regex[1], regex[2])
    
