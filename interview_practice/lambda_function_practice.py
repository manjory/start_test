
from functools import reduce

'''practice lambda function with a few basic usages'''
# creating a fnction to multiply to numbers
multiply= lambda x,y : x*y
print(multiply(101,201))
#Creating a function to find the nth power of a number
power= lambda x,n: x**n
print(power(4,4))
#Create a function to find the double of the array of numbers
some_num=[1,2,238,102]
double=map(lambda x:x+x,some_num)
print(list(double))
#Create a function to capitalize the words in a given string
string=["My", "Name", "is", "Manjory"]
capitalize=map(lambda x: str.upper(x), string)
print(list(capitalize))
#sorting with lambda function:
attendance=[32,23,42,54,12,78]
# difference between sorted and sort functions:

print(sorted(attendance,reverse=True), attendance)# sorted does not actually sort "attendance".
attendance.sort(reverse=True)# to actually sort attendance we have to either say attendance=sorted(attendance,reverse=True), or just use sort function like here
print(attendance)
attendance.sort(key=lambda x:x*1.5)#use any function as x:x*1.5 to define how the sorting is to be done
print(attendance)
#sorting a tuple using the index =1
class_att=[('9A',32),('9B',23),('9C',42),('9D',54),('9E',12),('9F',78)]
print(sorted(class_att,key=lambda x:x[1]))# function used to sort the array class_att is x[1] which says
# that acording to the values at index=1 in each of the tuples in the given array, sort the class_att array

#filter and lambda function:

above_avg_att = list(filter(lambda x: x >=30 , attendance))
print('above average attendance=',above_avg_att)
#using filter for string type arrays:
#return countries with length of the name of the country >3
countries=['India', 'USA','Canada','Pakistan','Mexico','England', 'UAE']
count_greater_than_three=filter(lambda x: len(x)>3,countries)
print(list(count_greater_than_three))
'''using reduce function in lambda functions: it returns a single value'''

