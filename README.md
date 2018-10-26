### Badges

[![Build Status](https://travis-ci.com/SokoPaulSokool/andela_fast_food_fast.svg?branch=challenge4)](https://travis-ci.com/SokoPaulSokool/andela_fast_food_fast)
[![Coverage Status](https://coveralls.io/repos/github/SokoPaulSokool/andela_fast_food_fast/badge.svg?branch=challenge4)](https://coveralls.io/github/SokoPaulSokool/andela_fast_food_fast?branch=challenge4)
[![Maintainability](https://api.codeclimate.com/v1/badges/f54c04080b3da2fdc162/maintainability)](https://codeclimate.com/github/SokoPaulSokool/andela_fast_food_fast/maintainability)

# APIs for Fast Food Fast

Fast-Food-Fast is a food delivery service app for a restaurant.

## Application is Hosted at [https://andela-fast-food-fast.herokuapp.com](https://andela-fast-food-fast.herokuapp.com)

## Functionality of the APPLICATION

- A new user signs up as customer
- A user who has an account can log in

### Customers can

- View items on the menu
- Place order for food
- View their order history

### Admins can

- Add items to the menu
- Delete items to the menu
- Get all orders made
- Get a specific order
- Change the status of a specific order

### Admin login credentials

```
- email : soko@gmail.com

- password : pass1234
```

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
  $ git checkout challenge4
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
