import matplotlib.pyplot as plt
import math
obj = {}


with open("dataset.csv", "r", encoding="utf8") as f:
    for i, line in enumerate(f):
        splitline = line.split(",")
        type = splitline[0]
        # year = int(splitline[1])
        obj[type] = obj.get(type, 0) + 1

lists = sorted(obj.items())
print(lists)

x,y = zip(*lists)
low = min(y)
high = max(y)
plt.bar(x,y)
plt.xticks(rotation=90)
plt.show()

