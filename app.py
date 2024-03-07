from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

def index():
    # return "<h1>Hello world</h1>"
    first_name = "john"
    favorite_pizza = ["pepperoni", "cheese", "mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')

def user(name):
    # return  f"<h1>hello {name} </h1>"
    return render_template("user.html", name=name)

# create custom error page
#  invalid url
@app.errorhandler(404)
def page_not_find(e):
    return render_template("404.html"), 404

# internal server error

@app.errorhandler(500)
def page_not_find(e):
    return render_template("500.html"), 500