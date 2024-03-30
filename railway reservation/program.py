

import pandas as pd
import numpy as np
import random
import datetime
import matplotlib.pyplot as plt
print("\n\~~~~~~~~~~~~~~~~Welcome! To Ticket Booking System~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("->Fill all the details from the Destination & Price Table exactly Same as given in the Table ") 
print("->Prices Given Against the destinations are the price that you need to pay for respective classes") 
print("~ ~~~~~~~~~~~~ Lets go ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
restart = ('Y')

df=pd.DataFrame(columns=['Registration_id', 'name', 'age', 'gender', 'Boarding place', 'Final Destination', 'Class', 'Date', 'Time of boarding', 'total amount'])
ft=pd.read_csv(r'Destination.csv')
while restart != ('N', 'NO', 'n', 'no'):
    print("Options: --")
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.View graph for price")
    print("4.Exit")
    option = int(input("\nEnter your option (1,2,3,4): "))
    if option == 1:
        people = int(input("\nEnter no. of Ticket you want : "))
        name_l = []
        age_l=[]
        sex_l= []
        print("~~~~~~~~ Destination & prices~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(ft)
        a=input('\nFrom: -')
        if a in ft.values:
            b=input('\nTo:-')
            if b in ft.values:
        
                c=input('\nSelect Class:-')
                if c in ft.columns:
                    year=int(input("\nEnter the Year in which you want to go:-")) 
                    month=int(input("\nEnter the month in which you want to go:-"))
                    day=int(input("\nEnter the Date on which you want to go:-"))
                    d=datetime.date(year, month, day)
                    d2=datetime.date.today()
                    if d>d2:
                        t=pd.read_csv(r"timing.csv")
                        print(t)
                        e=input('\nselect timing:-')
                        if e in t.values:
                            g=ft.set_index('place').at[b,c]
                            h=random.choice (range(10000000,99999999)) 
                            for p in range(people):
                                name =str(input("\nName :- "))
                                name_l.append(name)
                                age=int(input("\nAge:- "))
                            
                                age_l.append(age)
                                sex =str(input("\nMale or Female :- "))
                                sex_l.append(sex)
                                df1=pd.DataFrame(data=[[h, name, age, sex, a,b,c,d,e,g]],
                                                columns=['Registration_id', 'name', 'age', 'gender', 'Boarding place', 'Final Destination', 'Class', 'Date', 'Time of boarding', 'total amount'])
                                df=pd.concat([df,df1],axis=0)
                                df=df.set_index('Registration_id')
                                print('~'*100)
                                print(df)
                                print('~'*100)
                                print('Thank you for your corporation! You have successfully booked your ticket') 
                                restart=str(input("Wan't to book more (Yes/No): "))
                                if restart in ('y', 'YES', 'yes', 'Yes'):
                                    restart = ('Y')
                                else:
                                    x = 0

                        else:
                            print("error, Not given same timing(please write same as given in table)")
                    else:
                        print("error, sorry we dont book tickets for train for past")
                else:
                    print("error, Not gaven same Class as given in top different price")
            else:
                print("error, Not given proper destination (please check for capital letters in table)")    
        else:
            print("error, Not given proper destination (please check for capital letters in table)")
 
    elif option == 2:
        cancel=int(input("\nEnter your registration id (8-digit code given in your reciept)")) 
        if cancel in df.index:
            confirm=input("\nDo you really want to cancel your Reservation (Yes/No):-")
            if confirm in ('y', 'YES', 'yes', 'Yes'):
                print('~'*100)
                print("\nYour Reservation has been canceled successfully :) ")
                df.drop([cancel], inplace=True)
                print('~'*100)



            else:
                restart=('Y')
                print(~100)
        else:

            print("\ninvalid input") 
            print('~'*100)
    elif option == 3:
        print("5. Plot line Graph")
        print("6. Plot Bar graph")
        option2=int(input("Enter your choice (5,6)"))
        p=ft['place'] 
        priceac=ft['AC']
        priceseat=ft['Seating']
        pricesleep=ft['Sleeper'] 
        if option2 == 5: 
            f=plt.figure()
            f.set_figwidth(30)
            f.set_figheight(10)
            plt.plot(p, priceac, label='AC price') 
            plt.plot(p, priceseat, label='Seating price') 
            plt.plot(p, pricesleep, label='Sleeper price')
            plt.xlabel('Places')
            plt.ylabel('Prices')
            plt.legend()
            plt.show()
        else:

            f=plt.figure()
            f.set_figwidth(30)
            f.set_figheight(10)
            w=0.3
            bar1=np.arange(len(p))
            bar2=[i+w for i in bar1]
            bar3=[i+w for i in bar2]
            plt.bar(bar1, priceac,w, label='AC price', color='r')
            plt.bar(bar2, priceseat,w, label='Seating price', color='g')
            plt.bar(bar3, pricesleep,w, label='Sleeper price', color='y') 
            plt.xlabel('Places')
            plt.ylabel('Prices') 
            plt.legend()
            plt.show()
    else:
        break
print('~'*100)
print("\nSee You Soon :)")