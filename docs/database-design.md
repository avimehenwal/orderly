# Database  Design

is simplistic condeseting the time limitations

we are using in built `User` model provided by django auth in conjunction with following new models

table name | description
-----------|--------------
Product    | all products with theier information
Order      | Order infromation with Foreign key reference to User and Product

## Improvements

- Support for multiple products in each order could be added
- database security and access could be improved
