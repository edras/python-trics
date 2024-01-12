# normal dictionary

a = {"one": 1, "two": 2}
print(a, type(a))
# {'one': 1, 'two': 2} <class 'dict'>

a.update({"three": 3})
print(a)
# {'one': 1, 'two': 2, 'three': 3}

a["two"] = 2.1
print(a["two"])
# 2.1

# defaultdict
# return a default value for non-existing key
from collections import defaultdict
a = defaultdict(int)
# defaultdict(<class 'int'>, {})

print(a["one"])
# output 0
# defaultdict(<class 'int'>, {'one': 0})

a["one"] += 1
print(a["one"])
# output 1

# ordered dict
from collections import OrderedDict

a = OrderedDict({"one": 1, "two": 2, "three": 3, "four": 4})
print(a)
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
a.move_to_end("one", last=True)
# OrderedDict([('two', 2), ('three', 3), ('four', 4), ('one', 1)])
a.move_to_end("three", last=False)
# OrderedDict([('three', 3), ('two', 2), ('four', 4), ('one', 1)])

# chainmap
from collections import ChainMap

a = {"one":1, "two": 2}
b = {"three": 3, "four": 4}
c = {"five": 5, "six": 6, "three": 3.1}

merged = ChainMap(a, b, c)
print(merged)
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4}, {'five': 5, 'six': 6, 'three': 3.1})
print(merged["three"])
# 3

# counter
from collections import Counter
sentence = "we can't control our thoughts, but we can control our words"

a = Counter(sentence.split(" "))
print(a)
# Counter({'we': 2, 'control': 2, 'our': 2, "can't": 1, 'thoughts,': 1, 'but': 1, 'can': 1, 'words': 1})
print(a.most_common(2)) # get 2 most common elements
# [('we', 2), ('control', 2)]

# userdict
from collections import UserDict
# take a look also on UserList, UserString

class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 5)

    def __getitem__(self, item):
        super().__getitem__(item)

    def __delitem__(self, key):
        super().__delitem__(key)

d = MyDict({"one": 1, "two": 2})
print(d)
# {'one': 5, 'two': 10}






