drop table if exists Customers;
drop table if exists Goods;
drop table if exists Items;
drop table if exists Receipts;
use CSC365Lab2;

create table Customers (
   id int,
   lastName varchar(15),
   firstName varchar(15),
   unique key(id)
);

create table Goods (
   id varchar(15),
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
   receiptNum int,
   soldDate varchar(15),
   customerId int,
   unique key(receiptNum) 
);