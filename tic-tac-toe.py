from random import randint

arr = []
flags = []

for i in range(9):
	arr.append(".")
	flags.append(False)

p1 = int(input("p1:"))

arr[p1] = 'X'
flags[p1] = True

while True:

	b1 = randint(0,8)

	if flags[b1] == False:
		arr[b1] = "O"
		flags[b1] = True
		break

	else:
		print("rerun")

print(arr)

while True:

	p2 = int(input("p2:"))

	if flags[p2] == False:
		arr[p2] = "X"
		flags[p2] = True
		break

	else:
		print("rerun")

while True:

	b2 = randint(0,8)

	if flags[b2] == False:
	   arr[b2] = "O"
	   flags[b2] = True
	   break

	else:
		print("rerun")

print(arr)

while True:

	p3 = int(input("p3:"))

	if flags[p3] == False:
		arr[p3] = "X"
		flags[p3] = True
		break

	else:
		print("rerun")

print(arr)

if (arr[0] == "X" and arr[1] == "X" and arr[2] == "X") or (arr[3] == "X" and arr[4] == "X" and arr[5] == "X") or (arr[6] == "X" and arr[7] == "X" and arr[8] == "X") or (arr[0] == "X" and arr[3] == "X" and arr[6] == "X") or (arr[1] == "X" and arr[4] == "X" and arr[7] == "X") or (arr[2] == "X" and arr[5] == "X" and arr[8] == "X") or (arr[0] == "X" and arr[4] == "X" and arr[8] == "X") or (arr[2] == "X" and arr[4] == "X" and arr[6] == "X"):

	print("Victory")
	exit()

else:

	pass

while True:

	b3 = randint(0,8)

	if flags[b3] == False:
	   arr[b3] = "O"
	   flags[b3] = True
	   break

	else:
		print("rerun")

print(arr)

if (arr[0] == "O" and arr[1] == "O" and arr[2] == "O") or (arr[3] == "O" and arr[4] == "O" and arr[5] == "O") or (arr[6] == "O" and arr[7] == "O" and arr[8] == "O") or (arr[0] == "O" and arr[3] == "O" and arr[6] == "O") or (arr[1] == "O" and arr[4] == "O" and arr[7] == "O") or (arr[2] == "O" and arr[5] == "O" and arr[8] == "O") or (arr[0] == "O" and arr[4] == "O" and arr[8] == "O") or (arr[2] == "O" and arr[4] == "O" and arr[6] == "O"):

	print("Defeat")
	exit()

else:

	pass

while True:

	p4 = int(input("p4:"))

	if flags[p4] == False:
		arr[p4] = "X"
		flags[p4] = True
		break

	else:
		print("rerun")

print(arr)

if (arr[0] == "X" and arr[1] == "X" and arr[2] == "X") or (arr[3] == "X" and arr[4] == "X" and arr[5] == "X") or (arr[6] == "X" and arr[7] == "X" and arr[8] == "X") or (arr[0] == "X" and arr[3] == "X" and arr[6] == "X") or (arr[1] == "X" and arr[4] == "X" and arr[7] == "X") or (arr[2] == "X" and arr[5] == "X" and arr[8] == "X") or (arr[0] == "X" and arr[4] == "X" and arr[8] == "X") or (arr[2] == "X" and arr[4] == "X" and arr[6] == "X"):

	print("Victory")
	exit()

else:

	pass

while True:

	b4 = randint(0,8)

	if flags[b4] == False:
		arr[b4] = "O"
		flags[b4] = True
		break

	else:
		print("rerun")

print(arr)

if (arr[0] == "O" and arr[1] == "O" and arr[2] == "O") or (arr[3] == "O" and arr[4] == "O" and arr[5] == "O") or (arr[6] == "O" and arr[7] == "O" and arr[8] == "O") or (arr[0] == "O" and arr[3] == "O" and arr[6] == "O") or (arr[1] == "O" and arr[4] == "O" and arr[7] == "O") or (arr[2] == "O" and arr[5] == "O" and arr[8] == "O") or (arr[0] == "O" and arr[4] == "O" and arr[8] == "O") or (arr[2] == "O" and arr[4] == "O" and arr[6] == "O"):

	print("Defeat")
	exit()

else:

	pass

while True:

	p5 = int(input("p5:"))

	if flags[p5] == False:
		arr[p5] = "X"
		flags[p5] = True
		break

	else:
		print("rerun")

print(arr)

if (arr[0] == "X" and arr[1] == "X" and arr[2] == "X") or (arr[3] == "X" and arr[4] == "X" and arr[5] == "X") or (arr[6] == "X" and arr[7] == "X" and arr[8] == "X") or (arr[0] == "X" and arr[3] == "X" and arr[6] == "X") or (arr[1] == "X" and arr[4] == "X" and arr[7] == "X") or (arr[2] == "X" and arr[5] == "X" and arr[8] == "X") or (arr[0] == "X" and arr[4] == "X" and arr[8] == "X") or (arr[2] == "X" and arr[4] == "X" and arr[6] == "X"):

	print("Victory")
	exit()

else: 
	
	print("Tie)
