import os
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_db'
app.config["MONGO_URI"] = 'mongodb://admin:roastbe3f@ds113482.mlab.com:13482/recipe_db'

mongo = PyMongo(app)

@app.route('/')
def get_recipes():
    return render_template("list_recipes.html", 
    recipes=mongo.db.recipes.find())

@app.route('/<oid>')
def cook_recipe(oid):
    return render_template("cook_recipe.html",
    recipe=mongo.db.recipes.find({"_id": ObjectId(oid)}))

@app.route('/upvote/<recipe_id>')
def upvote(recipe_id):
    recipes = mongo.db.recipes
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    current_upvotes = the_recipe['upvotes']
    print(type(current_upvotes))
    new_upvotes = current_upvotes + 1
    print(type(new_upvotes))
    recipes.update( 
        {'_id': ObjectId(recipe_id)},
        { '$set': { "upvotes": new_upvotes } }
    )
    # the_recipe['upvotes'] += 1
    return redirect(url_for('cook_recipe', oid=recipe_id ))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")

@app.route('/insert_recipe', methods=['POST','GET'])
def insert_recipe():
    new_recipe = request.form.to_dict()
    recipes =  mongo.db.recipes
    recipes.insert_one(new_recipe)
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>', methods=['POST','GET'])
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)

@app.route('/update_recipe/<recipe_id>', methods=["GET","POST"])
def update_recipe(recipe_id):
    print(request.form)
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'dish':request.form['dish'],
        'author':username,
        'cooking_time':request.form['cooking_time'],
        'picture' : request.form['picture'],
        'ingredients': request.form['ingredients'],
        'upvotes': '0',
        'step_1':request.form['step_1'],
        'step_2':request.form['step_2'],
        'step_3':request.form['step_3'],
        'step_4':request.form['step_4'],
        'step_5':request.form['step_5'],
        'step_6':request.form['step_6'],
        'step_7':request.form['step_7'],
        'step_8':request.form['step_8'],
        'step_9':request.form['step_9'],
        'step_10':request.form['step_10']
    })
    return redirect(url_for('cook_recipe', oid=recipe_id ))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)