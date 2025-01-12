from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("You need to be logged in to access this page.", "error")
            return redirect(url_for("user.login"))
        if current_user.role != "admin":
            flash("You do not have permission to access this page.", "error")
            return redirect(url_for("main.home"))
        return f(*args, **kwargs)
    return decorated_function