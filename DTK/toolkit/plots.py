import pandas as pd
import dateutil
import datetime
import pandas as pd

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from bokeh.io import curdoc

df = pd.read_csv('DTK/static/data/Glucose.csv', parse_dates =[ 'datetime'], index_col = 0, nrows=1000)
df_generation = pd.read_csv('DTK/static/data/generation_data.csv', parse_dates = True)

def bokeh_discover(): 
    p = figure(x_axis_type="datetime", title="Asset ID", sizing_mode='stretch_both', height = 350, width=800, tools="pan,box_zoom,reset", toolbar_location="above")
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Value'
    p.line(df.index, df.glucose)
    p.toolbar.logo = None
    
    return p

def bokeh_discover_2(): 
    p = figure(x_axis_type="datetime", title="Asset ID", sizing_mode='stretch_both', height = 350, width = 350, tools="pan,box_zoom,reset", toolbar_location="above")
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Value'
    p.line(df.index, df.isig)
    p.toolbar.logo = None

    return p

def update_plot(attr, old, new):
    source.data = {
        'x' : df_generation['DATE_TIME'],
        'y' : df_generation[new]
    }

def bokeh_explore():
    source = ColumnDataSource(data={
    'x' : df_generation['DATE_TIME'],
    'y' : df_generation.iloc[:,3]
    })
    plot = figure(width = 800)
    plot.line('x', 'y', source=source)
    select = Select(title="Feature", options=list(df_generation.columns), value=df_generation.columns[3])
    select.on_change('value', update_plot)
    layout = column(select, plot)
    curdoc().add_root(layout)
    
    return layout