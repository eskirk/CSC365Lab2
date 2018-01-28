import csv

##### INN #####

### Populate the 'Reservations' table
file = open('./INN/Reservations.csv')
output = open('./INN-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['code', 'room', 'checkIn', 'checkOut', 'rate', 'lastName', 'firstName', 'adults', 'kids']
insert = 'INSERT INTO Reservations (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)

### Populate the 'Rooms' table
file = open('./INN/Rooms.csv')
output = open('./INN-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['roomId', 'roomName', 'beds', 'bedType', 'maxOccupancy', 'basePrice', 'decor'] 
insert = 'INSERT INTO Rooms (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)



##### BAKERY #####

### Populate the 'Customers' table
file = open('./BAKERY/Customers.csv')
output = open('./BAKERY-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['id', 'lastName', 'firstName']
insert = 'INSERT INTO Customers (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)

### Populate the 'Goods' table
file = open('./BAKERY/Goods.csv')
output = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['id', 'flavor', 'food', 'price']
insert = 'INSERT INTO Goods (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)

### Populate the 'Items' table
file = open('./BAKERY/Items.csv')
output = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['receipt', 'ordinal', 'item']
insert = 'INSERT INTO Items (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)

### Populate the 'Receipts' table
file = open('./BAKERY/receipts.csv')
output = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['receiptNum', 'soldDate', 'customerId']
insert = 'INSERT INTO Receipts (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)



##### AIRLINES #####

### Populate the 'Airlines' table
file = open('./AIRLINES/airlines.csv')
output = open('./AIRLINES-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['id', 'airline', 'abbreviation', 'country']
insert = 'INSERT INTO Airlines (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)

### Populate the 'Airports' table
file = open('./AIRLINES/airports100.csv')
output = open('./AIRLINES-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['city', 'airportCode', 'airportName', 'country', 'countryAbbrev']
insert = 'INSERT INTO Airports (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)

### Populate the 'Flights' table
file = open('./AIRLINES/flights.csv')
output = open('./AIRLINES-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['airline', 'flightNo', 'sourceAirport', 'destAirport']
insert = 'INSERT INTO Flights (' + ', '.join(headers) + ') VALUES '

# skip the header line
next(csvFile)
for row in csvFile:
   values = map((lambda x: x), row)
   statement = insert + '(' + ", ".join(values) + ');\n'
   print(statement)
   output.write(statement)