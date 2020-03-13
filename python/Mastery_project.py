x = 0
First = input("What is your first name: ") 
Last = input("What is your last name: ")
ID = input("What is your student ID: ")
schedule = f"*************************************************\n*\t\t\t\t\t\t*\n*\t{Last},{First}\tID:{ID}\t\t*\n*\t\t\t\t\t\t*\n*************************************************\n*\t\t\t\t\t\t*"
print (f"*************************************************\n*\t\t\t\t\t\t*\n*\t{Last},{First}\tID:{ID}\t\t*\n*\t\t\t\t\t\t*\n*************************************************")
while True:
    class1 = input("Enter your first class, enter Stop to end:")
    if class1 == "Stop":
        break
    room1 = input("Enter the room number: ")
    x += 1
    print (f"\n*\tBlock{x}:{class1}\t\tRoom:{room1}\t*")

    schedule += (f"\n*\tBlock{x}:{class1}\t\tRoom:{room1}\t*")
   
print(schedule)
print("*\t\t\t\t\t\t*\n*************************************************\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t*\n*************************************************")