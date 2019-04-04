# CarAPI

Car API is simple CRUD application.

## Start server via Docker(RECOMMEND):
  * Clone repository `git clone https://github.com/KamilSiwek/car_api.git`
  * Go to car_api folder `cd car_api`
  * `docker-compose build`
  * `docker-compose up`

The application will be launched at [`http://0.0.0.0:8000/`](http://0.0.0.0:8000/).

## Start server locally:
  * Clone repository `git clone https://github.com/KamilSiwek/car_api.git`
  * Go to car_api folder `cd car_api`
  * Install dependencies with `pip install -r requirements.txt`
  * Set enviroment variables ("CAR_API_DB_USER", "CAR_API_DB_HOST", "CAR_API_DB_NAME" and "CAR_API_DB_PASSWORD") or add to file car_api/config (fields 'NAME 'HOST' 'USER' and 'PASSWORD' in db config)
  * Create and migrate your database with `python manage.py makemigrations`
  * Create and migrate your database with `python manage.py migrate`
  * Start server with `python manage.py runserver`

The application will be launched at [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).

## Usage:
  * Create new car POST`/car/create`
  body:
  ```
  {
    "model": "Prius",
    "producent": "Toyota",
    "passangers": 5,
    "production_year": 2009,
    "electric_or_hybrid": false,
    "category": "5d",
    "registration_number": "SK9959"
  }
  ```

  * List all cars with inforamtions about motor and category GET`/cars/list?motor_info=true&category_info=true`

  * Show one car GET`/car/retrive?id=d8bdab33-490f-4f24-8510-5ab220e44de5`

  * Update car PUT`/car/retrive?id=d8bdab33-490f-4f24-8510-5ab220e44de5`
  body:
  ```
  {
    "model": "Corolla"
  }
  ```

  * Delete car DELETE`/car/retrive?id=d8bdab33-490f-4f24-8510-5ab220e44de5`

## Testing:

  * To run unit tests use `./manage.py test`
