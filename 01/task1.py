n = 30
my_list = [i for i in range(n)]

for i in my_list:
    if not i % 2 and i != 0:
        print(i)
