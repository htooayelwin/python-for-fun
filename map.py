import random
import string

test_list = [x for x in "".join(random.choice(string.ascii_lowercase) for i in range(3))]

print(test_list)