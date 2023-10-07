import os
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy

database_name = "hollywood"
database_path = "{}/{}".format(os.environ['DATABASE_URL'],database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()

def db_drop_and_create_all():
  db.drop_all()
  db.create_all()

class Movie(db.Model):
  __tablename__ = "movies"

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  release_date = Column(Date, nullable=True)
  star = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=True)

  def __init__(self, title, release_date, star):
    self.title = title
    self.release_date = release_date
    self.star = star

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
      'star': self.star
    }

class Actor(db.Model):
  __tablename__ = "actors"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=True)
  gender = Column(String, nullable=True)
  movie = db.relationship('Movie', backref='actor', lazy=True)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }
