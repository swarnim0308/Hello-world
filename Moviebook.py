l1=[]
for i in range(1,101):
	l1.append(i)
	print()
j=0
j=int(input(" 1. Book Seat \n 2. Exit \n Choice   :::::"))
while(j!=2):
	for i in l1:
		print(i,end="\t")
		if i%10==0:
			print()
				
		seat=int(input("Enter seat to book  : "))
		if seat in l1:
			#s_idx=l1.index(seat)	
			l1[seat-1]="Booked"

			print("Thank You your Seat is Booked :)  \n\n")
			print(l1)
        else:
        	if seat>100:
                        print("Invalid Input")
		else:
			print("Sorry !!! Seat is already booked")
	j=int(input("Enter 1 to continue    : "))	
else:
	print("Have a Nice Day SeeYA    : P  ")
