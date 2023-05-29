from flask import Flask

### WSGI Application
app = Flask(__name__)

@app.route("/")
def html():
    return "Welcome to the Home Page"

@app.route("/page_2")
def page_2():
    return "This is the 2nd Page"

if __name__ == "__main__":
    app.run(debug=True)
