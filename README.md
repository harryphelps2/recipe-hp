# Recipes App

## Database Design

### Usage Statements

+ As a user want I want to choose a recipe, and buy the ingredients to make it.

+ I want to follow the instructions to make the recipe.

+ I want to know how long it will take me to make it

+ I want to know if it is tasty

+ I want to know if it has any allergens in

+ I want to know if it is spicy.

+ I want to know how long it is going to take

+ I want to recommend a recipe to a friend

### Database contents

#### Recipes collection

1. id

2. Dish: string

3. Number_of_upvotes: int

4. Comments: {username:string, comment: string, recommended: bool}

5. Preparation_time: int

6. Spicy: bool

7. Ingredients: array of bison objects (item: string, amount: string, allergen: bool)
    [{ name: “garlic”, amount: “1 clove”, allergen: false},
    { name: “bread”, amount: “1 loaf”, allergen: false}

8. Steps: [{1: “Add beans”},{ 2: “add toast”}]

### Users collection

1. Username: string

## Setting up

1. Install Flask

`sudo pip3 install flask`
2. Run locally

`FLASK_APP=app.py FLASK_DEBUG=1 flask run`
3. Install heroku

`brew install heroku/brew/heroku`