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
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn
import pandas as pd

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

@blueprint.route("/workflow", methods=["GET", "POST"])
def workflow():
    """List members."""
    form = JSONForm()
    if form.validate_on_submit():
        
        json_string = str(form.json.data)
        contents = json_string.strip('"')
        contents = contents.replace('\\', '')

        json_data = json.dumps(contents)

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(contents, f, ensure_ascii=False, indent=4)

    with open('data.json') as f:
        saved_data = json.load(f)

    return render_template("toolkit/flow.html", form=form, data=saved_data)

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

    with open('data.json') as f:
        saved_data = json.load(f)

    json_data = json.dumps(contents)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(contents, f, ensure_ascii=False, indent=4)

    return render_template("gojs.html", data=saved_data, form = form)
    

@blueprint.route('/dataset')
def data_summary():
    return render_template('toolkit/dataset.html')

@blueprint.route('/explore')
def data_explore():
    df = pd.read_csv('DTK/static/data/Glucose.csv',  nrows=1000)
    source = ColumnDataSource(df)
    columns = [
        TableColumn(field="datetime", title="Timestamp"),
        TableColumn(field="glucose", title="Glucose"),
        TableColumn(field="isig", title="isig"),
    ]
    data_table = DataTable(source=source, columns = columns, height = 700, width = 400)

    script, div_dict = components(data_table)

    return render_template('toolkit/data_explore.html', data_table = div_dict, script = script)


@blueprint.route('/charts')
def data_charts():
    df = pd.read_csv('DTK/static/data/generation_data.csv', parse_dates = True, index_col = 0)
    axis = df.columns
    return render_template('toolkit/data_charts.html', axis = axis)

@blueprint.route('/history')
def data_history():
    return render_template('toolkit/data_history.html')
    
@blueprint.route('/settings')
def data_settings():
    return render_template('toolkit/data_settings.html')