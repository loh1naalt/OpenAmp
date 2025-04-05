#external imports which are necessary for this script.
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


#Model for table Users (for reference see OpenAmp/SQL_init.sql)
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)

#Model for table Songs (for reference see OpenAmp/SQL_init.sql)
class Songs(db.Model):
    __tablename__ = 'Songs'
    id = db.Column(db.Integer, primary_key=True)
    songname = db.Column(db.String(50), unique=False, nullable=False)
    songartist = db.Column(db.String(50), unique=False, nullable=False)
    serverdirtosong = db.Column(db.String(50), unique=False, nullable=False)
    songduration = db.Column(db.String(50), unique=False, nullable=False)
    playlistid = db.Column(db.String(50), db.ForeignKey('playlists.id'), nullable=False)
    songuploader = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)

#Model for table Playlists (for reference see OpenAmp/SQL_init.sql)
class Playlists(db.Model):
    __tablename__ = 'Playlists'
    id = db.Column(db.Integer, primary_key=True)
    playlistname = db.Column(db.String(50), unique=False, nullable=False)
    playlistuploader = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)



