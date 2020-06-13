import sys
import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


print(greet("World"))
print(greet("Dhrubo"))
r = requests.get("https://coreyms.com")
print(r.status_code)
