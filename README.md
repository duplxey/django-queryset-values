# Django Query Optimization: Defer, Only, and Exclude

## Want to learn how to build this?

Check out the [post](#).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```
   
1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Populate the database:

    ```sh
    (venv)$ python manage.py populate_db
    ```

1. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
   
1. Navigate to [http://localhost:8000/](http://localhost:8000/) in your browser.
   
## Benchmark

The project comes with [django-silk](https://pypi.org/project/django-silk/) preinstalled, which you can use for checking the performance of the SQL queries: [http://localhost:8000/silk/](http://localhost:8000/silk/).
