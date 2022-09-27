
#Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with recursion. Note: the input will contain only integers or lists.


def recursive_inner(input_list):    #I think this works for what we need. It doesn't work on more complex lists, like ([1,2,3,4,[5,6,7,11],12,[13,14,[15,16]]])
    empty = []
    for item in input_list:
        if isinstance(item, list):
            return(recursive_inner(item))
        else:
            item +=1
            empty.append(item)
    return(empty)


recursive_inner([1,2,3,4,[5,6,7,[8,9]]])
