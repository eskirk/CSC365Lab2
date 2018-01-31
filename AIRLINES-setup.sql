use CSC365Lab2;
drop table if exists flights;
drop table if exists airports;
drop table if exists airlines;

create table airlines (
   id int NOT NULL,
   airline varchar(30) NOT NULL,
   abbreviation varchar(20) NOT NULL,
   country varchar(10) NOT NULL,
   CONSTRAINT PRIMARY KEY(id)
);

create table airports (
   city varchar(20) NOT NULL,
   airportCode varchar(3) NOT NULL,
   airportName varchar(50) NOT NULL,
   country varchar(20) NOT NULL,
   countryAbbrev varchar(10) NOT NULL,
   CONSTRAINT UNIQUE KEY(airportCode)
);

create table flights (
   airline int NOT NULL,
   flightNo int NOT NULL,
   sourceAirport varchar(3) NOT NULL,
   destAirport varchar(3) NOT NULL,
   CONSTRAINT PRIMARY KEY(airline, flightNo),
   FOREIGN KEY(sourceAirport)
      REFERENCES airports (airportCode)
);