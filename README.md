# CS3380 - Final Project: Phase 3
Basic:
MySQL DBMS interface with Python (Python/MySQL Connector)

System Breakdown:
- 'generalFunc()'
  - obtains User ID and chosen option as user input
  - Funnels data (user Id) out to one of the other 3 functions based on option chosen
- 'findItem()'
  - prompts user to enter a clothing type, appends the type to pre-built SQL query, returns rows of PRODUCTS from DB that are of the chosen type
- 'viewCart()'
  - appends current user ID onto pre-built SQL query and returns appropriate user CART data
- 'viewOrders()'
  - appends current user ID onto pre-built SQL query and returns appropriate user ORDER data
