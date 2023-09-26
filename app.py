from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/rickrollsite')
def rickrollsite():
    return render_template('rickrollsite.html')

if __name__ == "__main__":
    app.run()