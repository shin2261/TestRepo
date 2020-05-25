import math
import os
import sys

import requests

name = input("Your Name? ")
print("Hellp,", name)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("http://coreyms.com")
print(r.status_code)
