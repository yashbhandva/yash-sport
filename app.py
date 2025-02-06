from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # Make sure the function name is 'index'
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/trainer')
def trainer():
    return render_template('tranner.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
