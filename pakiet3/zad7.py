from collections import defaultdict

def merge_dicts(*dicts):
    merged_dict = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            merged_dict[key] += value
    return dict(merged_dict)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
dict3 = {'c': 5, 'd': 6, 'e': 7}

merged = merge_dicts(dict1, dict2, dict3)
print(merged)