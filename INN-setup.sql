use CSC365Lab2;
drop table if exists reservations;
drop table if exists rooms;

create table rooms (
   roomId varchar(3) NOT NULL,
   roomName varchar(30) NOT NULL,
   beds int NOT NULL,
   bedType varchar(10) NOT NULL,
   maxOccupancy int NOT NULL,
   basePrice float NOT NULL,
   decor varchar(15) NOT NULL,
   CONSTRAINT PRIMARY KEY(roomId)
);

create table reservations (
   code int NOT NULL,
   room varchar(3) NOT NULL NOT NULL,
   checkIn date NOT NULL,
   checkOut date NOT NULL,
   rate float NOT NULL,
   lastName varChar(15) NOT NULL,
   firstName varChar(15) NOT NULL,
   adults int NOT NULL, 
   kids int NOT NULL,
   CONSTRAINT PRIMARY KEY(code)
);