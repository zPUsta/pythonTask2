
# tasks for define function 

# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 


# ---------TASK1 version 1------------


# def sqrt_function(input_list):
#     sqrt_list = []
#     for num in input_list:
#         if num ** 0.5 = 0 and num ** 0.5 == int( num** 0.5):
#             sqrt_list.append(num)
#     return sqrt_list

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]    
# print(sqrt_function(mylist))

    
 
# ---------TASK1 version 2----------

# import math
# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# result = list(filter(lambda num: num >= 0 and math.sqrt(num) == int(math.sqrt(num)), mylist))
# print(result)


 
# ---------TASK1 version 3----------
# import math
# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# result = [num for num in mylist if num >= 0 and math.sqrt(num) == int(math.sqrt(num))]
# print(result)
  
  
  
#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']

# my_list = [-1,1,2,2,6,7,7,'say']
# result = list(set(my_list))
# print(result)




# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın
# Kullanıcıdan birden çok sayı alınması ve listeye dönüştürülmesi

# input_str = input("ədədləri daxil edin(aralarında boşluq qoyaraq):")
# my_list = input_str.split()  
# my_list = [int(x) for x in my_list]  
# result = 1

# for num in my_list:
#     result *= num

# print("Hasil", result)

  
# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın
# num = int(input("ədədi daxil edin:"))
# result = [i for i in range(1, num) if num % i == 0]
# print(result)

# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}

# mylist=['may','iyun','iyul']
# my_dict = {x: len(x) for x in mylist}
# print(my_dict)

# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']


# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# first_names = [x.split()[0] for x in names if isinstance(x, str)]  
# lowercase = [name.lower() for name in first_names]  
# print(lowercase)



# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# if len(nums1) != len(nums2):
#     print("Listelerin uzunlukları eşit değil.")
# else:
  
#     total_sum = sum(nums1[i] + nums2[i] for i in range(len(nums1)))
    

#     average = total_sum / len(nums1)
    
#     print("Ortalama:", average)






