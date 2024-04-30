def generate_permutations(lst):
    if len(lst) == 0:
        return [[]]
    elif len(lst) == 1:
        return [lst]
    else:
        permutations = []
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in generate_permutations(rest):
                permutations.append([lst[i]] + p)
        return permutations

lst = [1, 2, 3]

permutations = generate_permutations(lst)
print(permutations)