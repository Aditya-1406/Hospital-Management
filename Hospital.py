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
