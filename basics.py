# Using python as a calculator

print(10/2)

print(8 * 4)

print(2 + 3)

# Review Modulo (tells you the remainder of a divisional problem)

print(5%2)

# example using expentation (Compounding interest)
#  A = P * (1+r)^t

print(100 * 1.1**7)

# Types, intager, floats, bools, string. (Variables)

savings = 100
factor = 1.1
time = 7
desc = "Compound Interest"
print(type(savings))
print(type(factor))
print(type(desc))

result = savings * factor**time

print(result)

doubledesc = desc + desc

print(type(doubledesc))
print (doubledesc)

print("I started with $"+str(savings)+" and now have $"+str(result)+ ", awesome!")

# Def of a pi_string

pi_string = "3.1415926539"

print(float(pi_string))

# Can python hanle everything. (true = 1, false = 0)

print(desc * 2)

print(True + True)

# Lists

austin = 17
eli = 16
joe = 28
noah = 16

ages = [austin, eli, joe, noah]
print(type(ages))
print(ages)

ages = ["Austin", austin, "Eli", eli, "Joe", joe, "Noah", noah]
print(ages)

a = [1,2,3,4]
b = [[1,2,3], [4,5,6]]
c = [1 + 2, "a"*5,3]

print(a)
print(b)
print(c)

# ages = [["Austin", austin],["Eli", eli],["Joe", joe],["Noah", noah]]

print(ages[1])
print(ages[1]==17)

if ages[1]==17:
	print("YOUR RIGHT! :) "*5)

print(ages[-1])

print(ages[-3])

print(ages[5] == ages[-3])

print(ages[1] + ages[3])

# Slicing list

ages1 = ages[0:(len(ages)/2)]
print(ages1)

ages2 = ages[(len(ages))/2: len(ages)]
print(ages2)

ages = [["Austin", austin],["Eli", eli],["Joe", joe],["Noah", noah]]

#Indexing lists within lists
print(ages[1])
print(ages[1][1])

ages[2][1] = 29

print(ages)

ages[1][0] = "Elijah"
print(ages)

ages1 = ages + [["Mason", 11]]

print(ages1)

# Remove Element

ages1.remove(ages1[4])

print(ages1)

















