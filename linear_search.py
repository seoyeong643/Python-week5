# def linear_search(the_list, target):
#     for x in range(len(the_list)):
#         if the_list[x] == target:
#             print("Found at index", x)
#             return x
#     print("Target is not in the list")
#     return -1

# my_list = [6, 3, 4, 2, 5, 7]
# linear_search(my_list, 5)
# linear_search(my_list, 3)
# linear_search(my_list, 8)

def linear_search_dictionary(dictionary, target):
    for key, value in dictionary.items():
        if value == target:
            print("Found at key", key)
            return key
    print("Target is not in the dirctionary")

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)