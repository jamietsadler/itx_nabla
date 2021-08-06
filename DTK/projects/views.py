# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

blueprint = Blueprint("projects", __name__, url_prefix="/projects", static_folder="../static")

@blueprint.route("/")
def projects():
    """List members."""
    return render_template("projects/projects.html")
