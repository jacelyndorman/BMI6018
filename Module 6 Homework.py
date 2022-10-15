#1.a
#Using the print() function only, get the wrong_add_function to print out where
#it is making a mistake, given the expected output for ex, "we are making an error 
#in the loop", which you would put near the loop. 
#Structure the print() statement to show what the expected output ought to be
#via f-strings: ie "The correct answer is supposed to be: [...]".


def wrong_add_function(arg1,arg2):
    arg1_index=0
    while arg1_index < len(arg1):
        print("There is an error in the while+for loop code. It is unnecessarily calculating the sum 3 times instead of 1, shown below.")
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            correct = arg1[arg1_index]+ arg2[arg1_index]
            print(f"There is also an error in the addition code. The correct output is supposed to be: {correct}, but the output is {arg_2_sum}.")
        arg1[arg1_index]=arg_2_sum  
        arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]
wrong_add_function(arg1, arg2)

#1.b
#Then, changing as little as possible, modify the function, using the same 
#general structure to output the correct answer. Call this new function 
#correct_add_function() 

def correct_add_function(arg1,arg2): #This one I changed as little as possible. I left the loop error, so it is not the most efficient code, but it works.
    arg1_index=0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = arg1[arg1_index]+ arg2[arg1_index]
        arg1[arg1_index]=arg_2_sum  
        arg1_index+=1
    return arg1

arg1 = [1,4,8]
arg2 = [1,1,2]
correct_add_function(arg1, arg2)


#1.b continued

# def correct_add_function(arg1,arg2): #This one I also fixed the loop error. Now it only adds the values once, so it is more efficient, but I changed it more from the original code. 
#     arg1_index=0
#     while arg1_index < len(arg1):
#         arg_2_sum = arg1[arg1_index]+ arg2[arg1_index]
#         arg1[arg1_index]=arg_2_sum  
#         arg1_index+=1
#     return arg1

# arg1 = [1,4,8]
# arg2 = [1,2,5]
# correct_add_function(arg1, arg2)


#2.a
# #Update the numeric section of the function with your changes from 1 for both 
# #2.b and 2.c


# def wrong_add_function(arg1,arg2): #This is confusing. If I add the updates from 1, it will not add the way it describes below.
#     '''
#    The function takes in two lists of integers, then it adds
#    all of arg2 to each item of arg1.
   
#    Example:
#       > wrong_add_function([1,2,3],[1,1,1])
#       > [4,5,6]
   
#    If the lists are lists of strings, concatenate them
#    Example:
#       > wrong_add_function(['1','2','3'],['1','1','1'])
#       > ['1111','2111','3111']
#    Parameters
#    ----------
#    arg1 : list
#       list of integers.
#    arg2 : list
#       list of integers.
#    Returns
#    -------
#    arg1 : list
#       Elements of arg1, with each element having had the contents of 
#       arg2 added to it.
#    '''
#    #numeric section
#     if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2): 
#         arg1_index=0
#         while arg1_index < len(arg1):
#             arg_2_sum = 0
#             for arg2_elements in arg2:
#                 arg_2_sum = arg1[arg1_index]+ arg2[arg1_index]
#             arg1[arg1_index]=arg_2_sum  
#             arg1_index+=1
#         return arg1
#    #string section
#     elif sum([type(i)==str for i in arg1])==len(arg1) and sum([type(i)==str for i in arg2])==len(arg2): #Checking that all are strings
#         arg1_index=0
#         while arg1_index < len(arg1):
#             arg_2_sum = ''
#             for arg2_elements in arg2:
#                 arg_2_sum += arg2_elements
#             arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
#             arg1_index+=1
#         return arg1
    
# arg_str_1=["1","2","3"]
# arg_str_2=["1","1","1"]
# wrong_add_function(arg_str_1,arg_str_2)


#2.b

# #I DID IT ON THE WRONG FREAKING CODE :,)
# '''
# def exception_add_function(arg1,arg2):
#     arg1_index=0
#     while arg1_index < len(arg1):
#         arg_2_sum = 0
#         for arg2_elements in arg2:
#             try:
#                 if type(arg1[arg1_index]) != int and type(arg2[arg1_index]) != int:
#                     elements = []
#                     elements.append(arg1[arg1_index])
#                     elements.append(arg2[arg1_index])
#                     raise Exception("first and second")
#                 elif type(arg1[arg1_index]) != int:
#                     elements = arg1[arg1_index]
#                     raise Exception("first")
#                 elif type(arg2[arg1_index]) != int:
#                     elements = arg2[arg1_index]
#                     raise Exception("second")
#                 else:
#                     arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
#             except Exception as whichargument:
#                 arg_2_sum = "error"
#                 print(f"Your {whichargument} input argument(s) at index {arg1_index}, element(s) {elements}, is not of the expected type. Please change to an integer and rerun.")
#                 break
#         arg1[arg1_index]=arg_2_sum  
#         arg1_index+=1
#     return arg1

