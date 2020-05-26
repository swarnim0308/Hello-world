print("STUDENT MANAGEMENT SYSTEM\n\n 1. Add Student Record\n 2.Display All Student Record\n 3.Display Student Record by Roll\n4.Update Student Record\n 5. Delete Record \n 6. Exit")
choice=0
while(choice!=6):
	choice=int(input("Choice Is :::    "))
	if choice==1:
		student={}
		roll=int(input("Enter Student Id ::   "))
		name =input("Enter Name ::   ")
		gender=input("Gender is ::")
		marks=input("Enter Marks ::")
		student.update({roll:[name,gender,marks]})
		print("Record Added Succesfully")
	elif choice==2:
		print("-------------------------------------------\nRoll \tName \tGender \tMarks\n-------------------------------------------")
		for i in student.items():
			print(i[0],end="\t")
			for j in i[1]:
				print(j,end="\t")
			print()
			print("-------------------------------------------")	
				
	elif choice==3:
		name=input("Enter Name of Student to display Record ::")
		print("-------------------------------------------\nRoll \tName \tGender \t Marks\n-------------------------------------------")
		for i in student.items():
			if name in i[1]:
				print(i[0],end="\t")
				for j in i[1]:
					print(j,end="\t")
				print()
			print("-------------------------------------------")	
				
	elif choice==4:
		roll=int(input("Enter rollno. whose record to be updated ::"))
		if i in student.keys():
			if roll == i:
				name=input("Enter new Name")
				gender=input("Enter new gender")
				marks=int(input("Enter new marks"))
			student[roll]=[name,gender,marks]
			print("\nUpdated Record . . . . ThankYou   :)  ")
		else:
			print("Invalid Rollno..... Record Not Found  :(   ")		
	elif choice==5:
		roll=int(input("Enter RollNo. to delete"))
		if roll in student.keys():
			student.pop(roll)
			print("Record Deleted Succesfully")
		else:
			print("Invalid Roll no.")
	elif choice==6:
		pass	
	else:
		print("Invalid Choice    : (    ")