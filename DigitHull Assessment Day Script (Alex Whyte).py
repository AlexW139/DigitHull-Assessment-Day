# Most popular blend of coffee

# Opening the txt file for the sales
Sales = open("Sales.txt")
Monday = Sales.read()

# Split up the string into seperate lines (now a list of strings)
Monday_line = Monday.split('\n')

# For each line in the list, test to see if the name Espresso, but not Double, is present.
# If it is, sum up the quantity sold.

val1 = 0
for line in Monday_line:
    if "Espresso" in line and "Double" not in line:
        Esp = line.split(', ')[2] 
        
        for x in Esp:
            val1 = val1 + int(x)
print("The number of Espressos sold on Monday was %d." % (val1))

# For each line in the list, test to see if the name Flat is present.
# If it is, sum up the quantity sold.

val2 = 0
for line in Monday_line:
    if "Flat" in line:
        Flat = line.split(', ')[2] 
        
        for x in Flat:
            val2 = val2 + int(x)
print("The number of Flat Whites sold on Monday was %d." % (val2))

# For each line in the list, test to see if the name Double is present.
# If it is, sum up the quantity sold.

val3 = 0
for line in Monday_line:
    if "Double" in line:
        Double = line.split(', ')[2] 
        
        for x in Double:
            val3 = val3 + int(x)
print("The number of Double Espressos sold on Monday was %d." % (val3))

# For each line in the list, test to see if the name Latte is present.
# If it is, sum up the quantity sold.

val4 = 0
for line in Monday_line:
    if "Latte" in line:
        Latte = line.split(', ')[2] 
        
        for x in Latte:
            val4 = val4 + int(x)
print("The number of Lattes sold on Monday was %d." % (val4))

# For each line in the list, test to see if the name Americano is present.
# If it is, sum up the quantity sold.

val5 = 0
for line in Monday_line:
    if "Americano" in line and "White" not in line:
        Am = line.split(', ')[2] 
        
        for x in Am:
            val5 = val5 + int(x)
print("The number of Americanos sold on Monday was %d." % (val5))

# For each line in the list, test to see if the name White Americano is present.
# If it is, sum up the quantity sold.

val6 = 0
for line in Monday_line:
    if "White Americano" in line:
        White = line.split(', ')[2] 
        
        for x in White:
            val6 = val6 + int(x)
print("The number of White Americanos sold on Monday was %d." % (val6))

# Determine which coffee blend was the most popular
quant = [val1, val2, val3, val4, val5, val6]
pop = max(quant)

# Need to print the corresponding name for the value that corresponds to pop...