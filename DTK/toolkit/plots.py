import pandas as pd
import dateutil
import datetime
import pandas as pd

from bokeh.plotting import figure
from bokeh.embed import components

df = pd.read_csv('DTK/static/data/Glucose.csv', parse_dates =[ 'datetime'], index_col = 0)

def bokeh_discover(): 
    p = figure(x_axis_type="datetime", title="Asset ID", sizing_mode='stretch_both', tools="pan,box_zoom,reset", toolbar_location="above")
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Value'
    p.line(df.index, df.glucose)
    p.toolbar.logo = None
    #p.sizing_mode = 'scale_width'
    
    return p

def bokeh_discover_2(): 
    p = figure(x_axis_type="datetime", title="Asset ID", sizing_mode='stretch_both', tools="pan,box_zoom,reset", toolbar_location="above")
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Value'
    p.line(df.index, df.isig)
    p.toolbar.logo = None
    #p.sizing_mode = 'scale_width'
    
    return p