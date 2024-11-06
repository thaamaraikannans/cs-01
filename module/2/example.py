myVal = "      netflix is an American Subscription Video On-Demand Over-the-top streaming service. The service primarily distributes original and acquired films and television shows from various genres, and it is available internationally in multiple languages. "

# length = len(myVal)
# print(length-1)
# data = myVal.capitalize()

# data = myVal.casefold()
# data = myVal.count(" and")
data = myVal.encode(encoding="utf-8")
data = data.decode("utf-8")
data = data.strip()
print(data.endswith("."))
print(data.find("."))
# try:
#     data = myVal.center(100,0)
# except Exception as sudharshan:
#     print(sudharshan)

print(myVal)
# print(len(myVal))
print("\n")
print(data,"\n")
# print(len(data),"\n")
print(type(data))
