import csv


# basic insert statement
def create_insert_statement(csvFile, outputFile, insert):
    next(csvFile)
    for row in csvFile:
        values = map((lambda x: x), row)
        statement = insert + '(' + ", ".join(values) + ');\n'
        # print(statement)
        outputFile.write(statement)


# insert statement template for receipts
def create_insert_statement_receipts(csvFile, outputFile, insert):
    date_indexes = [1]
    print('Receipts')
    next(csvFile)
    for row in csvFile:
        statement = insert + '('
        index_count = 0
        for item in row:
            if index_count in date_indexes:
                statement += str(', (STR_TO_DATE(' + item.strip().replace('-', ' ') + ', \'%d %M %Y\'))')
            else:
                if index_count == 0:
                    statement += str(item)
                else:
                    statement += str(', ' + item)
            index_count += 1
        statement += ');\n'
        outputFile.write(statement)


# insert statement for reservations
def create_insert_statement_reservations(csvFile, outputFile, insert):
    date_indexes = [2, 3]
    print('Reservations')
    next(csvFile)
    for row in csvFile:
        statement = insert + '('
        index_count = 0
        for item in row:
            if index_count in date_indexes:
                statement += str(', (STR_TO_DATE(' + item.strip().replace('-', ' ') + ', \'%d %M %Y\'))')
            else:
                if index_count == 0:
                    statement += str(item)
                else:
                    statement += str(', ' + item)
            index_count += 1
        statement += ');\n'
        outputFile.write(statement)


# ====== INN ======

# Populate the 'Reservations' table
file = open('./INN/reservations.csv')
outputFile = open('./INN-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['code', 'room', 'checkIn', 'checkOut', 'rate', 'lastName', 'firstName', 'adults', 'kids']
insert = 'INSERT INTO reservations (' + ', '.join(headers) + ') VALUES '

create_insert_statement_reservations(csvFile, outputFile, insert)

# Populate the 'Rooms' table
file = open('./INN/rooms.csv')
outputFile = open('./INN-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['roomId', 'roomName', 'beds', 'bedType', 'maxOccupancy', 'basePrice', 'decor']
insert = 'INSERT INTO rooms (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)


# ====== BAKERY ======

# Populate the 'Customers' table
file = open('./BAKERY/customers.csv')
outputFile = open('./BAKERY-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['id', 'lastName', 'firstName']
insert = 'INSERT INTO customers (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

# Populate the 'Goods' table
file = open('./BAKERY/goods.csv')
outputFile = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['id', 'flavor', 'food', 'price']
insert = 'INSERT INTO goods (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

# Populate the 'Items' table
file = open('./BAKERY/items.csv')
outputFile = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['receipt', 'ordinal', 'item']
insert = 'INSERT INTO items (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

# Populate the 'Receipts' table
file = open('./BAKERY/receipts.csv')
outputFile = open('./BAKERY-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['receiptNum', 'soldDate', 'customerId']
insert = 'INSERT INTO receipts (' + ', '.join(headers) + ') VALUES '

create_insert_statement_receipts(csvFile, outputFile, insert)

# ====== AIRLINES ======

# Populate the 'Airlines' table
file = open('./AIRLINES/airlines.csv')
outputFile = open('./AIRLINES-populate.sql', 'w')
csvFile = csv.reader(file)
headers = ['id', 'airline', 'abbreviation', 'country']
insert = 'INSERT INTO airlines (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

# Populate the 'Airports' table
file = open('./AIRLINES/airports100.csv')
outputFile = open('./AIRLINES-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['city', 'airportCode', 'airportName', 'country', 'countryAbbrev']
insert = 'INSERT INTO airports (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

# Populate the 'Flights' table
file = open('./AIRLINES/flights.csv')
outputFile = open('./AIRLINES-populate.sql', 'a')
csvFile = csv.reader(file)
headers = ['airline', 'flightNo', 'sourceAirport', 'destAirport']
insert = 'INSERT INTO flights (' + ', '.join(headers) + ') VALUES '

create_insert_statement(csvFile, outputFile, insert)

##### CUSTOM #####
