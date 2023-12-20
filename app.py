from flask import Flask, render_template
import flask
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/order')
def order():
    return render_template('order.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/done', methods=['POST'])
def done():
    con = sqlite3.connect("data.db")
    cur = con.cursor()

    name = flask.request.form['name']
    num = flask.request.form['num']

    cur.execute("INSERT INTO Customers (Name,Number) VALUES (?,?)",(name, num))
    con.commit()

    con.close()
    
    return render_template('done.html')



if __name__ == '__main__':
    app.run(debug=True)
