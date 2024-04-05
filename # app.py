# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This would render the HTML file shown above

if __name__ == '__main__':
    app.run(debug=True)