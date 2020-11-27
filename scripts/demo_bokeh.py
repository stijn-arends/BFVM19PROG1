#import
from bokeh.models import Select, ColumnDataSource
from bokeh.plotting import figure
from numpy.random import random, normal, lognormal

#create data
source = ColumnDataSource(data = {'x':random(500), 'y':random(500)})

#create plot
p =figure()
p.circle(x='x', y='y', source=source)

#create widget
menu = Select(options=['uniform', 'normal', 'lognormal'], value='uniform',
       title = 'select distribution of your choice')

def callback(attr, old, new):
    if menu.value == 'uniform': f = random
    elif menu.value == 'normal': f = normal
    else: f = lognormal
    source.data={'x': f(size=500), 'y': f(size=500)}


menu.on_change('value', callback)

# Arrange plots and widgets in layouts
from bokeh.io import curdoc
from bokeh.layouts import column
layout = column(menu, p)
curdoc().add_root(layout)
