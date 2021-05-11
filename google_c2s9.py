
#!/usr/bin/env python3

import re

email = input("Enter email for pattern matching and hide it:")
print(re.sub(r"[\w%+-]+@[\w.-]+", "[######]", email)
