from flask import render_template
from app import app
from app.models import WordClass, DuolingoWord
from app.utils import *


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Guilllermo'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/ipa/<ipa_symbol>')
def ipa(ipa_symbol):
    words_with_ipa = DuolingoWord \
        .query \
        .filter(DuolingoWord.pronunciation.contains(ipa_symbol)) \
        .all()

    if is_diphthong(ipa_symbol):
        return render_template('ipa.html', ipa_symbol=ipa_symbol, words_with_ipa=words_with_ipa)
    else:
        words_without_diphthongs = \
            list(filter(lambda duolingo_word: not has_diphthong(ipa_symbol, duolingo_word.pronunciation),
                        words_with_ipa))
        return render_template('ipa.html', ipa_symbol=ipa_symbol, words_with_ipa=words_without_diphthongs)