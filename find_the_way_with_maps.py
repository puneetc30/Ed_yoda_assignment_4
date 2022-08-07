size = int(input("Enter the size of list: "))
lst = [int(input("Enter a list element: ")) for i in range(size)]

new_3x = lambda num : num*3
new_3x_lst = list(map(new_3x,lst))
print(new_3x_lst)