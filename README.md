# andela_fast_food_fast

Fast-Food-Fast is a food delivery service app for a restaurant.

### Badges

[![Build Status](https://travis-ci.com/SokoPaulSokool/andela_fast_food_fast.svg?branch=challenge2)](https://travis-ci.com/SokoPaulSokool/andela_fast_food_fast)
[![Coverage Status](https://coveralls.io/repos/github/SokoPaulSokool/andela_fast_food_fast/badge.svg?branch=challenge2)](https://coveralls.io/github/SokoPaulSokool/andela_fast_food_fast?branch=challenge2)
[![Maintainability](https://api.codeclimate.com/v1/badges/f54c04080b3da2fdc162/maintainability)](https://codeclimate.com/github/SokoPaulSokool/andela_fast_food_fast/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f54c04080b3da2fdc162/test_coverage)](https://codeclimate.com/github/SokoPaulSokool/andela_fast_food_fast/test_coverage)

# APIs for Fast Food Fast

These are APIs to be used to interface the fuctionality of the Fast Food Fast application

## Functionality

- Placing order for food
- Obtaining a list of orders.
- Fetching a specific order.
- Updating the order status.
- Delete order

These are the endpoints

| METHOD | Endpoint          | Description                                                          | Body (json)                                                    |
| ------ | :---------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| GET    | /api/v1/orders/   | Get all orders                                                       |                                                                |
| GET    | /api/v1/orders/id | Get specific orders using an id                                      |                                                                |
| POST   | /api/v1/orders    | Place a new orders                                                   | order_title, order_description ,order_price ,delivery_location |
| PUT    | /api/v1/orders/id | Update a specific orders status to 'complete','pending','incomplete' | order_status                                                   |
| DELETE | /api/v1/orders/id | Delete a specific entry using an id                                  |                                                                |

APIs are Hosted at https://andela-fast-food-fast.herokuapp.com

Sample get all orders [https://andela-fast-food-fast.herokuapp.com/api/v1/orders](https://andela-fast-food-fast.herokuapp.com/api/v1/orders)

## Setting Up for Development

These are instructions for setting up Fast Food Fast app in a development enivornment.

### Prerequisites

- Python 3.6

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

* switch to challenge2 branch

  ```
  $ git checkout challenge2
  ```

* Install necessary requirements

  ```
  $ pip install -r requirements.txt
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
