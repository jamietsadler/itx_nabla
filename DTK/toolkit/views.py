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

blueprint = Blueprint("toolkit", __name__, url_prefix="/toolkit", static_folder="../static")

@blueprint.route("/")
def dtkhome():
    """List members."""
    return render_template("toolkit/home.html")

@blueprint.route("/dashboard")
def dashboard():
    """List members."""
    return render_template("toolkit/dashboard.html")

@blueprint.route("/connect")
def connect():
    """List members."""
    return render_template("toolkit/connect.html")

@blueprint.route("/workflow")
def workflow():
    """List members."""
    return render_template("toolkit/flow.html")

@blueprint.route("/users")
def project_users():
    """List members."""
    return render_template("toolkit/users.html")

@blueprint.route("/apps")
def project_apps():
    """List members."""
    return render_template("toolkit/apps.html")
