from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import ijson
import plotly
import plotly.graph_objs as go
import math

interface = Tk()
interface.minsize(width=300, height=300)


def open_plot_file():
    filename = filedialog.askopenfilename()
    with open(filename, 'r') as f:
        objects = ijson.items(f, 'item')
        columns = list(objects)

    xlist = []
    ylist = []
    for dict in columns:
        xlist.append(0.001 * dict['time_boot_ms'])  # x-axis in graph
        ylist.append(math.sqrt(dict['lon'] * dict['lon'] + dict['lat'] * dict['lat']))  # y-axis in graph

    plotly.offline.plot({
        "data": [go.Scatter(x=xlist, y=ylist)],
        "layout": go.Layout(title="Deviation vs Time")
    })


button = ttk.Button(interface, text="Open JSON File", command=open_plot_file)
button.grid(column=1, row=1)

interface.mainloop()
