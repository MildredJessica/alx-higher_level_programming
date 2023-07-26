#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(-2)
my_list.append(4)
my_list.append(-9)
my_list.append(0)
my_list.append(-5)
print(my_list)
my_list.print_sorted()
print(my_list)

#Checking for module docstring:
m = __import__("1-my_list").MyList.print_sorted.__doc__
print(len(m) > 1)

l = MyList()
l.print_sorted()
