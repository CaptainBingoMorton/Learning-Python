# This function returns the smallest integer from a list of integers
def smallestinteger(listofintegers):
# If the length of the list of integers is zero or the type of it is not a list then return none
    if len(listofintegers)==0 or type(listofintegers)!=list:
        return None
    smol=listofintegers[0]
# for each item in the list
    for tiny in listofintegers:
# IF any item in the list is not an integer then skip it
        if type(tiny)!=int:
            continue
# If we find a smaller integer then keep track of it using the smol variable
        if tiny < smol:
            smol=tiny
    return smol


print (smallestinteger([3,"stringtheory",5,6,]))
print (smallestinteger([10,4,5,6,]))
print (smallestinteger([]))
print (smallestinteger( "stringtheory" ))