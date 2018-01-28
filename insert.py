import csv


# Create an insert statement based on `insert` and write to a file based on `outputFile`
def create_insert_statement(csvFile, outputFile, insert):
   next(csvFile)
   for row in csvFile:
      values = map((lambda x: x), row)
      statement = insert + '(' + ", ".join(values) + ');\n'
      print(statement)
      outputFile.write(statement)


##### INN #####

### Populate the 'Reservations' table
file = open('./INN/Reservations.csv')
outputFile = open('./INN-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['code', 'room', 'checkIn', 'checkOut', 'rate', 'lastName', 'firstName', 'adults', 'kids']
insert = 'INSERT INTO Reservations (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

### Populate the 'Rooms' table
file = open('./INN/Rooms.csv')
outputFile = open('./INN-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['roomId', 'roomName', 'beds', 'bedType', 'maxOccupancy', 'basePrice', 'decor'] 
insert = 'INSERT INTO Rooms (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)



##### BAKERY #####

### Populate the 'Customers' table
file = open('./BAKERY/Customers.csv')
outputFile = open('./BAKERY-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['id', 'lastName', 'firstName']
insert = 'INSERT INTO Customers (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

### Populate the 'Goods' table
file = open('./BAKERY/Goods.csv')
outputFile = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['id', 'flavor', 'food', 'price']
insert = 'INSERT INTO Goods (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

### Populate the 'Items' table
file = open('./BAKERY/Items.csv')
outputFile = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['receipt', 'ordinal', 'item']
insert = 'INSERT INTO Items (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

### Populate the 'Receipts' table
file = open('./BAKERY/receipts.csv')
outputFile = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['receiptNum', 'soldDate', 'customerId']
insert = 'INSERT INTO Receipts (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)



##### AIRLINES #####

### Populate the 'Airlines' table
file = open('./AIRLINES/airlines.csv')
outputFile = open('./AIRLINES-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['id', 'airline', 'abbreviation', 'country']
insert = 'INSERT INTO Airlines (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

### Populate the 'Airports' table
file = open('./AIRLINES/airports100.csv')
outputFile = open('./AIRLINES-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['city', 'airportCode', 'airportName', 'country', 'countryAbbrev']
insert = 'INSERT INTO Airports (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

### Populate the 'Flights' table
file = open('./AIRLINES/flights.csv')
outputFile = open('./AIRLINES-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['airline', 'flightNo', 'sourceAirport', 'destAirport']
insert = 'INSERT INTO Flights (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)