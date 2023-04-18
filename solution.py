coll1 = ["Hello", "2", "world", ":-)"]  # -> [“2”, “:-)”]
coll2 = ["1234", "1567", "-2", "computer science"]  # -> ["-2"]
coll3 = ["Russia", "Denmark", "Kazan"]  # -> []


def sorted_len_less_4(collection):
    result = []
    for el in collection:
        if len(el) < 4:
            result.append(el)
    return result


print(sorted_len_less_4(coll1) == ["2", ":-)"])
print(sorted_len_less_4(coll2) == ["-2"])
print(sorted_len_less_4(coll3) == [])
