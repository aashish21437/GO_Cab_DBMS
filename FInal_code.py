import mysql.connector as c
import time
mydb=c.connect(host="localhost",user="root",passwd="#Aashish21437", database="gocab_final_db")
if mydb.is_connected():
    print("\n\n\nsuccessfully connected with Database\n\n\n")

mycursor = mydb.cursor()

def feedback():
      stars = int(input("Please Enter Rating for the Ride Experience: "))
      mycursor.execute('UPDATE details_of_driver SET rating = \'{}\' WHERE driver_id = {};'.format(stars, username))
      mycursor.execute('UPDATE details_of_driver SET status = \'available\' WHERE driver_id = {};'.format(username))
      mydb.commit()

      print("\n\n\nThank you For Sharing Your Valuable Feedback, New Rides Are always waiting for you\n\n\n")

def rideEnding():
      time.sleep(5)
      print("Ride Ended\n\nThank You For Choosing GoCab, Please Provide Your Valuable Feedback\n\n")
      feedback()

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

def bookConfirm():
        ride_id_no = username
        confirmation = int(input("\n\n\nDo you wish to Book The Ride?\n1. Yes\n2. No, I want to Book Different Ride\n\nSelect Your Option: "))
        if(confirmation==1):
              mycursor.execute('UPDATE details_of_driver SET status = \'booked\' WHERE driver_id = {};'.format(ride_id_no))
              mydb.commit()
              return True

        elif(confirmation==2):
              return False
        else:
              print("\n\nKindly Select Appropriate Option\n\n")
              bookConfirm()
      

def payment():
        mycursor.execute("select  from details_of_customer where username = {}".format(username))
        for tb in mycursor:
              if(username==convertTuple(tb)):
                    return(True)
              return(False)

def rideDetails():
      ridedetailprint = ["Ride ID: ", "Driver Contact Number: ", "Customer Contact Number: ", "Pickup Location: ", "Drop Location: ", "Amount: ", "Payment Method", "Car Model: ", "Driver ID: ", "Customer Username: \n\n\n"]
      rideDetailPrintData = []
      if(int(username)<=150):
            mycursor.execute("select * from ride_details where username = {}".format(username))
      else:
            mycursor.execute("select * from ride_details where username = {}".format(str(int(username)-75)))
      for tb in mycursor:
            rideDetailPrintData = list(tb)
      counter = 0
      for counter in range(len(ridedetailprint)-1):
            # print(counter)
            print(ridedetailprint[counter], rideDetailPrintData[counter])

      if(bookConfirm()==True):
            print("\n\nBooking Confirmed\n\n")
            rideEnding()

      else:
            booking()

def booking():
      pickLocate = input("Please Enter Your Pickup Location: ")
      dropLocate = input("Please Enter Your Drop Location: ")
      if(int(username)<=150):
            print("\n\n\nEntrered the 150 ke niche\n\n\n")
            if(pickLocate==dropLocate):
                  print("\n\nPlease Enter different locations\n\n")
                  booking()
            else:
                  #print(username)
                  mycursor.execute('UPDATE ride_details SET pick_location = \'{}\' WHERE username = {};'.format(pickLocate, username))
                  mycursor.execute('UPDATE ride_details SET drop_location = \'{}\' WHERE username = {};'.format(dropLocate, username))
                  mydb.commit()
                  rideDetails()
      else:
            print("\n\n\nEntrered 150 ke upar\n\n\n")
            if(pickLocate==dropLocate):
                  print("\n\nPlease Enter different locations\n\n")
                  booking()
            else:
                  mycursor.execute('UPDATE ride_details SET pick_location = \'{}\' WHERE username = {};'.format(pickLocate, str(int(username)-75)))
                  mycursor.execute('UPDATE ride_details SET drop_location = \'{}\' WHERE username = {};'.format(dropLocate, str(int(username)-75)))
                  mydb.commit()
                  rideDetails()

def login():
        verified = False
        global username
        username = input("Enter your Username: ")
        mycursor.execute("select username from details_of_customer where username = {}".format(username))
        for tb in mycursor:
              if(username==convertTuple(tb)):
                    return(True)
              return(False)

def signup():
        mycursor.execute('SELECT COUNT(username) FROM details_of_customer;')
        totalUsers = mycursor.fetchone()[0]
        nameOfCust = input("name: ")
      #   print(name)
        ContactNum = int(input("Contact Number: "))
      #   print(ContactNum)
        emailId = input("Email ID: ")
      #   print(emailId)
      #   sql = "INSERT INTO details_of_customer (username, name_of_customer, customer_contact_number, email_of_customer) VALUES (%s, %s, %s, %s)"
        mycursor.execute("INSERT INTO details_of_customer (username, name_of_customer, customer_contact_number, emai_of_customer) VALUES ({}, \'{}\', {}, \'{}\')".format(totalUsers+1,nameOfCust,ContactNum,emailId))
        mydb.commit()

def menuFunc():
        print("=======================================WELCOME TO GOCAB=======================================\n\n1. Log In\n2. Sign up")
        x = int(input("Selection the Option: "))
        if(x==1):
                if(login()==True):
                      print("Login Successful\n\n")
                      booking()

                else:
                      print("User not Registered, Please SignUp\n\n")
        elif(x==2):
                signup()
        else:
            print("\n\nPlease select appropriate option\n\n")
            menuFunc()
                            
while(True):
        menuFunc()
