from flask_app import app
from flask import render_template, redirect
from flask_app.models.user import User

@app.get("/routines/templates/retrieve")
def building_routines_intro():
    """
    Render the introductory routine-building page for authenticated users.

    Route: /routines/templates/retrieve

    This page introduces users to the process of building a personal routine using 
    pre-built templates or customized selections.

    Returns:
        - Redirects to login if no user is authenticated.
        - Renders the routine introduction template if the user is logged in.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    return render_template("/routines/building_routines_intro.html")
