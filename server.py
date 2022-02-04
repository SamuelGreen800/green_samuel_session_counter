from ast import Num
from itertools import count
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key='secrets'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        session['count'] += 1
    
    return render_template('index.html')

@app.route('/increment')
def increment():
    session['count'] += 2
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/sensei', methods=['POST'])
def sensei():
    session['count'] += int(request.form['numb'])
    
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
