import os
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/static/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
SECRET_KEY = 'my super secret key'.encode('utf8')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY
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

@app.route('/<username>/add_recipe')
def add_recipe(username):
    return render_template("add_recipe.html", username=username)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/insert_recipe', methods=['POST','GET'])
def insert_recipe():
    new_recipe = request.form.to_dict()
    print(new_recipe)
    username = new_recipe["author"]
    print(new_recipe["picture"])
    # if 'file' not in request.files:
    #     flash('No file part')
    #     return redirect(request.url)
    # file = request.files['file']
    # # if user does not select file, browser also
    # # submit an empty part without filename
    # if file.filename == '':
    #     flash('No selected file')
    #     return redirect(request.url)
    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    recipes =  mongo.db.recipes
    print(username)
    recipes.insert_one(new_recipe)
    return redirect(username)

@app.route('/edit_recipe/<recipe_id>', methods=['POST','GET'])
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)

@app.route('/update_recipe/<recipe_id>', methods=["GET","POST"])
def update_recipe(recipe_id):
    print(request.form)
    recipes = mongo.db.recipes
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = the_recipe['author']
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'dish':request.form['dish'],
        'cooking_time':request.form['cooking_time'],
        'ingredients': request.form['ingredients'],
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
    return redirect(url_for('cook_recipe', username=username, oid=recipe_id ))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)