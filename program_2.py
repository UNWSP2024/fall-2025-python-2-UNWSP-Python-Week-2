
#Braden Phetsarath
#9/8/25
#Average Age of Friends
def average_age():
    x = int(input("Enter Number of Friend(s) Min 1 Max 5:"))
    #allows for less than 5 friends
    #allows for possible additions to the friend cap
    print ("Enter zero for however many friends not there")
    a = int(input("Enter Age of friend 1:"))
    b = int(input("Enter Age of friend 2:"))
    c = int(input("Enter Age of friend 3:"))
    d = int(input("Enter Age of friend 4:"))
    e = int(input("Enter Age of friend 5:"))
    # Average the ages 
    # Print the results 
    # Sum ages
    print ((a + b + c + d + e)/x, "This is the Average age of your",x,"friends")


# Line which calls the above function.
average_age()
