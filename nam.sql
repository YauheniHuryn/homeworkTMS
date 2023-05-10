
CREATE TABLE Customers(
    CustomerID INT PRIMARY KEY,
    SurnameName VARCHAR(100),
    Address VARCHAR(100),
    Contact VARCHAR(100)
    );


CREATE TABLE Orders(
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    foreign key (CustomerID) references Customers(CustomerID)
    );

CREATE TABLE Products(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10,2)
    );

CREATE TABLE OrderDetails (
    ProductID INT,
    OrderID INT,
    Quantity INT,
    PRIMARY KEY (ProductID, OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    );


INSERT INTO Customers(CustomerID, SurnameName, Address, Contact)
VALUES (101, 'Huryn Yauheni', 'Minsk, pr. Partizanski 26', '+375291033603'),
(102, 'Bernal Ruis Fabian', 'Berlin, Friedrihstrasse 24', '+49294673603'),
(103, 'Limonov Daniil', 'Warshawa, Pielsudkego 269', '+48732343603'),
(104, 'Crispot Caroline', 'Nancy, av. Niveau 13-26', '+232469394');

INSERT INTO Orders(OrderID, CustomerID, OrderDate)
VALUES
(001, 101, '2022-12-22'),
(002, 102, '2022-11-24'),
(003, 101, '2023-02-03'),
(004, 103, '2022-12-10'),
(005, 102, '2023-02-01'),
(006, 104, '2023-03-08'),
(007, 103, '2023-03-08'),
(008, 102, '2023-01-22');

INSERT INTO Orders(OrderID, CustomerID, OrderDate)
VALUES
(001, 101, '2022-12-22'),
(002, 102, '2022-11-24'),
(003, 101, '2023-02-03'),
(004, 103, '2022-12-10'),
(005, 102, '2023-02-01'),
(006, 104, '2023-03-08'),
(007, 103, '2023-03-08'),
(008, 102, '2023-01-22');

INSERT INTO Products(ProductID, ProductName, Price) 
VALUES (10000, 'Book', 15.99),
(10020, 'Tablet', 499.99),
(20019, 'Vacuum', 59.50),
(20390, 'Microwave', 79.00),
(30330, 'TV', 230.49),
(14509, 'Potato Chips', 1.00),
(10549, 'Shower Gel', 4.99),
(10192, 'Phone', 399.99);

INSERT INTO OrderDetails(ProductID, OrderID, Quantity) 
VALUES (10000, 001, 2),
(10020, 001, 1),
(20019, 003, 1),
(20390, 002, 1),
(30330, 008, 1),
(20019, 004, 1),
(14509, 001, 12),
(14509, 008, 5),
(14509, 002, 2),
(10549, 006, 4),
(10192, 007, 2),
(20019, 005, 2),
(10549, 003, 1),
(10549, 004, 2),
(10000, 005, 2),
(10000, 006, 2);

select * from Orders

