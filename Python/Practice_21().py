list2 = []
for _ in range(int(input())):
    try:
        name = input()
        number = float(input())
        lists = [[name, number]]
        list2 +=lists
        print(list2)
    except Exception as e:
        print ('correct it: ' ,e)
