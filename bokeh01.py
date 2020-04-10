from bokeh.plotting import figure, output_file, show
import numpy as np
import urllib3

#pegando dados do Bing
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.bing.com/covid')
data = r..data.decode('utf-8')

#create a matriz
a = np.arange(64).reshape(2,32)

# prepare some data
x = a[0]

y = a[1]
print(x, y)

# output to static HTML file
output_file("/Users/rodsim/Documents/matrizes/templates/lines.html")

# create a new plot with a title and axis labels
p = figure(
   tools="pan,box_zoom,reset,save",
   y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
   x_axis_label='sections', y_axis_label='particles'
)

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="y=10^x", line_color="red")

# show the results
show(p)