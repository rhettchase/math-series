# LAB - Class 02

## Project: Modules and Testing

## Project Description

- Creates function called `fibonacci` that returns the nth value in the fibonacci series
- Creates function called `lucas` that returns the nth value in the fibonacci series
- Creates function called `sum_series` that produces numbers from the fibonacci series or lucas series depending on which params are included. If params do not match those series, then add up the numbers of the last two numbers in the series

### Author: Rhett Chase

### Links and Resources
<!-- - [back-end server url](http://xyz.com/) (when applicable)
- [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Real Python](https://realpython.com/lessons/python-fibonacci-sequence-overview/)

### Setup

- `pip install pytest`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

-`python3 series.py`

#### How to use your library (where applicable)

- N/A

#### Tests

- Run tests by activating virtual environment and running `pytest` command in command line
- `test_sum_series` includes 6 tests for various scenarios for which parameters are entered (e.g., left blank, different from `fibonacci` and `lucas` criteria, etc.)
