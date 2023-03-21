from app import app
from flask import render_template

@app.route('/')
def favorite_foods():
   return render_template('foods.html')

@app.route('/artists')
def favorite_artists():
   return render_template('artists.html')

@app.route('/colors')
def favorite_colors():
   return render_template('colors.html')
