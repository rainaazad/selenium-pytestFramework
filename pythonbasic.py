# in a list there are 100 names for example, i want you to
# write a function which will take this list as an input and in the function,
# you need to go through entire list and print following details,
# each name and how many times it was present in the entire list


# name_list = input("enter all the candidate names ")
# user_list = name_list.split(",")
# print("\n")
# all_the_name = []


def names_list(all_names):
    user_list = all_names.split(",")
    for name in user_list:
        print(name)
    print(user_list)
    dict_name = {i: user_list.count(i) for i in user_list}
    print(dict_name)


#all_names = input("enter all the candidate names ")
#names_list(all_names)

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter


triangle = Triangle(3, 5, 6)
perimeter = triangle.get_perimeter()
print("the perimeter of the triangle is ", perimeter)
print("raina azad")