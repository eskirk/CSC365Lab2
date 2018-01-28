drop table if exists Airlines;
drop table if exists Airports;
drop table if exists Flights;
use CSC365Lab2;

create table Airlines (
   id int primary key,
   airline varchar(30),
   abbreviation varchar(20),
   country varchar(10),
   unique key(id)
);

create table Airports (
   city varchar(20) not null,
   airportCode varchar(3) not null,
   airportName varchar(50) not null,
   country varchar(20) not null,
   countryAbbrev varchar(10) not null,
   unique key(airportCode)
);

create table Flights (
   airline int,
   flightNo int,
   sourceAirport varchar(3),
   destAirport varchar(3)
);