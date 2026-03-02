""" x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
print("\n----------------\n")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
print("\n----------------\n")

x = set(["apple", "banana", "cherry"])
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
 """

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print("dict :", thisdict)

print("len :", len(thisdict))


x = thisdict["model"]
print("avoir la cle model :", x)

x = thisdict.keys()
print("avoir les cles, utiliser .keys :", x)

x = thisdict.values()
print("Vallues :", x)

x = thisdict.items()
print("demo de .item :", x)

thisdict.update({"year": 2020})

x = thisdict.get("model")
print(x)