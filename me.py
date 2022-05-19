print('Hello My Happy client please provide  your details')


username=input("My  Name is;=")
age=int(input("What is Your Age: "))
height=float(input("Your Current Height is:"))
weight=float(input("Please Enter Your Current Weight: "))
Phone_no=int(input("Phone No is "))
home_place=input('My home place is:')


bmi= weight / (height*height)
print("The Details of the client are as follows \n\n\n\n\n")
print(f"the Client name is {username}")
print(f'The client age is {age}')
print(f'Bmi is {bmi} KG')
print(f'The Phone No is {Phone_no}')
print(f'The Home Place is {home_place}')