from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class TVShowDB(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    show = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    seasons = db.Column(db.Integer, nullable=True)
    episodes = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String, nullable=True)
    rating = db.Column(db.String, nullable=True)
    thumbnail = db.Column(db.String, nullable=True)
    year_released = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"TVShowDB('{self.show}', '{self.description}', '{self.seasons}', '{self.episodes}', '{self.genre}'" \
               f"'{self.rating}', {self.thumbnail}, {self.year_released})"


class SeasonDB(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    show = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    season = db.Column(db.Integer, nullable=False)
    episodes = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String, nullable=False)
    thumbnail = db.Column(db.String, nullable=False)
    year_released = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"SeasonDB('{self.show}', '{self.description}', '{self.season}', '{self.episodes}', " \
               f"'{self.rating}', {self.thumbnail}, {self.year_released})"


class EpisodeDB(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    show = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    season = db.Column(db.Integer, nullable=False)
    episode = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String, nullable=False)
    thumbnail = db.Column(db.String, nullable=False)
    date_released = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"EpisodeDB('{self.show}', '{self.description}', '{self.season}', '{self.episode}', " \
               f"'{self.rating}', {self.thumbnail}, {self.date_released})"


class AssetDB(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"AssetDB('{self.title}', '{self.filename}', '{self.path}', '{self.date_created}')"
