#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Example

zero_a = ['jacelyn','second','third','fourth','fifth']
zero_b = zero_a[0].upper()
zero_c = hex(ord(zero_a[0][0]))

print (zero_b)
print (zero_c)
print (ord(zero_a[0][0]))


# In[2]:


#Problem 1: Lists, Sets and Coersion
#1.a Create a list of integers no fewer than 10 items from 0 to 9.
integers = [0,1,2,3,4,5,6,7,8,9]
backupintegers = [0,1,2,3,4,5,6,7,8,9]
one_a = integers
print(one_a)
# .b Add 3 to the 5th indexed element
integers.insert(5, 3)
one_b = integers
print(one_b)
# .c Coerce all elements in the list to floats using list comprehension
floats = [float(x) for x in integers]
one_c = floats
print (one_c)
# .d Coerce the list to a set
set1 = set(floats)
one_d = set1
print(one_d)
# .e Using a method, append int 10 to the set
set1.add(10)
one_e = set1
print(one_e)
# .f Using a method, pop an item from the set
set1.pop()
one_f = set1
print(one_f)
# .g Using a length counting function, count the number of items in the set
one_g = len(set1)
print (one_g)
# .h Check if the number of items in the set is the same as the 
#    number of items in the list
one_h = len(set1) == len(integers)
print (one_h)
# .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
one_i = list(set1) + backupintegers
print(one_i)
# .j Coerce 1.i to a set
one_j = set(one_i)
print (one_j)
# .k Count the number of elements in the 1.j
one_k = len(one_j)
print (one_k)



# In[3]:


#Problem 2: Dictionary woes

#2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
#    two_a, ensure the key names are the same as the dictionary names.

two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

two_a = {
    'two_patient_dictionary_kinoko' : {"name" : "Kinoko","year" : 2021},
    'two_patient_dictionary_dango'  : {"name" : "Dango", "year" : 2019},
    'two_patient_dictionary_mochi'  : {"name" : "Mochi", "year" : 2020}
}

print(two_a)

# .b Using keys, retrieve the Dango's name from 2.a
two_b = two_a['two_patient_dictionary_dango']["name"]
print(two_b)

# .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
#    and should simply update 2.a.
two_a['two_patient_dictionary_mochi']["year"] = 2018

# .d Manually create a dictionary that has a single level and contains each patient
#    as the key and the year as the value. Set Mochi's year to 2019.'
two_d = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019
    
}
print(two_d)
# .e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
print(two_e)
# .f Coerce the values of 2.d into a list
two_f = list(two_d.values())
print(two_f)
# .g Use the zip function to combine 2.e and 2.f into a dictionary again
two_g = dict(zip(two_e, two_f))
print(two_g)


# In[4]:


#Problem 3: Set combinations

#Given the predefined sets below and using set methods
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
#3.a Is set E a subset of set A
three_a = three_setE.issubset(three_setA)
print(three_a, "(Yes)")
# .b Is set E a strict subset of set A
three_b = three_setE.issubset(three_setA) and len(three_setA) != len(three_setE)
print(three_b, "(Yes)")
# .c Create a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print(three_c)
# .d Create a set that is the union of sets C, D and E
three_d = three_setC | three_setD | three_setE
print(three_d)
# .e add 9 to the set
three_d.add(9)
three_e = three_d
print(three_e)
# .f Using == compare this set to the list in one_a
three_f = three_e == backupintegers
print(three_f)
# .g Explain why they are not the same. What would you need to change if you
#    wanted this to be True?
three_g = "The list and set do not contain the same numbers. Additionally, sets and lists are different and cannot be compared this way if you are looking for whether the elements are the same. They would not equal each other even if they contained the same numbers."
print(three_g)



# In[13]:


#Problem 4: Changing variable types

#For each step you will modify a variable, then append the type of the variable
#to a list. Do not recreate the list variable, it should be a running list of 
#types.

#4.a Create a variable of type int with the value of 8
four_a = 8
print(four_a)
# .b Create an empty list 
four_b = []
print(four_b)
# .c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
four_c = four_b
print(four_c)
# .d Add 0.39 to 4.c
four_c.append(3.9)
four_d = four_c
print(four_d)
# .e append the type of 0.39 to the list
four_d.append(type(0.39))
four_e = four_d
print(four_e)
# .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
#    decimal places, and append to list.
four_e.append(int(0.39**-10))
four_f = four_e
print(four_f)
# .g append the type to the list
four_f.append(type(12284))
four_g = four_f
print(four_g)
 


# In[14]:


#Problem 5: More variable type changes

#Continue from where you left off in Problem 4.

#5.a Manually create a dictionary where the values are items in the list from where we left in 
#   problem 4, and the keys should be their index in the list. Print the dictionary.

index = list(range(len(four_g)))
five_a = dict(zip(index, four_g))
print(five_a)
# .b Add 300 and coerce it into a string
number = str(300)
four_g.append(number)
five_b = four_g
print(five_b)
# .c append the type to the list
five_b.append(type(number))
five_c = five_b
print(five_c)
# .d slice the string up to the 2nd element
five_d = number[0:2]
print(five_d)
# .e append the type to the list
five_c.append(type(five_d))
five_e = five_c
print(five_e)
# .f use list comprehension to convert this into a new list of integers
five_f = [*five_d]
print(five_f)
# .g append the type to the list
five_e.append(type(five_f))
five_g = five_e
print(five_g)
# .h append the type of three_setA to the list
five_g.append(type(three_setA))
five_h = five_g
print(five_h)


# In[ ]:





# In[ ]:




