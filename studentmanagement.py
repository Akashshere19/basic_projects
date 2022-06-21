import os
import platform

global liststd
liststd = ['yogesh','kishor','gajen','gopi']
def managementStudent():
    x='#'*30
    y='='*28
    global bye
    bye="\n {}\n# {}\n# ===>BROUGHT To You By <=== #\n#  ===>\n{} #\n {}".format(x,y,y,x)
    print("""
     ----------------------------------------------------------------
     |===============================================================|
     |===============================================================|
       -------------------------------------------------------------

    Enter 1: To View Studen's List
    Enter 2: To Add New Student
    Enter 3: To Search Student
    Enter 4: To Remove Student
                            """)
    try:
        userInput = int(input("Please Select An Above Option: "))
        
    except Exception:
        exit("\nHy ! That's Not A Number ")
    else:
        print("\n")

    if (userInput == 1):
        print("List Students\n")
        for students in liststd:
            print("=> {}".format(students))
    elif(userInput == 2):
        newstd = input("enter new student :")
        if (newstd in liststd):
            print("\nThis Student {} Already In Database".format(newstd))
        else:
            liststd.append(newstd)
            print("\nThis Student {} Successfully Add \n".format(newstd))
            for students in liststd:
                print("=> {}".format(students))
    elif(userInput == 3):
        srcstd = input("Enter Student Name To Search:")
        if(scrstd in liststd):
            print("\n=> Record Found of Student {}".format(srcstd))
        else:
            print("\n=> No Record Found of Student {}".format(srcstd))
    elif(userInput == 4):
        rmstd = input("Enter Student Name To Remove:")
        if(rmstd in liststd):
            liststd.remove(rmstd)
            print("\n=> student {} Successfully Deleted \n".format(rmstd))
            for students in liststd:
                print("=> Student {} Successfull y Deleted  \n".format(students))
        else:        
            print("=> No Record Found of This Student {}".format(rmstd))
    elif(userInput < 1 or userInput >4):
        print("Please Enter Valid Option")
managementStudent()        


    








                
