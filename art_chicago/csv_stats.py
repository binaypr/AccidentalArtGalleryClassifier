datset = []

with open("dataset.csv", "r", encoding="utf8") as f:
    for i, line in enumerate(f):
        splitline = line.split(",")
        type = splitline[0]
        if type not in datset:
            datset.append(type)
print(datset)
