import numpy as np
from bokeh.plotting import figure, output_file, show

a = np.loadtxt('inputfile.dat')
# prepare some data
x = a[:,0]
y = a[:,1]

# output to static HTML file
output_file("OneDimensional.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)
