use CSC365Lab2;
drop table if exists inventory_parts;
drop table if exists colors;
drop table if exists inventories;


create table colors (
   id int NOT NULL,
   name varchar(15) NOT NULL,
   rgb varchar(6) NOT NULL,
   is_trans varchar(1) NOT NULL,
   CONSTRAINT PRIMARY KEY(id)
);

create table inventories (
   id int NOT NULL,
   version int NOT NULL,
   set_num varchar(20) NOT NULL,
   CONSTRAINT PRIMARY KEY(id)
);

create table inventory_parts (
   inventory_id int NOT NULL,
   part_num varchar(20) NOT NULL,
   color_id int NOT NULL,
   quantity int NOT NULL,
   is_spare varchar(1) NOT NULL,
   CONSTRAINT FK_inventory_id FOREIGN KEY(inventory_id)
      REFERENCES inventories(id) ON DELETE CASCADE ON UPDATE CASCADE,
   CONSTRAINT FK_color_id FOREIGN KEY(color_id)
      REFERENCES colors(id) ON DELETE CASCADE ON UPDATE CASCADE

);