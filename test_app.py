import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import setup_db, Actor, Movie

class TestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client

    self.database_name = "hollywood_test"
    self.database_path = "{}/{}".format(os.environ['DATABASE_URL'],self.database_name)

    self.producer_token = os.environ['PRODUCER_TOKEN']
    self.assistant_token = os.environ['ASSISTANT_TOKEN']
    self.director_token = os.environ['DIRECTOR_TOKEN']

    setup_db(self.app, self.database_path)

    self.brad_pitt = {
      'name': 'Brad Pitt',
      'gender': 'male',
      'age': 59
    }

    self.tom_cruise = {
      'name': 'Tom Cruise',
      'gender': 'male',
      'age': 61
    }

    self.bad_actor = {
      'name': 'foo',
      'gender': 50,
      'age': 'male'
    }

    self.fury = {
      'title': 'Fury',
      'star': 2,
      'release_date': '2014-10-17'
    }

    self.top_gun = {
      'title': 'Top Gun',
      'star': 1,
      'release_date': '1986-05-16'
    }

    self.bad_movie = {
      'title': 'Fury',
      'star': 2,
      'release_date': 2014-10-17
    }

    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      self.db.create_all()

  def tearDown(self):
    pass

  # Doesn't require any authentication to verify app is running
  def test_app_running(self):
    res = self.client().get('/')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['status'], 'A-OK!')

  def test_add_actor(self):
    res = self.client().post('/actors',
      json = self.brad_pitt,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_add_actor_bad_params(self):
    res = self.client().post('/actors',
      json = self.bad_actor,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)

  def test_update_actor(self):
    actor = Actor.query.first()
    res = self.client().patch(f'/actors/{actor.id}',
      json = self.tom_cruise,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_update_nonexisting_actor(self):
    res = self.client().patch('/actors/100000',
      json = self.tom_cruise,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)

  def test_update_actor_bad_params(self):
    actor = Actor.query.first()
    res = self.client().patch(f'/actors/{actor.id}',
      json = self.bad_actor,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)

  def test_retrieve_all_actors(self):
    res = self.client().get('/actors',
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['actors'])

  def test_delete_actor(self):
    deleted_actor = Actor.query.first()
    actor_id = deleted_actor.id
    cloned_actor = Actor(deleted_actor.name, deleted_actor.age, deleted_actor.gender)
    res = self.client().delete(f'/actors/{actor_id}',
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    cloned_actor.id = actor_id
    cloned_actor.insert()

  def test_delete_invalid_actor(self):
    res = self.client().delete('/actors/1000000',
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)

  def test_add_movie(self):
    res = self.client().post('/movies',
      json = self.fury,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_add_movie_bad_param(self):
    res = self.client().post('/movies',
      json = self.bad_movie,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)

  def test_update_movie(self):
    movie = Movie.query.first()
    res = self.client().patch(f'/movies/{movie.id}',
      json = self.top_gun,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_update_invalid_movie(self):
    res = self.client().patch('/movies/1000000',
      json = self.top_gun,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)

  def test_update_movie_bad_param(self):
    movie = Movie.query.first()
    res = self.client().patch(f'/movies/{movie.id}',
      json = self.bad_movie,
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)

  def test_retrieve_all_movies(self):
    res = self.client().get('/movies',
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['movies'])

  def test_delete_movie(self):
    deleted_movie = Movie.query.first()
    movie_id = deleted_movie.id
    cloned_movie = Movie(deleted_movie.title, deleted_movie.release_date, deleted_movie.star)
    res = self.client().delete(f'/movies/{movie_id}',
      headers = {'Authorization': "Bearer {}".format(self.producer_token)
    })
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    cloned_movie.id = movie_id
    cloned_movie.insert()

  def test_delete_invalid_movie(self):
    res = self.client().delete('/movies/1000000',
      headers = {'Authorization': "Bearer {}".format(self.producer_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)

  def test_add_actor_director_role(self):
    res = self.client().post('/actors',
      json = self.brad_pitt,
      headers = {'Authorization': "Bearer {}".format(self.director_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_add_movie_director_role(self):
    res = self.client().post('/movies',
      json = self.fury,
      headers = {'Authorization': "Bearer {}".format(self.director_token)}
    )

    data = json.loads(res.data)

    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['success'], False)

  def test_retrieve_all_actors_assistant_role(self):
    res = self.client().get('/actors',
      headers = {'Authorization': "Bearer {}".format(self.assistant_token)}
    )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['actors'])

  def test_add_movie_assistant_role(self):
    res = self.client().post('/movies',
      json = self.fury,
      headers = {'Authorization': "Bearer {}".format(self.assistant_token)}
    )

    data = json.loads(res.data)

    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['success'], False)

if __name__ == "__main__":
    unittest.main()
