drop database if exists eskirk;
create database eskirk;
use eskirk;

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
   airportName varchar(20) not null,
   country varchar(20) not null,
   countryAbbrev varchar(10) not null,
   unique key(airportCode)
);

create table Flights (
   airline int primary key,
   flightNo int,
   sourceAirport varchar(3),
   destAirport varchar(3)
);