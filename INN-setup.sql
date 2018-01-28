drop table if exists Reservations;
drop table if exists Rooms;
use CSC365Lab2;

create table Rooms (
   roomId varchar(3),
   roomName varchar(30),
   beds int,
   bedType varchar(10),
   maxOccupancy int,
   basePrice float,
   decor varchar(15),
   unique key(roomId)
);

create table Reservations (
   code int primary key,
   room varchar(3),
   checkIn varchar(10),
   checkOut varchar(10),
   rate float,
   lastName varChar(15),
   firstName varChar(15),
   adults int,
   kids int
);