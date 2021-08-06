mport pandas as pd
import numpy as np
import dateutil
import datetime
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.palettes import Blues4
from bokeh.plotting import figure

def bokeh_plot():
    df = pd.read_csv('DTK/static/data/Glucose.csv', index_col=0)
    df.index = pd.to_datetime(df.index)
    p = figure(x_axis_type="datetime", title="Asset ID", plot_height=300, plot_width=800)
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Value'

    p.line(df.index, df.glucose)
    
    return p

def bokeh_plot_discover():
    df = pd.read_csv('DTK/static/data/Glucose.csv', index_col=0)
    df.index = pd.to_datetime(df.index)
    p = figure(x_axis_type="datetime", title="Asset ID", plot_height=200, plot_width=500)
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Value'

    p.line(df.index, df.glucose)
    
    return p