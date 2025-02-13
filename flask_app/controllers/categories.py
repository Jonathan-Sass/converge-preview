from flask_app import app
from flask import redirect, jsonify

from flask_app.models.category import Category
from flask_app.models.user import User



@app.get("/api/categories-with-practices/all")
def fetch_all_categories_with_practices():
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")
  
  categories_with_subcats = Category.get_all_categories_with_subcategories()

  return jsonify(categories_with_subcats)

