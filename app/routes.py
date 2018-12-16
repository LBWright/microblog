from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'logan'}
    posts = [
        {
            'author': {'username': 'taylor'},
            'body': 'It\'s a beautiful day outside'
        },
        {
            'author': {'username': 'logan'},
            'body': 'We went to Bass Pro Shop today and it was fun'
        }
    ]
    return render_template('index.html',  user=user, posts=posts)