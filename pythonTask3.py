# ---------------TASK 1
# Task1 version 1
# def sqrt_function(input_list):
#     sqrt_list = []
#     for num in input_list:
#         if num >= 0 and num ** 0.5 == int(num ** 0.5):
#             sqrt_list.append(num)
#     return sqrt_list

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]    
# print(sqrt_function(mylist))

# Task1 version 2


# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# result = list(filter(lambda num: num >= 0 and num ** 0.5 == int(num ** 0.5), mylist))
# print(result)


# Task1 version 3


# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# result = [num for num in mylist if num >= 0 and num ** 0.5 == int(num ** 0.5)]
# print(result)






# ---------------TASK 2

# my_list = [-1,1,2,2,6,7,7,'say']
# def remove_duplicates(input_list):
#     result = list(set(my_list))
#     return result


# print(remove_duplicates(my_list))


# ------------TASK3

# input_int = input("ədədləri daxil edin(aralarında boşluq qoyaraq):")
# def math_function(iput_number):
#     my_list = input_int.split()  
#     my_list = [int(x) for x in my_list]  
#     result = 1
    
#     for num in my_list:
#      result *= num
     
#     return result
    
    
# print(math_function(input_int))

# ------------TASK4

# num = int(input("ədədi daxil edin:"))
# result = [i for i in range(1, num) if num % i == 0]
# print(result)



# ------------TASK5
# mylist=['may','iyun','iyul']
# my_dict = {x: len(x) for x in mylist}
# print(my_dict)
    
    
# ------------TASK6    
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# first_names = [x.split()[0] for x in names if isinstance(x, str)]  
# lowercase = [name.lower() for name in first_names]  
# print(lowercase)
    
     # 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# if len(nums1) != len(nums2):
#     print("uzunluq eyni deyil")
# else:
  
#     total_sum = sum(nums1[i] + nums2[i] for i in range(len(nums1)))
    

#     average = total_sum / len(nums1)
    
#     print("Ortalama:", average)
