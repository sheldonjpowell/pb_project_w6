from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.Numeric, nullable=False)
    address = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    #  name = StringField('name', validators=[DataRequired()])
    # phonenumber = PasswordField('Phonenumber', validators=[DataRequired()])
    # address = PasswordField('Address', validators=[DataRequired()])
    # submit = SubmitField('

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User|{self.username}>"

    def __str__(self):
        return self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)