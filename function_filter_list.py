
#Question 3
#Write a python program that, given an input list, will filter the input above a user defined threshold. 
#This is to be done with a standard function.
#That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]



def function_filter(input_list, input_number):
    newlist = []
    for i in input_list:
        if i <= input_number:
            newlist.append(i)
    return(newlist)

function_filter([1,2,3,4,5,6,7,8,9], 6)
