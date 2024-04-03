inp=input("Enter number")
nums=inp.split()
list = [int(num) for num in nums]
print(list)

# list=[3,3,3,2,2,2]
for i in list:
	# print('i',i)
	if list.count(i)>=len(list)/2:
		print('max',i)
		break