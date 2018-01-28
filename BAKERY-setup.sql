use eskirk;

create table Customers (
   id int,
   lastName varchar(15),
   firstName varchar(15),
   unique key(id)
);

create table Goods (
   id int,
   flavor varchar(20),
   food varchar(10),
   price float,
   unique key(id)
);

create table Items (
   receipt int,
   ordinal int, 
   item varchar(15)
);

create table Receipts (
   receiptNum int primary key,
   date DATE,
   customerId int,
   unique key(receiptNum) 
);