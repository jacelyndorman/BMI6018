
#Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with a while loop. Note: the input will contain only integers or lists. 
#As an example:
#input_list = [1,2,3,4,[5,6,7,[8,9]]]
#your_py_program.py input_list will produce:
#[9,10]
#That is [8, 9] (the inner most list) plus 1 -> [9, 10]


#Amy's idea: Works better than my last one, but I tried yours and it's working too!
input_list = [1,2,3,4,[5,6,7,[8,9]]]

i = 0
sublist = []
while i < len(input_list):
    for x in (input_list):
        if type(x) == list:
            input_list = x
            continue  
    i +=1
k=1
output_list = [j + k for j in input_list] 
print(output_list)


def while_inner(input_list):     #I think this actually works. - Jacelyn
    islist = True
    while islist:
        empty = []
        for i in input_list:
            if isinstance(i, list):
                islist = True
                input_list = i
                break
            else:
                islist = False
                i += 1
                empty.append(i)
    return(empty)
            
            
    
print(while_inner([1,2,3,4,[5,6,7,[8,9,[10,11],12]]]))
