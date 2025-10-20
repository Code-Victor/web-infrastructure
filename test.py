Hello = {"hi": 1, "hello": 2, "hey": 3}


for value in Hello.values():
    print(f" Value: {value}")
for key in Hello.keys():
    print(f" key: {key}")
for key, value in Hello.items():
    print(f"Key: {key}, Value: {value}")
print(Hello.items())
