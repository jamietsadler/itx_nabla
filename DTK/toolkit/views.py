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
    return render_template("dtkbase.html")

@blueprint.route("/dashboard")
def toolkitdashboard():
    """List members."""
    return render_template("toolkit/dashboard.html")

@blueprint.route("/")
def connect():
    """List members."""
    return render_template("toolkit/connect.html")

@blueprint.route("/workflow")
def workflow():
    """List members."""
    return render_template("toolkit/flow.html")
