### Badges

[![Build Status](https://travis-ci.com/SokoPaulSokool/andela_fast_food_fast.svg?branch=develop)](https://travis-ci.com/SokoPaulSokool/andela_fast_food_fast)
[![Coverage Status](https://coveralls.io/repos/github/SokoPaulSokool/andela_fast_food_fast/badge.svg?branch=develop)](https://coveralls.io/github/SokoPaulSokool/andela_fast_food_fast?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f54c04080b3da2fdc162/maintainability)](https://codeclimate.com/github/SokoPaulSokool/andela_fast_food_fast/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f54c04080b3da2fdc162/develop)](https://codeclimate.com/github/SokoPaulSokool/andela_fast_food_fast/develop)

# APIs for Fast Food Fast

Fast-Food-Fast is a food delivery service app for a restaurant.

These are APIs to be used to interface the fuctionality of the Fast Food Fast application.

## Functionality of the API

- A new user signs up as either admin or customer
- A user who has an account can log in

### Customers can

- Place order for food
- View their order history
- View items on the menu

### Admins can

- Get all orders made
- Get a specific order
- Get a specific order
- Change the status of a specific order
- Add items to the menu

These are the endpoints

| METHOD | Endpoint            | Description                                                          | Body (json)         |
| ------ | :------------------ | -------------------------------------------------------------------- | ------------------- |
| POST   | /api/v1/auth/login  | Provides a token to be used by a user as they access other endpoints | user_name, password |
| POST   | /api/v1/auth/signup | Signs up a user for an account                                       |                     |

| METHOD | Endpoint             | Description                                           | Body (json)                |
| ------ | :------------------- | ----------------------------------------------------- | -------------------------- |
| POST   | /api/v1/users/orders | Places order for an item in the menu for the customer | item_id, delivery_location |
| GET    | /api/v1/users/orders | Gets the order histry of the customer                 |                            |
| GET    | /api/v1/menu         | Gets all items on the menu                            |                            |

For Admins only

| METHOD | Endpoint                 | Description                                                           | Body (json)                             |
| ------ | :----------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| GET    | /api/v1/orders/          | Gets all orders made by customers                                     |                                         |
| GET    | /api/v1/orders/<orderId> | Get specific order using an id                                        |                                         |
| PUT    | /api/v1/orders/<orderId> | Updates a specific orders status to 'complete','pending','incomplete' | order_status                            |
| POST   | /api/v1/menu             | Adds food item to the menu                                            | item_name, item_description, item_price |

#### APIs are Hosted at [https://andela-fast-food-fast.herokuapp.com](https://andela-fast-food-fast.herokuapp.com)

#### Documentation for the APIs is found here [https://andela-fast-food-fast.herokuapp.com/apidocs](https://andela-fast-food-fast.herokuapp.com/apidocs)

## Setting Up for Development

These are instructions for setting up Fast Food Fast app in a development enivornment.

### Prerequisites

- Python 3.6

- Access to postgres database

- Make a directory on your computer and a virtual environment

  ```
  $ mkdir fastfoodfast
  ```

- Prepare the virtual environment

  ```
  $ pip install virtualenv
  $ virtualenv venv
  ```

- Clone the project repo

  ```
  $ git clone https://github.com/SokoPaulSokool/andela_fast_food_fast.git
  ```

* switch to challenge3 branch

  ```
  $ git checkout challenge3
  ```

* Install necessary requirements

  ```
  $ pip install -r requirements.txt
  ```

* Set up connection to your local postgress

  ```
  $ Navigate to app/api/models/database
  ```

  ```
  $ Open connection.py and adjust the fields below to connect to your local database
        database='',
        user='',
        password='',
        host="",
        port='5432'
  ```

* Run development server
  ```
  $ python app.py
  ```

This site should now be running at http://localhost:5000

### Run Tests

- Make sure pytest is installed

  ```
  $ py.test
  ```
