# opening the file
log_file = open("um-server-01.txt")

# declaring the function with a parameter
def sales_reports(log_file):
    # for loop to go through each line in the file
    for line in log_file:
        #removeing the trailing space 
        line = line.rstrip()
        #making a ner var day and its the first 3 chars of the line
        day = line[0:3]
        #if the day is "Tue" print the line
        if day == "Mon":
            print(line)

def over_10_melons_orders(log_file):
    for line in log_file:
        line = line.rstrip()
        value = line.rstrip('\n').split(' ')
        quantity_of_melon = int(value[2])
        if quantity_of_melon > 10:
            print(line)

# sales_reports(log_file)
over_10_melons_orders(log_file)