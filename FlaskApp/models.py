import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Profile(Base):
    __tablename__ = "Profile"
    id = Column(Integer, primary_key=True)
    firstName = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    age = Column(Integer, unique=False, nullable=True)
    gender = Column(String(20), unique=False, nullable=True)
    state = Column(String(20), unique=False, nullable=True)
    country = Column(String(50), unique=False, nullable=True)

    def __repr__(self):
        return '<Profile %r>' % self.firstName + " " + self.lastName

class Organization(Base):
    __tablename__ = "Organization"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=False, nullable=False)
    purpose = Column(String(80), unique=False, nullable=True)
    summary = Column(String(2000), unique=False, nullable=True)

    def __repr__(self):
        return '<Organization %r>' % self.name

class Challenges(Base):
    __tablename__ = "Challenges"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=False, nullable=False)
    organizationId = Column(Integer, ForeignKey('Organization.id'), nullable=False)
    catalystId = Column(Integer, ForeignKey('Profile.id'), nullable=False)

    def __repr__(self):
        return '<Challenges %r>' % self.name

class ApprovedTask(Base):
    __tablename__ = "ApprovedTask"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=False, nullable=False)
    description = Column(String(500), unique=False, nullable=True)

    def __repr__(self):
        return '<ApprovedTask %r>' % self.name

class TaskChallenges(Base):
    __tablename__ = "TaskChallenges"
    id = Column(Integer, primary_key=True)
    approvedTaskId = Column(Integer, ForeignKey('ApprovedTask.id'), nullable=False)
    challengeId = Column(Integer, ForeignKey('Challenges.id'), nullable=False)
    participantId = Column(Integer, ForeignKey('Participant.id'), nullable=False)

class Participant(Base):
    __tablename__ = "Participant"
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('Profile.id'), unique=False, nullable=False)
    parentUserId = Column(Integer, ForeignKey('Profile.id'), unique=False, nullable=True)
    counter = Column(Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

# get path of current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///' + dir_path + '/6degree.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)