from datetime import datetime
from app import db, bcrypt



# class User(db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(20))
#     user_email = db.Column(db.String(60), unique=True, index=True)
#     user_password = db.Column(db.String(80))
#     registration_date = db.Column(db.DateTime, default=datetime.now)
#
#     # class methods belong to a class but are not associated with any class instance
#     @classmethod
#     def create_user(cls, user, email, password):
#
#         user = cls(user_name=user,
#                    user_email=email,
#                    user_password=bcypt.generate_password_hash(password).decode('utf-8')
#                    )
#
#         db.session.add(user)
#         db.session.commit()
#         return user

class Publication(db.Model):

    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Publisher is {}'.format( self.name)


class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} byg {}'.format(self.title, self.author)

