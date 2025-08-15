user_score = int(input("Enter the name of the user :"))
if (user_score >=50 and user_score <=100):
    print("The User has passsed the exams ")
elif(user_score < 50 and user_score >=0):
    print("The user has failed the exams ")
else:
    print("Invalid score entered")