# Data-Centric Development Milestone Project - Recipe app

Link to live site: https://recipes-hp.herokuapp.com/

A recipe book where users can add their own recipes, edit recipes and see how popular they are.

## UX

+ As a user want I want to choose a recipe, and buy the ingredients to make it.

+ I want to follow the instructions to make the recipe.

+ I want to know how long it will take me to make it

+ I want to know if it is tasty

+ I want to know if it has any allergens in

+ I want to know how long it is going to take

+ I want to recommend a recipe to a friend 


## Features

### Views

1. A front page year with a carousel of for recipes and a button to click them.

2. A recipe detail page that shows the instructions for cooking the chosen dishes.

3. An all recipes view, showing all recipes on the database on cards sorted by popularity.

4. A filtered view with recipes without allergens.

### Data

1. id

2. Dish: string

3. Author: string

3. Number_of_upvotes: int

4. Preparation_time: int

5. Ingredients: string

6. Steps_#: string

### Functionality

1. Like recipe - Increment upvotes by 1 when a user clicks the like button.

2. Add recipe - Add recipe to the database

3. Edit recipe - Edit recipe entry on the database

### Features to Implement

In the future, I would like to add prices to the ingredients and sum up the cost of each recipe. The user could then filter by budget.

## Technologies Used

The site uses:

1. Python framework [Flask](http://flask.pocoo.org/) for the backend
2. [Materialize](https://materializecss.com/) for front end layout and styling


## Testing

| Scenario                                                                     | Results                                                          |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| User navigates the home page and selects a recipe to cook from the carousel. | The site goes to the choosen recipe in detail.                   |
| User navigates to the home page and selects All recipes                      | Load page showing all recipes.                                   |
| User filters out allergen recipes.                                           | Only the recipes without allergens are shown.                    |
| User cooks the recipe and clicks the like icon.                              | The number of upvotes is increased by the number of clicks.      |
| User selects edit recipe.                                                    | User is shown form to edit recipe, prefilled with existing text. |
| User edits recipe.                                                           | Recipe entry on database edited with new details.                |
| User clicks add recipe.                                                      | User shown form to populate details of new recipe.               |
| User saves recipe.                                                           | New recipe added to database and redirected to the front page.   |


## Deployment

To deploy the project on Heroku:

1. Add Procfile to tell Heroku it is a web app and to run the run.py script:

```web: python app.py```

2. Connected Heroku to the github repo.

3. Add config vars for IP 0.0.0.0 and PORT 5000.


To run locally:

1. Install python3
   On the command line install HomeBrew
   ```$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

   Then 
   ```$ brew install python```

2. Get pip if not already installed
```$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
Then
```$ python get-pip.py```

3. Use pip to install Flask
   ```pip install Flask```

4. Then run Flask with 
```$ FLASK_APP=app.py FLASK_DEBUG=1 flask run```

