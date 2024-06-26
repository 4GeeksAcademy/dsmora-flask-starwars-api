from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model): 
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model): 
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class FavoritesPeople(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),  nullable = True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable = True)

    user = db.relationship(User)
    people = db.relationship(People)

    def serialize(self):
        return {
            "id": self.id,
        }
    
class FavoritesPlanets(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),  nullable = True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable = True)

    user = db.relationship(User)
    planet = db.relationship(Planet)

    def serialize(self):
        return {
            "id": self.id,
        }


