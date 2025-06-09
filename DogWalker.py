def name():
    name_is=input("Enter your name:")
    return name_is
  
def error():
    print("Error. You must enter a number")

def num_dogs():
    while True:
        try:
            total_dogs=int(input("How many dogs for the client: "))
            if total_dogs>3:
                print("You can only enter up to 3 dogs. Please try again.")
            else:
                return total_dogs
        except ValueError:
            error()

def num_days():
    total_days=int(input("How many days has the dog been walked? "))
    return total_days

def num_walks(total_dogs, total_days):
    total_walks=total_dogs*total_days
    return total_walks

def total_charge(total_walks):
    total_cost=total_walks*4.00  
    return total_cost

def invoice(total_dogs, total_days, total_walks, total_cost, name_is):
    print(f"Number of dogs: {total_dogs}")
    print(f"Number of days walked: {total_days}")
    print(f"Total number of walks: {total_walks}")
    print(f"Total cost: £{total_cost}")
    print(f"Name: {name_is}")

def main_program():
    total_dogs=num_dogs()
    total_days=num_days()
    total_walks=num_walks(total_dogs, total_days)
    total_cost=total_charge(total_walks)
    name_is=name()
    invoice(total_dogs, total_days, total_walks, total_cost, name_is)
    

main_program()
