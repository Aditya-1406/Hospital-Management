import random
z = (random.randint(0,999))

print(""" 
                       ==============================
               ============================================
       ==========================================================
           ˜”*°•.˜”*°• WELCOME TO A*3 HOSPITAL •°*”˜.•°*”˜
        ==========================================================
""")             
print("""---May I Help You---
     
      1. About Doctors (Only For Staff)
      2. Timings
      3. Online Payments
      4. Emergency alarm
      5. Patient Registration
      6. To Check the Details of Patient(Only for staff)
      7. medicines counter 
      8. laboratory area
        """)

user1 = int(input("Enter the number respective to your inquiry: "))

if user1 == 1:
      user2= input("Enter The Id: ")
      Pass= int(input("Enter the Password: "))
      
      if user2 == "greengold007" and Pass == 123456:
      
            print("""
                      *****************************************************
                  Serial no. |  Doctor Name:-     | Qualification:-   |     Department:-       |     Contact No.(+91):-
                              
                  1.        |  Dr. Chudail        |       MS          |     Cardiologist       |     8574525610
                  2.        |  Dr. Aseem Goyal    |       MS          |     Orthopedics        |     6325748912
                  3.        |  Dr. Pardeep Sharma |       Ms          |     Pediatrician       |     2478936513
                  4.        |  Dr. Ajay Gupta     |       DNB         |     Gynaecologist      |     7402000004
                  5.        |  Dr. Gurpreet Bhatia|       BHMS        |     Naturopathy        |     7968554776
                  7.        |  Dr. Ranjit Sharma  |       MD          |     Dental Surgeon     |     7688574599
                  8.        |  Dr. Tejinder Aggarwal     MBBS         |    Gastroentrologist   |     7867589685
                  9.        |  Dr. Deepak Tyagi   |       MD          |     Neurologist        |     8967565870
                  10.       |  Dr. Sanya Sharma   |       MD          |     Physiologist       |     9786756350
                       *****************************************************
                  """)
      else:
            print("Incorrect Id or Password")
elif user1==2:
    print("""
             
          Timings of OPD : 9:00AM - 6:00PM
          Timings for Appointment of Doctor : 10:00AM - 4:00PM
          Timing of Pharamacy : 24/7
          Timing of Emergency : 24/7
            
          """)
elif user1==3:
      
      print("""IF YOU WANT TO PAY MONEY ONLINE THEN SELECT THE OPTION -->
            1. Via App
            2. Scan The Qr Code
            """)
      user3 = int(input("Select the Mode of Payment:- "))
      if user3 == 1:
            print("""   
            1. Download A*3 Hospital App from the Playstore or Appstore.
            2. Login with your creditals and patient Name.
            3. Go to payment section.
            4. Your Due payment will reflect there.
            5. Select the payment card and then click on pay.
            6. Pay with any app or UPI ID.""")
      elif user3==2:
            from PIL import Image
            myImage = Image.open("payment2.jpg")
            myImage.show()
      else:
            print("Not available")



elif user1==4:
      from playsound import playsound
      playsound("alert.wav")

elif user1==5:
      print("  ---For Patient Registration please fill The details---   ")
      
      
      from datetime import datetime
      a = datetime.now()
            
      b = "A*3 Hospital"

      name1 = input("Enter the Name of Patient: ")
      Add = input("Enter the address of Patient: ")
      city = input("Enter the city: ")
      state = input("Enter the state: ")
      Pin = int(input("Enter the pin code: "))
      Phn = int(input("Enter the phone Number: "))
      dob = input("Enter the DOB: ")
      Email = input("Enter the Email id: ")
      Sex = input("Enter the Sex: ")
      Age= int(input("Enter the age: "))
      Emer= input("Enter the Medical Problem: ")
      doc= input("Enter the Doctor Name (if you fill this form by self then leave it):- ")
      Sign = input("Enter the Name who fill the form: ")
      c =  (f"""
                              PATIENT REGISTRATION FORM
            Today's Date:{a}                                 {b} 
            ------------------------------------------------------------------------
            PATIENT INFORMATION:
            
            Name:- {name1}
            
            Address:- {Add}
            
            City:- {city}            State:- {state}       Pin Code:{Pin}
            
            Phone Number:- {Phn}       
            
            DOB:- {dob}
            
            E-mail id:- {Email}    Sex:- {Sex}       Age:- {Age}  
            
            Problem:{Emer}         Refer Doctor:{doc}
            
            Password for medicines and laboratory:{z}
            
                                                                 Sign:{Sign}
--------------------------------------------------------------------------
                              
            """)
      print(c)
      
      f = open(f'C:\\Users\\Aditya\\Desktop\\trials\\{name1}.txt','w')
      f.writelines(c)
      f.close
      
   
elif user1==6: 
            user5= input("Enter the ID:- ")
            Pass2 = int(input("Enter The Password: "))
            
            if user5 == "greengold007" and Pass2 == 123456:
                  print("TO CHECK THE DETAILS:-")     
                  user4= input("Enter the Name of Patient:- ")
                  f=open(f'C:\\Users\\Aditya\\Desktop\\trials\\{user4}.txt', 'r')
                  print(f.read(),end="")
                  f.close     


elif user1==7:
    
             
             print(" === Submit  medicines  password")  
             pass3 = int(input("enter given  medicine  password:-"))
             if pass3 in range(1000):
                 print(''' 
                 ===============
                 order confirmed
                 ===============
            please show the slip to the delivery counter 
                 
                 ''')  
             else:
                 print('''
      
      no order on this password
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



       **             **      
       check password and try again 
       **             ***
       ''')


elif user1==8:
            print('''
               =================================
                      laboratory area      
               =================================       
                      ''')
            print ('''Select your required test
            1.kidney function test.
            2.liver function test.
            3.lumbar puncture.
            4.malabsorption test.

            ''')

            user8 = int(input("Enter the number respective to your inquiry: "))
            z1 = int(input("Enter the Medicine and Laboratory Code: "))
            if user8 == 1 and z1 in range(1000):
                  print ('''
                  ========================================================================
                  booking sent  for the Kidney function test please check your mail for confirmaton 
                  ========================================================================
                  ''')
            if user8 == 2 and z1 in range(1000):
                  print ('''
                  ========================================================================
                  booking sent  for the Liver Function test please check your mail for confirmaton 
                  ========================================================================
                  ''')       
            if user8 == 3 and z1 in range(1000):
                  print ('''
                  ========================================================================
                  booking sent  for the Lumbar Puncture test please check your mail for confirmaton 
                  ========================================================================
                  ''')
            if user8 == 4 and z1 in range(1000):
                  print ('''
                  ========================================================================
                  booking sent  for the Malabsorption test please check your mail for confirmaton 
                  ========================================================================
                  ''')



  
else:
      print("Not Found")
