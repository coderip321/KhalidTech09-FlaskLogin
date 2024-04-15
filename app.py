from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dummy credentials
USERNAME = 'khalid'
PASSWORD = '@khalid000'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            return redirect(url_for('welcome'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