# arg1 = ["1",2,3]
# arg2 = ["4",5,6]
# exception_add_function(arg1, arg2)

# '''


#2.b
#Without modifying the string section code itself or the input directly, 
#write a try, except block that catches the issue with the input below and 
#returns an error message to the user, in case users give invalid inputs,
#(for example an input of ["5","2", 5])
#: "Your input argument [1 or 2] at element [n]
#is not of the expected type. Please change this and rerun. Name this function 
#exception_add_function()

def exception_add_function(arg1,arg2):
   #numeric section
    if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2):
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index]+ sum(arg2)
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
        return arg1
   #string section
    elif sum([type(i)==str for i in arg1])==len(arg1) and sum([type(i)==str for i in arg2])==len(arg2):
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
        return arg1
    #try/except block 
    else:
        try:
            elements = []
            if sum([type(i)==int for i in arg1]) < len(arg1) and sum([type(i)==int for i in arg2])==len(arg2):
                for i in arg1:
                    if type(i) != int:
                        elements.append(i)
                raise Exception("first")#Error: There are fewer integers in arg1 than arg2.
            elif sum([type(i)==int for i in arg1]) == len(arg1) and sum([type(i)==int for i in arg2]) < len(arg2):
                for i in arg2:
                    if type(i) != int:
                        elements.append(i)
                raise Exception("second")#Error: There are fewer integers in arg2 than arg1.
            elif sum([type(i)==str for i in arg1]) == len(arg1) and sum([type(i)==str for i in arg2]) < len(arg2):
                for i in arg2:
                    if type(i) != str:
                        elements.append(i)
                raise Exception("second")#Error: There are fewer strings in arg2 than arg1.
            elif sum([type(i)==str for i in arg1]) < len(arg1) and sum([type(i)==str for i in arg2])==len(arg2):
                for i in arg1:
                    if type(i) != str:
                        elements.append(i)
                raise Exception("second")#Error: There are fewer strings in arg1 than arg2.
            else:
                print("Your input arguments are a mess. Please rethink your life and change all values to either integers or strings.")
        except Exception as whichargument:
            print(f"Your {whichargument} input argument at element(s) {elements}, is not of the expected type. Please change and rerun.")
                 
    
arg_str_1=["1","2",3]
arg_str_2=[1,1,1]
exception_add_function(arg_str_1,arg_str_2)


#2.c
#Without modifying the string section code itself or the input directly, 
#write a try, except block that catches the issue with the input below and 
#gets it to process via the string section. IE, do not, outside the function,
#change the values of arg_str_1 or arg_str_2. Name this function 
#correction_add_function(), i.e you will not be updating the wrong_add_function,
#you will simply handle the error of wrong inputs in a seperate function, you want
#the wrong_add_function to output its current result you are only bolstering the 
#function for edge cases .



def wrong_add_function(arg1,arg2):
    '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   '''
   #numeric section
    if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2): #Checking that all are integers
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index]+ sum(arg2)
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
        return arg1
            
   #string section
    elif sum([type(i)==str for i in arg1])==len(arg1) and sum([type(i)==str for i in arg2])==len(arg2): #Checking that all are strings
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
        return arg1
    
    #try/except block 
    else:
        try:
            if sum([type(i)==int for i in arg1]) < len(arg1) or sum([type(i)==int for i in arg2]) < len(arg2):
                raise Exception #either argument is not all integers.
            elif sum([type(i)==str for i in arg1]) < len(arg1) or sum([type(i)==str for i in arg2]) < len(arg2):
                raise Exception #either argument is not all strings.
            else:
                print("Your input arguments are a mess. Please rethink your life and change all values to either integers or strings.")
        except Exception:
            return(correction_add_function(arg1, arg2))

    
def correction_add_function(arg1, arg2):
    for i in range(len(arg1)):
        arg1[i] = str(arg1[i])
        arg2[i] = str(arg2[i])
    return(wrong_add_function(arg1, arg2))

    
arg_str_1=[1,2,3]
arg_str_2=["1","1","1"]
wrong_add_function(arg_str_1,arg_str_2)

