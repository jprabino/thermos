from flask import Flask, render_template, url_for

app = Flask(__name__)
class User(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def initials(self, initials = None):
        if not initials:
            initials = "{}.{}.".format(self.first[0], self.last[0])
        return initials

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Nominal", user=User('Juan', 'Rabino'))

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)