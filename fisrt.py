import random
import string

random_range = random.randint(1,30000) 

def random_list(x, y):
    test_list = []
    atoz = string.ascii_lowercase
    print("The range is ", x)
    for xx in range(x):
        test_list.append("".join(random.choice(atoz) for i in range(y)))
    return test_list

def find_duplicate(x):
    duplicate = []
    for xx in x:
        if x.count(xx) > 1:
            if xx not in duplicate:
                duplicate.append(x.count(xx))
                duplicate.append(xx)
    return duplicate

print(random_list(100,2))
print(find_duplicate(random_list(100, 1)))
