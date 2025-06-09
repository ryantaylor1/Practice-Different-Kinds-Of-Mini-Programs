from datetime import datetime

adult=20
child=12
seniorcitizen=11
wristband_total=20
maximum_capacity=500
total_tickets_sold=0
date=datetime.now().date()

print("Are you an Admin? Y/N")
user_type=input()

if user_type=="Y":
    print("Enter Admin password:")
    admin_password=input()
    if admin_password=="Admin1234": 
        print("Welcome to Admin Mode.")
        print("Enter new price for Adult ticket:")
        adult=int(input())
        print("Enter new price for Child ticket:")
        child=int(input())
        print("Enter new price for Senior Citizen ticket:")
        seniorcitizen=int(input())
        print("Enter new price for Wristband:")
        wristband_total=int(input())
        print("Prices now updated.")
        print(f"New prices are: Adult = £{adult}, Child = £{child}, Senior Citizen = £{seniorcitizen}, Wristband = £{wristband_total}")

print("Would you like to use the system? Y/N")
system=input()

if system=="Y":
    while total_tickets_sold<maximum_capacity:
        print("Welcome to Copington Adventure Park")
        print(f"These are our prices for today:\nAdult=£{adult}\nChild=£{child}\nSenior Citizen=£{seniorcitizen}")
        print("How many adult tickets would you like?")
        adult_ticket=int(input())
        print("How many child tickets would you like?")
        child_ticket=int(input())
        print("How many senior citizen tickets would you like?")
        seniorcitizen_ticket=int(input())
        
        tickets_wanted=adult_ticket+child_ticket+seniorcitizen_ticket

        if total_tickets_sold+tickets_wanted>maximum_capacity:
            print(f"Sorry, we only have {maximum_capacity-total_tickets_sold} tickets remaining.")
            
        print("Do you want wristbands for you and your companions? Y/N")
        wristband=input()

        print("Please can the lead booker enter their surname: ")
        leadbooker_surname=input()

        print("Do you need a parking pass? Y/N")
        parking_pass=input()

        total=adult_ticket*adult+child_ticket*child+seniorcitizen_ticket*seniorcitizen
        
        if wristband=="Y":
            total+=wristband_total
            print(f"Your total is £{total}")
        else:
            print(f"Your total is £{total}")

        pay=0
        while pay< total:
            print("Enter £10 and £20 pound notes:")
            notes=int(input())
            if notes==10 or notes==20:
                pay+=notes
                print(f"Your total paid so far is: £{pay}")
            else:
                print("Sorry, we can only accept £10 or £20 pound notes.")

        if pay>total:
            change=pay-total
            print(f"Here is your change: £{change}")

        print("Please Confirm your details:\n ")
        print(f"Adult: {adult_ticket}")
        print(f"Child: {child_ticket}")  
        print(f"Senior Citizen: {seniorcitizen_ticket}")
        print(f"Wristband: {wristband}")
        print(f"Parking Pass: {parking_pass}")  
        print(f"Todays Date: {date}")
        print("Is this information correct?")
        confirm_details=input()

        if confirm_details=="Y":
            print("Thank you! Have a great day at Copington Adventure Park.")
            total_tickets_sold+=tickets_wanted
            print(f"Total tickets sold: {total_tickets_sold}")
            print(f"Remaining capacity: {maximum_capacity-total_tickets_sold}")
        else:
            print("Check your details please.")

        if total_tickets_sold>=maximum_capacity:
            print("Sorry, the park has reached its maximum capacity. No more tickets can be sold today.")
            break
else:
    print("Have a nice day!")
