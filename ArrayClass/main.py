from Array import Array

arr = Array(["zero","one","two","three","four"])

print(arr.get(0))
arr.append("five")
arr.pop()
arr.extend(["five", "six", "seven"])
arr.insert(8, "eight")
arr.index("zero")
print(arr.length())
