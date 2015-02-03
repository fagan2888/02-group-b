from flask import Flask, render_template

app = Flask(__name__)
#Main DEW page
@app.route('/')
def home():
    return render_template("index.html")

#About page
@app.route('/about')
def about():
    return render_template("about.html")

"{{url_for('static', filename='us.json')}}"


if __name__ == '__main__':
    app.run(debug=True)
