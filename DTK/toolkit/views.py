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

from bokeh.embed import components
from bokeh.layouts import layout
from .plots import *

blueprint = Blueprint("toolkit", __name__, url_prefix="/toolkit", static_folder="../static")

@blueprint.route("/")
def dtkhome():
    """List members."""
    return render_template("toolkit/home.html")

@blueprint.route("/dashboard")
def dashboard():
    """List members."""
    plot = bokeh_discover()
    plot2 = bokeh_discover_2()
    plot3 = bokeh_discover()
    page_layout = layout([
        [plot],
        [plot2, plot3]
    ])
    # bokeh_script, bokeh_div = components(plot)
    # bokeh_script_2, bokeh_div_2 = components(plot2)
    bokeh_script, bokeh_div = components(page_layout)
    return render_template(
        "toolkit/dashboard.html", 
        script=bokeh_script, 
        div=bokeh_div,
        # script2=bokeh_script_2,
        # div2=bokeh_div_2
    )

@blueprint.route("/connect")
def jobs():
    """List members."""
    return render_template("toolkit/jobs.html")

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

@blueprint.route("/gojs")
def gojs():
    """List members."""
    return render_template("gojs.html")