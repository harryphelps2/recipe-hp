import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_db'
app.config["MONGO_URI"] = 'mongodb://admin:roastbe3f@ds113482.mlab.com:13482/recipe_db'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())

@app.route('/<oid>')
def cook_recipe(oid):
    return render_template("recipe.html",
    recipe=mongo.db.recipes.find({"_id": ObjectId(oid)}))

@app.route('/steps/<oid>')
def cook_recipe_fullscreen(oid):
    return render_template("steps.html",
    recipe=mongo.db.recipes.find({"_id": ObjectId(oid)}))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)