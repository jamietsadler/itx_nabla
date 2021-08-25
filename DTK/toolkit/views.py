# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    render_template
)

from flask_login import login_required, login_user, logout_user

from bokeh.embed import components
from bokeh.layouts import layout
from .plots import *

import json

from DTK.toolkit.forms import JSONForm

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
    bokeh_script, bokeh_div = components(page_layout)
    return render_template(
        "toolkit/dashboard.html", 
        script=bokeh_script, 
        div=bokeh_div)

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

@blueprint.route("/gojs", methods=['GET', 'POST'])
def gojs():
    """List members."""
    #saved_data = json.loads('data.json') # load saved model
    
    form = JSONForm()
    json_string = str(form.json.data)
    contents = json_string.strip('"')
    contents = contents.replace('\\', '')

    json_data = json.dumps(contents)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(contents, f, ensure_ascii=False, indent=4)

    with open('data.json') as f:
        saved_data = json.load(f)

    return render_template("toolkit/gojs.html", data=saved_data, form = form)
    

@blueprint.route('/dataset')
def data_explore():
    return render_template('toolkit/dataset.html')