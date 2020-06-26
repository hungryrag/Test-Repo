import requests

def greetings(name):
    greet = 'Hello {}, nice to meet you!'.format(name)
    #greet = "Hello "+name+", nice to meet you!"
    return greet

r = requests.get("https://google.com")
print(r.status_code)

greet = greetings("Dhrubo")
print(greet)


