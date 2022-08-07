size = int(input("Enter the size of list: "))
lst = [int(input("Enter a list element: ")) for i in range(size)]

sqr = lambda num : num*num
sqr_lst = list(map(sqr,lst))
print(sqr_lst)