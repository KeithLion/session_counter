from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'the count'


@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('counter.html')


@app.route('/add2', methods=['post'])
def add():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
