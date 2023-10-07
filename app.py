from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database.models import setup_db, db_drop_and_create_all, Movie, Actor
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  # WARN: db_drop_and_create_all will remove any existing tables in the defined database and create
  # blank ones. Should only be run on intial app start or when resetting data.
  db_drop_and_create_all()

  CORS(app)

  @app.route('/')
  def status():
    return jsonify({'status': 'A-OK!'}), 200

  @app.route('/actors')
  @requires_auth('get:actors')
  def actors(payload):
    actors = Actor.query.order_by(Actor.id).all()
    formatted_actors = [actor.format() for actor in actors]
    return jsonify({
      'success': True,
      'actors': formatted_actors
    })

  @app.route('/actors', methods=['POST'])
  @requires_auth('add:actor')
  def create_actor(payload):
    body = request.get_json()
    try:
      new_actor = Actor(
        name = body['name'],
        age = body['age'],
        gender = body['gender']
      )
    except:
      abort(400)

    try:
      new_actor.insert()
      return jsonify({
        'success': True
      })
    except:
      abort(422)

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actor(payload, actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
      abort(404)

    try:
      actor.delete()
      return jsonify({
        'success': True,
        'delete': actor_id
      })
    except:
      abort(422)

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('update:actor')
  def modify_actor(payload, actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
      abort(404)

    body = request.get_json()
    if 'name' in body:
      actor.name = body['name']
    if 'age' in body:
      actor.age = body['age']
    if 'gender' in body:
      actor.gender = body['gender']

    try:
      actor.update()
    except:
      abort(422)

    return jsonify({
      'success': True,
      'actors': [actor.format()]
    })

  @app.route('/movies')
  @requires_auth('get:movies')
  def movies(payload):
    movies = Movie.query.order_by(Movie.id).all()
    formatted_movies = [movie.format() for movie in movies]
    return jsonify({
      'success': True,
      'movies': formatted_movies
    })

  @app.route('/movies', methods=['POST'])
  @requires_auth('add:movie')
  def create_movie(payload):
    body = request.get_json()
    try:
      new_movie = Movie(
        title = body['title'],
        star = body['star'],
        release_date = body['release_date']
      )
    except:
      abort(400)

    try:
      new_movie.insert()
      return jsonify({
        'success': True
      })
    except:
      abort(422)

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(payload, movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
      abort(404)

    try:
      movie.delete()
      return jsonify({
        'success': True,
        'movie_id': movie_id
      })
    except:
      abort(422)

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('update:movie')
  def modify_movie(payload, movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
      abort(404)

    body = request.get_json()
    if 'title' in body:
      movie.title = body['title']
    if 'release_date' in body:
      movie.release_date = body['release_date']

    try:
      movie.update()
    except:
      abort(422)

    return jsonify({
      'success': True,
      'movies': [movie.format()]
    })

  # Error handling
  @app.errorhandler(400)
  def bad_request(error):
    return(
      jsonify({
        'success': False,
        'error': 400,
        'message': 'bad request'
      }),
      400
    )

  @app.errorhandler(401)
  def token_expired(error):
    return(
      jsonify({
        'success': False,
        'error': 401,
        'message': 'unauthorized'
      }),
      401
    )

  @app.errorhandler(403)
  def permission_denied(error):
    return(
      jsonify({
        'success': False,
        'error': 403,
        'message': 'permission denied'
      }),
      403
    )

  @app.errorhandler(404)
  def not_found(error):
    return(
      jsonify({
        'success': False,
        'error': 404,
        'message': 'not found'
      }),
      404
    )

  @app.errorhandler(405)
  def method_not_allowed(error):
    return(
      jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
      }),
      405
    )

  @app.errorhandler(422)
  def unprocessable(error):
    return(
      jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
      }),
      422
    )

  @app.errorhandler(500)
  def server_error(error):
    return(
      jsonify({
        'success': False,
        'error': 500,
        'message': 'server error'
      }),
      500
    )

  # AuthError handling
  @app.errorhandler(AuthError)
  def authorization_error(error):
    return(
      jsonify({
        'success': False,
        'error': error.status_code,
        'message': error.error
      }),
      error.status_code
    )

  return app

APP = create_app()

if __name__ == '__main__':
  # Need to change to 127 address bc host has multiple interfaces
  APP.run(host='127.0.0.1', port=8080, debug=True)
  # APP.config['JSON_SORT_KEYS'] = False