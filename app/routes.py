from flask import render_template
from app import app
from app.models import WordClass, DuolingoWord

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

    words_with_ipa = DuolingoWord.query.filter(DuolingoWord.pronunciation.contains(ipa_symbol)).all()
    # print(words_with_ipa)
    return render_template('ipa.html', ipa_symbol=ipa_symbol, words_with_ipa=words_with_ipa)