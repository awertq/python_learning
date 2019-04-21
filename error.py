'''trying try and except block '''

a = 1


try:
	b = int(input("enter a num : "))
	print(a/b)

except ValueError as v:
	print("input correct value sir ")

except TypeError as t:
	print("you get an type error ")

except ZeroDivisionError as z:
	print("do not input zero ")

except Exception as e :
	print("you got some error and that is ",e)

finally:
	print("at end every thing go right")

print("THE END")
