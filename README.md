# FSND-Capstone project: Casting Agency API

## Final project for Udacity FSND

Render link: TODO: Replace with running endpoint
Local link: http://127.0.0.1:8080

## Getting started

### Installing dependencies

#### Python 3.8

Follow instructions to install latest version of python for your platform using [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual environment

Suggest using a virtual environment when working with python projects to keep dependencies separate and organized. Follow instructions to setup a virtual environment for your platform using [python docs](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

#### Dependencies install

Once inside your virtual environment, install the python dependencies using:

```bash
pip install -r requirements.txt
```

## Running the app

Before starting the API service, it is optional to uncomment the `db_drop_and_create_all()` from the app.py file. This will reset back to a blank database.
!!! DO NOT DO THIS IF YOU DON'T WANT TO ERASE YOUR DATA !!!

To run the app execute the following from the root directory of the repo:

```bash
export DATABASE_URL=<ex: 'postgresql://postgres@localhost:5432'>
export FLASK_APP=app.py
flask run
```

Note: make sure to replace the `DATABASE_URL` with your unique path and credentials

## API References

### Getting started

Base URL: can be run locally or on a hosted platform

Authentication: required for various actions within the API. Every endpoint, with the exception of the root `/` endpoint, require some form of authentication to access. Authentication is proved via the `bearer` token generated through auth0.

There are 3 different types of roles with unique authentication permissions:
  - Assistant:
    - Can only view information
    - Has permissions `get:actors` & `get:movies`
  - Director:
    - Full control over actors, limited control over movies
    - Has permissions`add:actor`, `delete:actor`, `get:actors`, `get:movies`, `update:actor` & `update:movie`
  - Producer:
    - Full control over actors and movies
    - Has permissions `add:actor`, `add:movie`, `delete:actor`, `delete:movie`, `get:actors`, `get:movies`, `update:actor` & `update:movie`

### Error Handling

Errors are displayed as JSON objects of the following format

```
{
  'success': False,
  'error': 400,
  'message': 'bad request'
}
```

The API can handle several different common error codes including:
  - 400: Bad request
  - 401: Unauthorized
  - 403: Permission denied
  - 404: Not found
  - 405: Method not allowed
  - 422: Unprocessable
  - 500: Server error

### Endpoints

Note all 'request example' snippets are coded for local running but can be replaced with whatever path makes sense for your running environment.

#### GET /

This is the root endpoint of the app which can be used as a status check and requires no authentication.

##### Example request

`http://localhost:8080/`

##### Example return

```
{
    "status": "A-OK!"
}
```

#### GET /actors

- Returns all actors in the database
- Requires the `get:actors` permission

##### Example request

`http://localhost:8080/actors`

##### Example return

```
{
    "actors": [
        {
            "age": 61,
            "gender": "male",
            "id": 1,
            "name": "Tom Cruise"
        },
        {
            "age": 59,
            "gender": "male",
            "id": 2,
            "name": "Brad Pitt"
        },
        {
            "age": 38,
            "gender": "female",
            "id": 3,
            "name": "Scarlett Johansson"
        }
    ],
    "success": true
}
```

#### POST /actors

- Creates a new actor
- Requires the `add:actor` permission
- Body:
  - name: string, required
  - age: int, not required
  - gender: string, not required

##### Example request

- endpoint: `http://localhost:8080/actors`
- body:
```
{
    "name": "Brad Pitt",
    "gender": "male",
    "age": 59
}
```

##### Example return

```
{
    "success": true
}
```

#### DELETE /actors/\<int:actor_id\>

- Deletes the actor with the specified id
- Requires the `delete:actor` permission

##### Example request

- endpoint: `http://localhost:8080/actors/1`

##### Example return

```
{
    "delete": 1,
    "success": true
}
```

#### PATCH /actors/\<int:actor_id\>

- Updates the actor with the specified id
- Requires the `update:actor` permission
- None of the fields in the body are required, if a field is empty the value already stored will not change
- Body:
  - name: string
  - age: int
  - gender: string

##### Example request

- endpoint: `http://localhost:8080/actors/1`
- body:
```
{
    "name": "Brad Pitt",
    "gender": "male",
    "age": 59
}
```

##### Example return

```
{
    "actors": [
        {
            "age": 59,
            "gender": "male",
            "id": 1,
            "name": "Brad Pitt"
        }
    ],
    "success": true
}
```

#### GET /movies

- Get all movies storied in database
- Requires the `get:movies` permission

##### Example request

- endpont: `http://localhost:8080/movies`

##### Example return

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 16 May 1986 04:00:00 GMT",
            "star": 1,
            "title": "Top Gun"
        },
        {
            "id": 2,
            "release_date": "Fri, 17 Oct 2014 04:00:00 GMT",
            "star": 2,
            "title": "Fury"
        },
        {
            "id": 3,
            "release_date": "Fri, 09 Jul 2021 04:00:00 GMT",
            "star": 3,
            "title": "Black Widow"
        }
    ],
    "success": true
}
```

#### POST /movies

- Create a new movie
- Requires the `add:movie` permission
- Body:
  - title: string, required
  - release_date: date, not required
  - star: int, not required

##### Example request

- endpoint: `http://localhost:8080/movies`
- body:
```
{
    "title": "Fury",
    "star": 2,
    "release_date": "2014-10-17"
}
```

##### Example return

```
{
    "success": true
}
```

#### DELETE /movies/\<int:movie_id\>

- Delete the movie with the specified id
- Requires the `delete:movie` permission

##### Example request

- endpoint: `http://localhost:8080/movies/1`

##### Example return

```
{
    "success": true,
    "movie_id": 1
}
```

#### PATCH /movies/\<int:movie_id\>

- Update the movie with the specified id
- Requires the `update:movie` permission
- None of the fields in the body are required, if a field is empty the value already stored will not change
- Body:
  - title: string
  - release_date: date
  - star: int

##### Example request

- endpoint: `http://localhost:8080/movies/1`
- body:
```
{
    "title": "the little mermaid",
    "release_date": "1989-11-17"
}
```

##### Example return

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 17 Nov 1989 05:00:00 GMT",
            "star": 1,
            "title": "the little mermaid"
        }
    ],
    "success": true
}
```

## Testing

For backend testing, run the following command from the root directory of the repo.

```bash
bash testing/test.sh
```

Alternately, can run commands by hand from the root directory following this order:

```
source setup.sh
dropdb -U postgres hollywood_test
createdb -U postgres hollywood_test
psql -U postgres hollywood_test < data.sql
python3 test_app.py
```
