# x=1
# for i in range(0,2001):
#     x%i==0
#     x=x+1
# print(x)


# marks=int(input("Hey garvit "))
# if(marks>90):
#     print("Garvit top")
# elif(80<marks>90):
#     print("Theek thak")
# elif(70<marks>80):
#     print("BElt")
# elif(60<marks>50):
#     print("Nikass"):
# elif()

from datetime import datetime, timedelta


    # Get user input for birthday
birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

    # Convert input string to a datetime object
birthday = datetime.strptime(birthday_str, '%Y-%m-%d')

    # Get the current date
today = datetime.now()

    # Calculate the number of Sundays
sunday_count = sum(1 for day in range((today - birthday).days + 1) 
                       if (birthday + timedelta(days=day)).weekday() == 6)

    # Display the result
print(f"You have lived {sunday_count} Sundays since your birthday.")