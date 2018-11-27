import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_db'
app.config["MONGO_URI"] = 'mongodb://admin:roastbe3f@ds113482.mlab.com:13482/recipe_db'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(username)
    return render_template("index.html")

@app.route('/<username>')
def get_recipes(username):
    return render_template("list_recipes.html", 
    recipes=mongo.db.recipes.find(), username=username)

@app.route('/<username>/<oid>')
def cook_recipe(username, oid):
    return render_template("cook_recipe.html",
    recipe=mongo.db.recipes.find({"_id": ObjectId(oid)}), username=username)

@app.route('/steps/<oid>')
def cook_recipe_fullscreen(oid):
    return render_template("recipe_steps.html",
    recipe=mongo.db.recipes.find({"_id": ObjectId(oid)}))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)