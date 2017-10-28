from flask import Flask
from flask_sqlalchemy import sqlalchemy
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir_path + '/6degree.db'
db = SQLAlchemy(app)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    state = db.Column(db.String())

    def __repr__(self):
        return '<User %r>' % self.firstName + " " + self.lastName

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    purpose = db.Column(db.String(80), unique=False, nullable=True)
    summary = db.Column(db.String(2000), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

class Challenges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    organizationId = (db.Integer, db.ForeignKey('Organization.id'), nullable=False)
    catalystId = (db.Integer, db.ForeignKey('Profile.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

class ApprovedTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

class TaskChallenges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=False, nullable=False)
    parentUserId = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

