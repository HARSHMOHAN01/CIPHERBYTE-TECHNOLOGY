# PROJECT : SIMPLE LIFE
# CREATED BY : HARSH MOHAN
# SCHOOL : CONVENT OF GAGAN BHARTI
# ADMISSION NUMBER : 7087
import time
import webbrowser
import random
print("                       WELCOME TO THE SIMPLE LIFE ")
print()
print()
print()
time.sleep(2)
print("                PURCHASE OR BOOK YOUR THINGS ON BEST RATES ")
print()
print()
print()
time.sleep(2)
print("           WITH THE WORLD'S BEST SALERS AND THEIR TRUSTWORTHY COMPANIES ")
print()
print()
print()
time.sleep(2)
print("         WITH THE AVABILITY OF YOUR MULTINATIONALS BRANDS AND SITES ")
print()
print()
print()
time.sleep(2)
print("                 WELCOME TO HARSH MOHAN'S SIMPLE LIFE PROGRAM ")
print()
print()
print()
A=str(input("""  ENTER "CONTINUE" : IF YOU WANT TO SHOP SOMETHING OR SEE SOMETHING \n
  ENTER STOP : IF YOU WANT TO NOT SEE THE PRODUCTS : """))
if A=="CONTINUE":
    B=str(input("ENTER YOUR NAME : "))
    C=str(input("ENTER YOUR EMAIL ID AS 'NAME@SIMPLELIFE.COM' "))
    D="USER NAME = "+B
    d="USER EMAIL ID = "+C
    E=open("LOGIN USER.txt","a")
    E.write(D+"\n")
    E.write("\n")
    E.write(d+"\n")
    E.write("\n")
    E.write("**********************************************"+"\n")
    E.close()
    D=str(input(""" PRESS A IF YOU WANT TO BOOK A AIRPLANE TICKET
 PRESS B IF YOU WANT TO BOOK A RAILWAY TICKET
 PRESS C IF YOU WANT TO DOWNLOAD A BOOK FROM OUR LIBRARY
 PRESS D IF YOU WANT TO ENTERTAIN YOURSELF : """))
    if D=="A":
        print("                        WELCOME TO HARSHGO  ")
        print("             WE ARE THE BEST AIRLIES BOOKING SECTION ")
        time.sleep(5)
        print("""
 **     **              **               ***********  *******  **    **  *********       *********
 **     **            **   **            **       **  *        **    **  *********       *********
 **     **          **       **          **       **  *        **    **  **              **     **
 *********        **************         ***********  *******  ********  **      ******  **     **
 *********      **               **      ****               *  ********  **      **  **  **     **
 **     **    **                   **    **  **             *  **    **  **********  **  *********
 **     **  **                       **  **    **     *******  **    **  *********   **  *********""")
        time.sleep(5)
        print("""
 |*******************************************************************************************************
 |SERIAL|DEPARTURE  |ARRIVAL                                 |FLIGHT NAME   | TOTAL TIME | PRICE/PERSON *
 | A.1  |DELHI(IGI) |CHHATRAPATI SHIVAJI AIRPORT (MUMBAI)    |INDIAN MOHANS | 180 MINUTE | 2,155(INR)   *
 | A.2  |DELHI(IGI) |PUNE AIRPORT (PUNE)                     |INDIAN MOHANS | 120 MINUTE | 2,247(INR)   *
 | B.1  |DELHI(IGI) |KEMPEGOWDA AIRPORT (BENGALURU)          |INDIAN MOHANS | 160 MINUTE | 3,610(INR)   *
 | B.2  |DELHI(IGI) |MYSORE AIRPORT (MYSORE)                 |INDIAN MOHANS | 300 MINUTE | 4,580(INR)   *
 | C.1  |DELHI(IGI) |CHENNAI AIRPORT (CHENNAI)               |INDIAN MOHANS | 150 MINUTE | 2,258(INR)   *
 | C.2  |DELHI(IGI) |COIMBATORE AIRPORT (COIMBATORE)         |INDIAN MOHANS | 180 MINUTE | 4,076(INR)   *
 | D.1  |DELHI(IGI) |VALLABHBHAI PATEL AIRPORT (AHMEDABAD)   |INDIAN MOHANS | 100 MINUTE | 1,776(INR)   *
 | D.2  |DELHI(IGI) |VADODARA AIRPORT (VADODARA)             |INDIAN MOHANS | 100 MINUTE | 3,542(INR)   *
 | E.1  |DELHI(IGI) |COCHIN AIRPORT (KOCHI)                  |INDIAN MOHANS | 170 MINUTE | 4,823(INR)   *
 | E.2  |DELHI(IGI) |TRIVANDRUM AIRPORT (KANYAKUMARI)        |INDIAN MOHANS | 200 MINUTE | 3,341(INR)   *
 | F.1  |DELHI(IGI) |BHUBANESHWAR AIRPORT (BHUBANESHWAR)     |INDIAN MOHANS | 125 MINUTE | 1,801(INR)   *
 | F.2  |DELHI(IGI) |JHARSUGUDA AIRPORT (DURALAGA)           |INDIAN MOHANS | 115 MINUTE | 2,051(INR)   *
 | G.1  |DELHI(IGI) |SHEIKH-UL-ALAM AIRPORT (SRINAGAR)       |INDIAN MOHANS |  75 MINUTE | 3,838(INR)   *
 | G.2  |DELHI(IGI) |JAMMU AIRPORT (JAMMU)                   |INDIAN MOHANS |  75 MINUTE | 2,388(INR)   *
 | H.1  |DELHI(IGI) |RAJA BHOJ AIRPORT (BHOPAL)              |INDIAN MOHANS |  85 MINUTE | 2,300(INR)   *
 | H.2  |DELHI(IGI) |KHAJURAHO AIRPORT (CHHATTARPUR)         |INDIAN MOHANS |  80 MINUTE | 1,500(INR)   *
 | I.1  |DELHI(IGI) |BIRSA MUNDA AIRPORT (RANCHI)            |INDIAN MOHANS | 100 MINUTE | 1,320(INR)   *
 | I.2  |DELHI(IGI) |DHANBAD AIRPORT (DHANBAD)               |INDIAN MOHANS |  96 MINUTE | 7,149(INR)   *
 | J.1  |DELHI(IGI) |SHIMLA AIRPORT (SHIMLA)                 |INDIAN MOHANS |  70 MINUTE | 2,576(INR)   *
 | J.2  |DELHI(IGI) |KULLU-MANALI AIRPORT (BUNTAR)           |INDIAN MOHANS |  80 MINUTE | 4,926(INR)   *
 | K.1  |DELHI(IGI) |DAMAN AND DIU AIRPORT (DAMAN DIU)       |INDIAN MOHANS | 305 MINUTE | 3,433(INR)   *
 | L.1  |DELHI(IGI) |SWAMI VIVEKANAND AIRPORT (RAIPUR)       |INDIAN MOHANS | 100 MINUTE | 2,975(INR)   *
 | L.2  |DELHI(IGI) |JAGDAL AIRPORT (JAGDAL)                 |INDIAN MOHANS | 510 MINUTE | 4,056(INR)   *
 | M.1  |DELHI(IGI) |TEZU AIRPORT (TEZU)                     |INDIAN MOHANS | 175 MINUTE | 4,000(INR)   *
 | M.2  |DELHI(IGI) |DAPORIZO AIRPORT (DAPORIZO)             |INDIAN MOHANS | 175 MINUTE | 3,433(INR)   *
 | N.1  |DELHI(IGI) |VISHAKHAPATNAM AIRPORT (VISHAKHAPATNAM) |INDIAN MOHANS | 155 MINUTE | 2,975(INR)   *
 | N.2  |DELHI(IGI) |VIJAYADA AIRPORT (VIJAYADA)             |INDIAN MOHANS | 150 MINUTE | 4,191(INR)   *
 | N.3  |DELHI(IGI) |CUDDAPAH AIRPORT (KADAPA)               |INDIAN MOHANS |  75 MINUTE | 5,300(INR)   *
 | O.1  |DELHI(IGI) |CHANDIGARH AIRPORT (CHANDIGARH)         |INDIAN MOHANS |  55 MINUTE | 1,830(INR)   *
 | P.1  |DELHI(IGI) |VARANASI AIRPORT (VARANASI)             |INDIAN MOHANS |  80 MINUTE | 1,507(INR)   *
 | Q.1  |DELHI(IGI) |GAYA AIRPORT (GAYA)                     |INDIAN MOHANS | 115 MINUTE | 3,435(INR)   *
 | Q.2  |DELHI(IGI) |PATNA AIRPORT (PATNA)                   |INDIAN MOHANS | 150 MINUTE | 2,190(INR)   *""")
        E=str(input("ENTER YOUR SERIAL NUMBER TO BOOK YOUR TICKET : "))
        if E=="A.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO CHHATRAPATI SHIVAJI AIRPORT (MUMBAI)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS A.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2155
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="A.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO PUNE AIRPORT (PUNE)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS A.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2247
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="B.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO KEMPEGOWDA AIRPORT (BENGALURU)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS B.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3610
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="B.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO MYSORE AIRPORT (MYSORE)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS B.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4580
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="C.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO CHENNAI AIRPORT (CHENNAI)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS C.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2258
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="C.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO COIMBATORE AIRPORT (COIMBATORE)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS C.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4076
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="D.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO SARDAR VALLABHBHAI PATEL AIRPORT (AHEMDABAD)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS D.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1776
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="D.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO VADODRA AIRPORT (VADODRA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS D.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3542
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="E.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO COCHI AIRPORT (KOCHI)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS E.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4823
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="E.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO TRIVANDRUM AIRPORT (KANYAKUMARI)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS E.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3341
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="F.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO BHUBANESHWAR AIRPORT (BHUBANESHWAR)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS F.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1081
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="F.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO JHARSUGUDA AIRPORT (DURALAGA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS F.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2051
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="G.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO SEIKH-UL-ALAM AIRPORT (SRINAGAR)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS G.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3838
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="G.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO JAMMU AIRPORT (JAMMU)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS G.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2388
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="H.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO RAJA BHOJ AIRPORT (BHOPAL)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS H.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="H.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO KHAJURAHO AIRPORT (CHHATTRAPUR)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS H.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="I.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO BIRSA MUNDA AIRPORT (RANCHI)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS I.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1320
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="I.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO DHANBAD AIRPORT (DHANBAD)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS I.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*7149
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="J.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO SHIMLA AIRPORT (SHIMLA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS J.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2576
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="J.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO KULLU AND MANALI AIRPORT (BUNTAR)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS J.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4926
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="K.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO DAMAN AND DIU AIRPORT (DAMAN AND DIU)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS K.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3433
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="L.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO SWAMI VIVEKANAND AIRPORT (RAIPUR)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS L.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2975
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="L.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO JAGDAL AIRPORT (JAGDALPUR)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS L.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4056
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="M.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO TEZU AIRPORT (TEZU)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS M.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="M.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO DAPORIZO AIRPORT (DAPORIZO)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS M.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3433
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="N.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO VISHAKHAPATNAM AIRPORT (VISHAKHAPATNAM)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS N.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2975
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="N.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO VIJAYWADA AIRPORT (VIJAYWADA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS N.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4191
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="N.3":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO CUDDAPAH AIRPORT (KADAPA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS N.3"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*5300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="O.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO CHANDIGARH AIRPORT (CHANDIGARH)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS O.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1830
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="P.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO VARANASI AIRPORT (VARANASI)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS P.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1507
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="Q.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO GAYA AIRPORT (GAYA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS Q.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3435
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif E=="Q.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST CLASS/BUSINESS CLASS/ECONOMY CLAS' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("FLIGHT TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM DELHI IGI AIRPORT AND ARRIVAL TO PATNA AIRPORT (PATNA)"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("FLIGHT NAME INDIAN MOHANS AIRWAYS Q.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2190
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
    elif D=="B":
        print("                           WELCOME TO THE HARSH RAILS SECTION")
        print("             WE PROVIDES YOU THE FASTEST TRAINS IN INDIA WITH BEST FACILITIES")
        time.sleep(5)
        print("""
**    **  ****       ****       **********             **                ****************  **          ************** 
**    **  **  **   **  **       **      **           **  **              ****************  **          ****
**    **  **    **     **       **      **         **      **                   **         **          ****
********  **           **       **********       **          **                 **         **          **************
********  **           **       ** **          ******************               **         **                    ****
**    **  **           **       **  **       **********************             **         **                    ****
**    **  **           **       **   **    **                      **    ****************  **********  **************
**    **  **           **       **    ** **                          **  ****************  **********  **************""")
        time.sleep(5)
        print("""
*******************************************************************************************************************
SERIAL      |ARRIVAL          |DEPARTURE                        |TRAIN NAME           |TOTAL TIME    |PRICE/PERSON*
 A.1        |NDLS             |SRINAGAR(JAMMU AND KASHMIR)      | MOHAN RAILS A.1     |1,077 MINUTES |4,800(INR)  *
 B.1        |NDLS             |LEH(LADAKH)                      | MOHAN RAILS B.1     |1,200 MINUTES |4,620(INR)  *
 C.1        |NDLS             |SHIMLA(UTTRAKHAND)               | MOHAN RAILS C.1     | 580  MINUTES |1,205(INR)  *
 D.1        |NDLS             |CHANDIGARH(PUNJAB)               | MOHAN RAILS D.1     | 180  MINUTES |1,190(INR)  *
 E.1        |NDLS             |ROHTAK(HARYANA)                  | MOHAN RAILS E.1     | 105  MINUTES |210(INR)    *
 F.1        |NDLS             |JAIPUR(RAJASTHAN)                | MOHAN RAILS F.1     | 295  MINUTES |193(INR)    *
 G.1        |NDLS             |LUCKNOW(UTTAR PRADESH)           | MOHAN RAILS G.1     | 480  MINUTES |1,085(INR)  *
 H.1        |NDLS             |PATNA(BIHAR)                     | MOHAN RAILS H.1     |1,205 MINUTES |3,700(INR)  *
 I.1        |NDLS             |RANCHI(JHARKHAND)                | MOHAN RAILS I.1     |1,164 MINUTES |4,000(INR)  *
 J.1        |NDLS             |KOLKATA(WEST BENGAL)             | MOHAN RAILS J.1     |1,560 MINUTES |2,300(INR)  *
 J.2        |NDLS             |DARJEELING(WEST BENGAL)          | MOHAN RAILS J.2     |2,040 MINUTES |2,900(INR)  *
 K.1        |NDLS             |GANGTOK(SIKKIM)                  | MOHAN RAILS K.1     |2,203 MINUTES |3,300(INR)  *
 L.1        |NDLS             |DISPUR(ASSAM)                    | MOHAN RAILS L.1     |1,841 MINUTES |3,900(INR)  *
 M.1        |NDLS             |ITANAGAR(ARUNACHAL PRADESH)      | MOHAN RAILS M.1     |2,275 MINUTES |2,105(INR)  *
 N.1        |NDLS             |DIMAPUR(NAGALAND)                | MOHAN RAILS N.1     |1,941 MINUTES |5,205(INR)  *
 O.1        |NDLS             |IMPHAL(MANIPUR)                  | MOHAN RAILS O.1     |2,400 MINUTES |5,300(INR)  *
 P.1        |NDLS             |AIZAWL(MIZORAM)                  | MOHAN RAILS P.1     |1,035 MINUTES |7,000(INR)  *
 Q.1        |NDLS             |AGARTALA(TRIPURA)                | MOHAN RAILS Q.1     |2,941 MINUTES |7,200(INR)  *
 R.1        |NDLS             |BHOPAL(MADHYA PRADESH)           | MOHAN RAILS R.1     | 487  MINUTES |4,100(INR)  *
 S.1        |NDLS             |RAIPUR(CHHATTISGARH)             | MOHAN RAILS S.1     |1,377 MINUTES |2,129(INR)  *
 T.1        |NDLS             |BHUBANESHWAR(ODISHA)             | MOHAN RAILS T.1     |1,680 MINUTES |5,640(INR)  *
 U.1        |NDLS             |MUMBAI(MAHARASHTRA)              | MOHAN RAILS U.1     |3,600 MINUTES |4,730(INR)  *
 V.1        |NDLS             |PANAJI(GOA)                      | MOHAN RAILS V.1     |1,680 MINUTES |4,915(INR)  *
 W.1        |NDLS             |BENGALURU(KARNATAKA)             | MOHAN RAILS W.1     |2,400 MINUTES |5,815(INR)  *
 X.1        |NDLS             |TRIVUNATHAPURAM(KERELA)          | MOHAN RAILS X.1     |2,705 MINUTES |7,418(INR)  *
 Y.1        |NDLS             |CHENNAI(TAMIL NADU)              | MOHAN RAILS Y.1     |2,100 MINUTES |5,285(INR)  *""")
        D=str(input("ENTER THE SERIAL NUMBER OF WHERE YOU WANT TO BOOK YOUR TRIAN TICKET : "))
        if D=="A.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO SRINAGAR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS A.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4800
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="B.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO LEH RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS B.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4620
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="C.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO SHIMLA RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS C.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1205
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="D.3":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO CHANDIGARH RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS D.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1190
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="E.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO ROHTAK RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS E.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*210
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="F.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO JAIPUR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS F.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*193
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="G.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO LUCKNOW RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS G.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*1085
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="H.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO PATNA RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS H.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3700
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="I.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO RANCHI RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS I.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="J.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO KOLKATA RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS J.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="J.2":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO DARJELLING RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS J.2"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2900
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="K.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO GANGTOK RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS K.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="L.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO DISPUR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS L.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*3900
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="M.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO ITANAGAR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS M.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2105
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="N.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO DIMAPUR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS N.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*5205
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="O.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO IMPHAL RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS O.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*5300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="P.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO AIZAWAL RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS P.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*7000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="Q.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO AGARTALA RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS Q.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*7200
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="R.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO BHOPAL RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS R.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4100
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="S.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO RAIPUR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS S.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*2129
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="T.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO BHUBANESHWAR RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS T.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*5640
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="U.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO MUMBAI RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS U.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4730
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="V.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO PANAJI RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS V.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*4915
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="W.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO BENGALURU RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS W.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*5815
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="X.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO TIRVUNATHAPURAM RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS X.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*7418
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="Y.1":
            F=str(input("ENTER THE TOTAL NUMBER OF PERSON : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF DEPARTURE : "))
            K=str(input("""ENTER THE TYPE OF SEAT YOU WANT
'FIRST TIER/SECOND TIER/THIRD TIER' : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    print("SEE  ON YOUR DESKTOP THE TICKET IS UPLOADED THERE ")
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
            Z=open("TRAIN TICKET.txt","a")
            f="NUMBER OF PERSON = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="PASSENGER NAME = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PASSENGER = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF DEPARTURE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF ARRIVAL = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("DEPARTURE FROM NEW DELHI RAILWAY STATION AND ARRIVAL TO CHENNAI RAILWAY STATION"+"\n")
            l="TYPE OS SEAT = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("TRAIN NAME -> MOHAN RAILS Y.1"+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=int(F)*5285
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="PASSENGER'S MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("******************************************************************************"+"\n")
            Z.close()
    elif D=="C":
        print("                   WELCOME TO THE INDIAN MOHANS LIBRARY SECTION")
        print("               WE CONTAIN THE USEFUL BOOKS AT VERY REASONABLE PRICE")
        time.sleep(3)
        print("""
**********   ***     ***      **********   ************   ************   **   **   ********
   **        ** *   * **      **      **   ************   ************   **  **    **
   **        **  * *  **      **      **   **        **   **        **   ** **     **
   **        **   *   **      **********   **        **   **        **   ****      **
   **        **       **      **********   **        **   **        **   ****      ********
   **        **       **      **      **   **        **   **        **   ** **           **
   **        **       **      **      **   ************   ************   **  **          **
**********   **       **      **********   ************   ************   **   **   ********""")
        time.sleep(5)
        print("""
*******************************************************************************************************************
SERIAL |BOOK NAME                              |LEVEL    |RATINGS     |PUBLISHER         |TYPE OF BOOK |PRICE     *
 A.1   |ARIHANT CHEMISTRY                      |IIT-JEE  |*****/***** |ARIHANT PRAKASHAN |SOFTCOPY     |3,000(INR)*
 B.1   |ARIHANT MATHEMATICS                    |IIT-JEE  |*****/***** |ARIHANT PRAKASHAN |SOFTCOPY     |2,500(INR)*
 C.1   |ARIHANT PHYSICS                        |IIT-JEE  |*****/***** |ARIHANT PRAKASHAN |SOFTCOPY     |4,000(INR)*
 D.1   |DISHA CHEMISTRY                        |IIT-JEE  |*****/***** |DISHA             |SOFTCOPY     |1,300(INR)*
 E.1   |DISHA MATHEMATICS                      |IIT-JEE  |*****/***** |DISHA             |SOFTCOPY     |1,400(INR)*
 F.1   |DISHA PHYSICS                          |IIT-JEE  |*****/***** |DISHA             |SOFTCOPY     |1,500(INR)*
 G.1   |D MUKHERJI(MCQ)                        |IIT-JEE  |*****/***** |D MUKHERJI        |SOFTCOPY     |5,000(INR)*
 H.1   |ELECTRICITY AND MAGNETISM (DC PANDEY)  |IIT-JEE  |*****/***** |DC PANDEY         |SOFTCOPY     |3,000(INR)*
 I.1   |H C VERMA (VOLUME 1)                   |IIT-JEE  |*****/***** |HC VERMA          |SOFTCOPY     |800(INR)  *
 J.1   |MECHANISM VOLUME 1(DC PANDEY)          |IIT-JEE  |*****/***** |DC PANDEY         |SOFTCOPY     |1,600(INR)*
 K.1   |MECHANISM VOLUME 2(DC PANDEY)          |IIT-JEE  |*****/***** |DC PANDEY         |SOFTCOPY     |1,500(INR)*
 L.1   |OPTICS AND MORDERN PHYSICS (DC PANDEY) |IIT-JEE  |*****/***** |DC PANDEY         |SOFTCOPY     |2,000(INR)*
 M.1   |PYTHON NCERT                           |CBSE     |*****/***** |N.C.E.R.T         |SOFTCOPY     |560(INR)  *
 N.1   |PHYSICAL EDUCATION                     |CBSE     |***/*****   |SARASVATI         |SOFTCOPY     |1,000(INR)*
 O.1   |SAMEER BANSAL CLACULUS                 |IIT-JEE  |*****/***** |SAMEER BANSAL     |SOFTCOPY     |860(INR)  *
 P.1   |WAVES AND THERMODYNAMICS (DC PANDEY)   |IIT-JEE  |*****/***** |DC PANDEY         |SOFTCOPY     |2,500(INR)*""")
        D=str(input("ENTER YOUR SERIAL NUMBER TO CHOOSE WHICH BOOK YOU WANT : "))
        if D=="A.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1yvIEOyG2WNAUpBD8jvRxum1F8ZEepppu/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING ARIHANT CHEMISTRY SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=3000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="B.2":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1a1lnUeDjvIN2hYWmU0khdYDSAbMXS8zD/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING ARIHANT MATHEMATICS SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=2500
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="C.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/11pm33sgguV58enm2rNeRbVD3XtSO3YYu/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING ARIHANT PHYSICS SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=4000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="D.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1AETdm8yatoTmEB6x5ygAeEAkJWfRe8Qr/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING DISHA CHEMISTRY SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=1300
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="E.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1pjiOat3vtqp4wIl3K7Fhqp-7eHxLG-1j/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING DISHA MATHEMATICS SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=1400
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="F.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1ughR2Tk-iX5Nfe1QS1zAOAdgSABurx1l/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING DISHA PHYSICS SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=1500
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="G.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1hIPdjxcxZTkgSBzXSJ07j5u3KggjTgAB/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING D. MUKHERJI SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=5000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="H.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1ycr0MPy_e8ztm9r5TgBnJM1RVZOfnguO/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING ELECTRICITY AND MAGNETISM (DC PANDEY) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=3000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="I.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1fUTctf9zTqthOf5imtXw7aXeH1oly_eA/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING HC VERMA(VOLUME 1) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=800
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="J.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1fxy8n2rQH9FHR52iU_yW-Dw7xiET7Z3N/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING MECHANSIM DC PANDEY(VOLUME 1) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=1600
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="K.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/10-pLDQnZYdgp1yzi7KTm12sDvUOsO2-d/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING MECHANSIM DC PANDEY(VOLUME 2) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=1500
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="L.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1UgtApCkDFLXfRUv8xuxdgq799Iwg7Xk3/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING OPTICS AND MORDEN PHYSICS(DC PANDEY) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=2000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="M.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1GmOAX42UqEXUyYDNgnsujG5kq3q-brN3/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING PYTHON(NCERT) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=560
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="N.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1QRY4BE5nWsGuKWazZaTn0UM35vU4hsVW/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING PHYSICAL EDUCATION(SARASVVATI) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=1000
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="O.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1qRs7IKr3WOn9I6M7S1kRVl1ceBKmYsJx/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING SAMEER BANSAL CALCULUS SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=860
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.close()
        elif D=="P.1":
            F=str(input("ENTER YOUR EMAIL ID : "))
            G=str(input("ENTER THE NAME OF THE PERSON : "))
            H=str(input("ENTER THE AGE OF THE PERSON : "))
            I=str(input("ENTER THE GENDER OF THE PERSON : "))
            J=str(input("ENTER THE DATE OF PURCHASE : "))
            K=str(input("""ENTER YOUR RESIDENTIAL ADDRESS : """))
            time.sleep(5)
            print()
            print()
            print("      PLEASE MAKE THE PAYMENT")
            print("      WE ACCEPTS PAYMENTS FROM ALL BANKS SO NO WORRIES ")
            print("      PLEASE WAIT FOR YOUR SYSTEM GENERATED PASSWORD")
            b=0
            while b==0:
                D=random.randint(0,100000)
                print("      YOUR SYSTEM GENERATED PASSWORD IS : ",D)
                c=int(input("ENTER THE SYSTEM GENERATED PASSWORD : "))
                if c==D:
                    print("OK NOW YOU CAN MOVE ON ")
                    b=1
                else:
                    print("YOUR SYSTEM GENERATED PASSWORD IS WRONG PLEASE TRY AGAIN")
                    b=0
            L=str(input("ENTER THE COMPLETE NAME OF YOUR BANK : "))
            b=0
            while b==0:
                M=int(input("ENTER YOUR SIX DIGIT BANK ACCOUNT NUMBER : "))
                if M in range(0,10000000):
                    print("BANK ACCOUNT NUMBER ",M," ACCEPTED")
                    b=1
                else:
                    print("YOUR BANK ACCOUNT NUMBER IS WRONG PLEASE TRY AGAIN")
                    b=0
            b=0
            while b==0:
                N=int(input("ENTER YOUR MOBILE NUMBER : "))
                if len(str(N))==10:
                    print("YOU WILL BE REDIRECTED TO YOUR DEFAULT BROWSER TO DOWNLOAD THE BOOK")
                    print("PLEASE ENSURE THAT YOU ARE CONNECTED WITH CONTINUOUS INTERNET")
                    time.sleep(3)
                    print("PLEASE WAIT WE ARE PROCESSING ......")
                    time.sleep(3)
                    print("SEE  ON YOUR DESKTOP THE RECEIPT IS UPLOADED THERE ")
                    time.sleep(3)
                    print("THANKS FOR CHOOSING US HOPE YOU WILL VISIT AGAIN")
                    print("PLEASE WAIT FOR FIVE SECONDS")
                    time.sleep(5)
                    webbrowser.open_new("https://drive.google.com/file/d/1z_aSPBF9witu9xjJcdoocIdhVxeu22qf/view?usp=sharing")
                    b=1
                else:
                    print("YOU HAVE ENTER ANY WRONG NUMBER PLEASE ENTER AGAIN")
                    b=0
            Z=open("BOOK PURCHASE RECEIPT.txt","a")
            f="YOUR EMAIL ID = "+F
            Z.write(f+"\n")
            Z.write("\n")
            g="NAME OF THE BUYER = "+G
            Z.write(g+"\n")
            Z.write("\n")
            h="AGE OF THE PERSON = "+H
            Z.write(h+"\n")
            Z.write("\n")
            i="GENDER OF THE PERSON = "+I
            Z.write(i+"\n")
            Z.write("\n")
            j="DATE OF PURCHASE = "+J
            Z.write(j+"\n")
            Z.write("\n")
            k="DATE OF HANDOVER OF BOOK = "+J
            Z.write(k+"\n")
            Z.write("\n")
            Z.write("THANKS FOR PURCHASING WAVES AND THERMODYNAMICS(DC PANDEY) SOFTCOPY BOOK"+"\n")
            l="YOUR RESENDITIAL ADDRESS = "+K
            Z.write("\n")
            Z.write(l+"\n")
            Z.write("COMPANY NAME -> INDIAN MOHAN LIBRARY "+"\n")
            Z.write("\n")
            Z.write("\n")
            m="PAYMENT FROM BANK = "+L
            Z.write(m+"\n")
            Z.write("\n")
            n="THE ACCEPTED BANK ACCOUNT NUMBER = "+str(M)
            Z.write(n+"\n")
            Z.write("\n")
            cost=2500
            P="TOTAL COST = "+str(cost)+"(INR)"
            Z.write(P+"\n")
            Z.write("\n")
            o="BUYER MOBILE NUMBER = "+str(N)
            Z.write(o+"\n")
            Z.write("\n")
            Z.write("""-->IF CHANGE ANY PAGE OF THIS BOOK
-->YOU WILL SURELY DISTROY THE COPYRIGHT TERMS
-->AND CONDITION OF THIS BOOK.
-->AND YOU WILL BE NO LONGER A PART OF
-->OUR COMPANY'S INDIAN MOHANS LIBRARY
-->LICENCE AND TERMS AND CONDITION ACCEPTOR""")
            Z.write("******************************************************************************"+"\n")
            Z.write("\n")
            Z.close()
    elif D=="D":
        print("                  WELCOME TO INDIAN MOHANS FREE SECTION")
        print("           ENTERTAIN YOURSELF WITH THE FREE OF COST ACTIVITES")
        print("""
 PRESS A : IF YOU WANT TO LISTEN SONGS
 PRESS B : IF YOU WANT TO WATCH MOVIES""")
        D=str(input("ENTER WHAT YOU WANT TO DO A OR B : "))
        if D=="A":
            print(''' PLEASE CHOOSE WHAT YOU WANT TO LISTEN :
 A=PATROTIC SONG
 B=PATROTIC MASH UP 
 C=BOLLYWOOD MASH UP''')
            A=input("ENTER YOUR CHOICE = A/B/C : ")
            C=0
            while C==0:
                if A=="A":
                    print("WELCOME TO THE PATROTIC MUSIC ZONE ")
                    print(""" PLEASE SELECT YOUR SONG FROM THE LIST BELOW :
 A=VANDE MATARAM           * F=JIGRA
 B=TERI MITTI              * G=AE WATAN
 C=CHALLA MEIN LAD JANNA   * H=JAGGA JITEYA
 D=VIJAYI BHAVA            * I=SAUNGDH MUJHE IS MITTI KI
 E=MEIN RAHOON YA NA       * J=MAA TUJHE SALAAM""")
                    Z=input("ENTER YOUR CHOICE WHAT YOU WANT TO LISTEN : ")
                    B=open("SONG HISTORY.txt","w")
                    if Z=="A":
                        webbrowser.open_new("https://www.youtube.com/watch?v=FDi1YVkvqt8")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF VANDE MATARAM")
                        B.close()
                    elif Z=="B":
                        webbrowser.open_new("https://www.youtube.com/watch?v=MsPAaH7Pq8Y")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF TERI MITTI")
                        B.close()
                    elif Z=="C":
                        webbrowser.open_new("https://www.youtube.com/watch?v=PVpwiG9Tazo")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF CHALLA MEIN LAD JANNA")
                        B.close()
                    elif Z=="D":
                        webbrowser.open_new("https://www.youtube.com/watch?v=cithtm4I3IQ")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF VIJAYI BHAVA")
                        B.close()
                    elif Z=="E":
                        webbrowser.open_new("https://www.youtube.com/watch?v=iL96f_xtHxI")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF MEIN RAHOON YA NA RAHOON")
                        B.close()
                    elif Z=="F":
                        webbrowser.open_new("https://www.youtube.com/watch?v=UBRsoxJXoJI")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF JIGRA")
                        B.close()
                    elif Z=="G":
                        webbrowser.open_new("https://www.youtube.com/watch?v=M9YiT9oGLF4")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF AE WATAN")
                        B.close()
                    elif Z=="H":
                        webbrowser.open_new("https://www.youtube.com/watch?v=Re9mbvZ_mCM")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF JAGGA JITEYA")
                        B.close()
                    elif Z=="I":
                        webbrowser.open_new("https://www.youtube.com/watch?v=QaG-8fJ-e5k")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF SAUNGDH MIJHE IS MITTI KI")
                        B.close()
                    elif Z=="J":
                        webbrowser.open_new("https://www.youtube.com/watch?v=akPuNNzsR70")
                        C=1
                        B.write("YOU HAVE LISTENED A SONG OF MAA TUJHE SALLAM")
                        B.close()
                    else:
                        print("BY MISTAKELY YOU HAVE TYPED",Z,"INSTEAD OF OPTIONS GIVEN TO YOU")
                        C=0
                elif A=="B":
                    print("WELCOME TO THE PATROTIC MASHUP ZONE ")
                    print(""" PLEASE SELECT THE MASHUP FROM BELOW PLAYLIST :
 A=PATROTIC MASHUP 2020                      * D=PATROTIC MASHUP INDEPENDENCE DAY SPECIAL
 B=PATROTIC MASHUP 2021                      * E=PATROTIC MASHUP REPUBLIC DAY SPECIAL
 C=PATROTIC MASHUP BY JOSH JUKEBOX           * F=PATROTIC MASHUP ANDROID MUSIC MIX""")
                    Z=input("WHAT YOU WANT TO LISTEN : ")
                    if Z=="A":
                        webbrowser.open_new("https://www.youtube.com/watch?v=bc1FIpQbEog")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PATROTIC MASH UP 2020")
                        B.close()
                    elif Z=="B":
                        webbrowser.open_new("https://www.youtube.com/watch?v=e4CpDzYKuGY")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PATROTIC MASHUP 2021")
                        B.close()
                    elif Z=="C":
                        webbrowser.open_new("https://www.youtube.com/watch?v=qS5zNqzQtsQ")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PATROTIC MASH UP BY JOSH JUKEBOX")
                        B.close()
                    elif Z=="D":
                        webbrowser.open_new("https://www.youtube.com/watch?v=wAAYQzWpET0")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PATROTIC MASHUP IDEPENDENCE DAY SPECIAL")
                        B.close()
                    elif Z=="E":
                        webbrowser.open_new("https://www.youtube.com/watch?v=nvkhnMvgq60")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PATROTIC MASHUP REPUBLIC DAY")
                        B.close()
                    elif Z=="F":
                        webbrowser.open_new("https://www.youtube.com/watch?v=xNEd_PnNT-o")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PATROTIC MASHUPVANDROID MUSIC MIX")
                        B.close()
                    else:
                        print("BY MISTAKELY YOU HAVE TYPED",Z,"INSTEAD OF OPTIONS GIVEN TO YOU")
                        C=0
                elif A=="C":
                    print("WELCOME TO THE BOLLYWOOD MASHUP ZONE ")
                    print(""" PLEASE SELECT YOUR SONG FROM BELOW LIST :
 A=YO YO HONEY SINGH REMIX            * C=HOLLYWOOD AND BOLLYWOOD MIX 
 B=PARTY MASHUP BY KEDROCK            * D=DJ CHETAS MASHUP""")
                    Z=input("ENTER THE OPTIONS WHAT YOU WANT TO LISTEN A/B/C/D : ")
                    if Z=="A":
                        webbrowser.open_new("https://www.youtube.com/watch?v=NEPmlbjsfXo")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF YO YO HONEY SINGH")
                        B.close()
                    elif Z=="B":
                        webbrowser.open_new("https://www.youtube.com/watch?v=PcHkJNvkE6M")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF PARTY MASHUP BY KEDROCK")
                        B.close()
                    elif Z=="C":
                        webbrowser.open_new("https://www.youtube.com/watch?v=yJ-1_mWNpqs")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF HOLLYWOOD AND BOLLYWOOD MIX")
                        B.close()
                    elif Z=="D":
                        webbrowser.open_new("https://www.youtube.com/watch?v=nagt7yu-Hw4")
                        C=1
                        B.write("YOU HAVE LISTENED A MASH UP OF DJ CHETAS MASHUP")
                        B.close()
                    else:
                        print("BY MISTAKELY YOU HAVE TYPED",Z,"INSTEAD OF OPTIONS GIVEN TO YOU")
                        C=0
                else:
                    print("YOU HAVE TYPED ANY WRONG LETTER INSTEAD OF GIVEN IN THE OPTIONS ")
                    C=0
        elif D=="B":
            print(''' PLEASE CHOOSE WHICH YOU WANT TO WATCH :
 A=SHORT HORROR MOVIE
 B=ACTION MOVIE 
 C=COMEDY''')
            A=input("ENTER YOUR CHOICE = A/B/C : ")
            C=0
            while C==0:
                if A=="A":
                    print("WELCOME TO THE SHORT HORROR MOVIE ")
                    print(""" PLEASE SELECT YOUR MOVIE FROM THE LIST BELOW :
 A=DEAD PAINTER            * F=MAKE ME A SANDWICH
 B=THE BALLERINA           * G=POLARIOD
 C=I HEARD IT TO           * H=LIGHTS OUT
 D=DON'T LOOK AWAY         * I=CLOSET SPACE
 E=DON'T LOOK              * J=PICTURES """)
                    Z=input("ENTER YOUR CHOICE WHAT YOU WANT TO LISTEN : ")
                    B=open("MOVIE HISTORY.txt","w")
                    if Z=="A":
                        webbrowser.open_new("https://www.youtube.com/watch?v=wpUIoYtW6Jw")
                        C=1
                        B.write("YOU HAVE WATCHED DEAD PAINTER")
                        B.close()
                    elif Z=="B":
                        webbrowser.open_new("https://www.youtube.com/watch?v=sTtmpFIaFqc")
                        C=1
                        B.write("YOU HAVE WATCHED THE BALLERINA")
                        B.close()
                    elif Z=="C":
                        webbrowser.open_new("https://www.youtube.com/watch?v=OxRIWBoluzs")
                        C=1
                        B.write("YOU HAVE WATCHED I HEARED IT TO")
                        B.close()
                    elif Z=="D":
                        webbrowser.open_new("https://www.youtube.com/watch?v=4f3hG-5grlw")
                        C=1
                        B.write("YOU HAVE WATCHED DON'T LOOK AWAY")
                        B.close()
                    elif Z=="E":
                        webbrowser.open_new("https://www.youtube.com/watch?v=PBPn-9P0KRk")
                        C=1
                        B.write("YOU HAVE WATCHED DON'T LOOK")
                        B.close()
                    elif Z=="F":
                        webbrowser.open_new("https://www.youtube.com/watch?v=pfGEdmZyVyY")
                        c=1
                        B.write("YOU HAVE WATCHED MAKE ME A SANDWICH")
                        B.close()
                    elif Z=="G":
                        webbrowser.open_new("https://www.youtube.com/watch?v=ck1NO9MyQsM")
                        C=1
                        B.write("YOU HAVE WATCHED POLARIDO")
                        B.close()
                    elif Z=="H":
                        webbrowser.open_new("https://www.youtube.com/watch?v=TcOOYq9W6xk")
                        C=1
                        B.write("YOU HAVE WATCHED LIGHTS OUT")
                        B.close()
                    elif Z=="I":
                        webbrowser.open_new("https://www.youtube.com/watch?v=5fje6_ou5RY")
                        C=1
                        B.write("YOU HAVE WATCHED CLOSET SPACE")
                        B.close()
                    elif Z=="J":
                        webbrowser.open_new("https://www.youtube.com/watch?v=sfQrDGu3OkQ")
                        C=1
                        B.write("YOU HAVE WATCHED PICTURES")
                        B.close()
                    else:
                        print("BY MISTAKELY YOU HAVE TYPED",Z,"INSTEAD OF OPTIONS GIVEN TO YOU")
                        C=0
                elif A=="B":
                    print("WELCOME TO THE ACTION MOVIE ZONE ZONE ")
                    print(""" PLEASE SELECT THE MOVIE FROM BELOW PLAYLIST :
 A=commando 3                                * D=ABCD
 B=HEROPANTI                                 * E=BAHUBALI THE BEGINNING
 C=BAAGHI                                    * F=BABHUBALI THE CONCLUSION """)
                    Z=input("WHAT YOU WANT TO LISTEN : ")
                    if Z=="A":
                        webbrowser.open_new("https://www.youtube.com/watch?v=N_nyvV8KVc4")
                        C=1
                        B.write("YOU HAVE WATCHED COMMANDO 3")
                        B.close()
                    elif Z=="B":
                        webbrowser.open_new("https://www.youtube.com/watch?v=BODMpqsZMLs")
                        C=1
                        B.write("YOU HAVE WATCHED HEROPANTI")
                        B.close()
                    elif Z=="C":
                        webbrowser.open_new("https://www.youtube.com/watch?v=SfdEe_7OLec")
                        C=1
                        B.write("YOU HAVE WATCHED BAAGHI")
                        B.close()
                    elif Z=="D":
                        webbrowser.open_new("https://www.youtube.com/watch?v=_fRsCnEP7E4")
                        C=1
                        B.write("YOU HAVE WATCHED ABCD")
                        B.close()
                    elif Z=="E":
                        webbrowser.open_new("https://www.youtube.com/watch?v=KcxaB3FwGqY")
                        C=1
                        B.write("YOU HAVE WATCHED BAHUBALI THE BEGINNING")
                        B.close()
                    elif Z=="F":
                        webbrowser.open_new("https://www.youtube.com/watch?v=TxXrGzNiqhc")
                        C=1
                        B.write("YOU HAVE WATCHED BABHUBALI THE CONCLUSION")
                        B.close()
                    else:
                        print("BY MISTAKELY YOU HAVE TYPED",Z,"INSTEAD OF OPTIONS GIVEN TO YOU")
                        C=0
                elif A=="C":
                    print("WELCOME TO THE COMEDY MOVIE ZONE ")
                    print(""" PLEASE SELECT YOUR MOVIE FROM BELOW LIST :
 A= PK                                * C= TOTAL DHAMAAL 
 B= ENTERTAINMENT                     * D= PHIR HERA PHERI """)
                    Z=input("ENTER THE OPTIONS WHAT YOU WANT TO LISTEN A/B/C/D : ")
                    if Z=="A":
                        webbrowser.open_new("https://www.youtube.com/watch?v=XXEsZe3TI2Y")
                        C=1
                        B.write("YOU HAVE WATCHED PK")
                        B.close()
                    elif Z=="B":
                        webbrowser.open_new("https://www.youtube.com/watch?v=LXXkiUKDK4w")
                        C=1
                        B.write("YOU HAVE WATCHED ENTERTAINMENT")
                        B.close()
                    elif Z=="C":
                        webbrowser.open_new("https://www.youtube.com/watch?v=LKNHVDPKy7g")
                        C=1
                        B.write("YOU HAVE WATCHED TOTAL DHAMMAL")
                        B.close()
                    elif Z=="D":
                        webbrowser.open_new("https://www.youtube.com/watch?v=TIQ5hrfermg")
                        C=1
                        B.write("YOU HAVE WATCHED PHIR HERA PHERI")
                        B.close()
                    else:
                        print("BY MISTAKELY YOU HAVE TYPED",Z,"INSTEAD OF OPTIONS GIVEN TO YOU")
                        C=0
                else:
                    print("YOU HAVE TYPED ANY WRONG LETTER INSTEAD OF GIVEN IN THE OPTIONS ")
            C=0
