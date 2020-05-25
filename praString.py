message = """Hello's world"""
print(message)
print(len(message))
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count("Hello"))
print(message.count("l"))
print(message.find("world"))
print(message.find("Universe"))
new_message = message.replace("world", "Universe")
print(new_message)
greeting = "Hello"
name = "Micheal"
message = greeting + ", " + name + ". Welcome!"
print(message)
message = "{}, {}. Welcome!".format(greeting, name)
print(message)
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)
# print(dir(name))
print(help(str.lower))
