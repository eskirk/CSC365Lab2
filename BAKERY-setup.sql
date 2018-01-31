use CSC365Lab2;
drop table if exists customers;
drop table if exists goods;
drop table if exists items;
drop table if exists receipts;

create table customers (
   id int NOT NULL,
   lastName varchar(15) NOT NULL,
   firstName varchar(15) NOT NULL,
   CONSTRAINT PRIMARY KEY(id)
);

create table goods (
   id varchar(15) NOT NULL,
   flavor varchar(20) NOT NULL,
   food varchar(10) NOT NULL,
   price decimal NOT NULL,
   CONSTRAINT PRIMARY KEY(id)
);

create table items (
   receipt int NOT NULL,
   ordinal int NOT NULL,  
   item varchar(15) NOT NULL,
   CONSTRAINT PRIMARY KEY(receipt, ordinal)
);

create table receipts (
   receiptNum int NOT NULL,
   soldDate date NOT NULL,
   customerId int NOT NULL,
   CONSTRAINT PRIMARY KEY(receiptNum)
);