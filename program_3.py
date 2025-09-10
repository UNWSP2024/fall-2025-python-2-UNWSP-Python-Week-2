def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    str(input("Enter names of  5 items :"))
    # potential application menu items i.e all items have a set cost together like a meal deal
    # not very specific whether items should have a set cost
    i1 = int(input("Cost of Item 1:"))
    i2 = int(input("Cost of Item 2:"))
    i3 = int(input("Cost of Item 3:"))
    i4 = int(input("Cost of Item 4:"))
    i5 = int(input("Cost of Item 5:"))
    subt = float(i1+i2+i3+i4+i5)
    x = .07
    #maybe the sales tax changed or different store
    finalc = (subt*.07 + subt)
    print ("Subtotal:",subt, "\nafter tax (7%)", "\nTotal Due:", finalc)
calculate_total_purchase()
