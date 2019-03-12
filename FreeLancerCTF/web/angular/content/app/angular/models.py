from sqlalchemy.ext.hybrid import hybrid_property
from ..app import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.UnicodeText(), unique=True, nullable=False)
    role = db.Column(db.UnicodeText(), default = 'nobody', nullable=False)
    authenticated = db.Column(db.Boolean, default = False, nullable=False)
    _password = db.Column(db.String(128))

    address = db.Column(db.UnicodeText(), default = '127.0.0.1', nullable=False)
    age = db.Column(db.UnicodeText(), default = '28', nullable=False)
    first_name = db.Column(db.UnicodeText(), default = 'Elliot', nullable=False)
    last_name = db.Column(db.UnicodeText(), default = 'Alderson', nullable=False)
    nationality = db.Column(db.UnicodeText(), default = 'Freedom', nullable=False)
    number_of_friends = db.Column(db.UnicodeText(), default = '2', nullable=False)
    experience_with_linux = db.Column(db.UnicodeText(), default = 'Mr. Robot', nullable=False)
    meaning_of_life = db.Column(db.UnicodeText(), default = '42', nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_valid(self):
        return ((self.username != '' and self.username != None) and
               (self.password != '' and self.password != None))

    def is_active(self):
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def get_id(self):
        return self.username

    def json(self):
        return {'username':self.username,
                'password':'H4H4H4H4H4',
                'address':self.address,
                'age':self.age,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'nationality':self.nationality,
                'number_of_friends':self.number_of_friends,
                'experience_with_linux':self.experience_with_linux,
                'meaning_of_life':self.meaning_of_life,
                'role':self.role,
                'id':self.id}
