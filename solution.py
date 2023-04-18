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


# Решение по блок-схеме

def sorted(collection):
    result = []
    ind_coll = 0
    end = len(collection)
    while ind_coll < end:
        if len(collection[ind_coll]) <= 3:
            result.append(collection[ind_coll])
        ind_coll += 1
    return result


print(sorted(coll1) == ["2", ":-)"])
print(sorted(coll2) == ["-2"])
print(sorted(coll3) == [])
