use eskirk;

create table Rooms (
   roomId varchar(3) primary key,
   roomName varchar(20),
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
   checkIn DATE,
   checkOut DATE,
   rate float,
   lastName varChar(15),
   firstName varChar(15),
   adults int,
   kids int
);