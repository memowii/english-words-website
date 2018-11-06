from app import db

class WordClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    duolingo_word = db.relationship('DuolingoWord', backref='word class', lazy='dynamic')

    def __repr__(self):
        return '<Word class {}>'.format(self.name)

class DuolingoWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(32))
    pronunciation = db.Column(db.String(32))
    word_class_id = db.Column(db.Integer, db.ForeignKey('word_class.id'))

    def __repr__(self):
        return '<Duolingo Word {}>'.format(self.word)