from datetime import datetime
from flask import Flask, render_template, url_for, redirect, request, flash
from forms import BookmarkForm

app = Flask(__name__)

bookmarks = []

app.config['SECRET_KEY'] = '\xba\xf5\xa6\x076\xe4\x9eb\x10\x8bZpV\x13:\xfey\xfc\x9a\xc4\x82A\x7f\xe2'
def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = 'juan.rabino',
        date = datetime.utcnow()
    ))

class User(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def initials(self, initials = None):
        if not initials:
            initials = "{}.{}.".format(self.first[0], self.last[0])
        return initials


def new_bookmarks(num):
    return sorted(bookmarks, key= lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5),
                           title="Nominal", user=User('Juan', 'Rabino'))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash('Stored Url: {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
if __name__ == '__main__':
    app.run(debug=True)