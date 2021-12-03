ages ={"Vasil Pupkin" : 19, "Marcus Aurelius" : 1860}
print(ages)

ages["Vasil Pupkin"] = 20
print(ages)

ages.pop("Vasil Pupkin", 20)
print(ages)


print("Vasil Pupkin :", "Vasil Pupkin" in ages)

print("Marcus Aurelius :", "Marcus Aurelius" in ages)