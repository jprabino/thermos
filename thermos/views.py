from datetime import datetime
from flask import render_template, url_for, redirect, request, flash
from thermos import app, db
from models import Bookmark, User
from forms import BookmarkForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5),
                           title="Nominal", user=User('Juan', 'Rabino'))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash('Stored Url: {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
if __name__ == '__main__':
    app.run(debug=True)