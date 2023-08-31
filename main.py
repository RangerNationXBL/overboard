# Import the good stuff tk and ttk to make some things look good

import tkinter as tk
from tkinter import ttk
import math

###########################################################################
## Most of the comments in this file are from me trying to do more       ##
## I might continue on with the other parts but this works for now       ##
## The goal was to make a triangle calculation and give a representation ##
## of that triangle on screem. Numbers are kinda boring, art is not.     ##
###########################################################################

####################################
## Initalization and Housekeeping ##
####################################

# initialize the things
window = tk.Tk()
window_height = 600
window_width = 800
window.geometry(f'{window_width}x{window_height}')
window.resizable(False, False)
window.title('The triangle')
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

#some safety precautions for error checking.
max_pixel_height = 325
max_pixel_width = 725

# Setting the base and center numbers for calculations
canvas_base = 350
canvas_center = 400
# Triangle basics
base = 600
height = 300
area = 0

## Functions for the thing to work well


def calculate_angle():
  slope = height / (base / 2)
  degrees = math.degrees(math.atan(slope))
  return degrees


#################################
## Canvas and Draw for program ##
#################################

# The canvas to draw in
canvas = tk.Canvas(window, width=795, height=375, bg='black')
canvas.grid(row=0, column=0)
canvas.rowconfigure(0, weight=1)

# Drawing the triangle on screen.

# Orientation discovery text
#canvas.create_text(300, 20, text='top @ 400px but at center --->')
#canvas.create_text(200, 300, text='bottom edge --->', angle=(-90))

# Can't seem to get this to work very well

#hyp_sq = math.sqrt((adjacent / 2) ** 2 + opposite ** 2)
#angle = math.atan((adjacent / 2) / opposite)
#degree = ma#th.degrees(angle)

#angle_1 = math.acos(adjacent / hyp_sq)
#angle_2 = math.acos(opposite / hyp_sq)

#angle_3 = (math.degrees(angle_1) * 2)

#degree_1 = math.degrees(angle_1) * math.degrees(angle_2)
#degree_1 = 180 - angle_2

#canvas.create_text(500, 200, text='< -- angle = ' + str(angle) + ' -- >', angle= (90 - angle))

##################################
## Frame and inputs for program ##
##################################

# The label frame for the inputs
lable_frame = ttk.LabelFrame(window, text='User Input', width=750, height=175)
lable_frame.grid(row=1, column=0, sticky='ewns', padx=10, pady=10)

# Inputs and Labels
base_label = ttk.Label(lable_frame, text='Enter the base', justify='center')
height_label = ttk.Label(lable_frame,
                         text='Enter the height',
                         justify='center')

base_entry = ttk.Entry(lable_frame, name='base', justify='center')
height_entry = ttk.Entry(lable_frame, name='height', justify='center')

# Submit and Reset
submit = ttk.Button(lable_frame, text='Submit', command=lambda: submit())
reset = ttk.Button(lable_frame, text='Reset', command=lambda: reset())

# positioning of things
base_label.grid(row=0, column=0)
height_label.grid(row=1, column=0)
base_entry.grid(row=0, column=1)
height_entry.grid(row=1, column=1)
submit.grid(
    row=3,
    column=0,
)
reset.grid(row=3, column=1)

#################################################
## Functions to make things happen, eventually ##
#################################################


def draw_triangle():
  global area
  area = 0.5 * (int(height) * int(base))
  display_triangle()
  return


def display_triangle():
  canvas.delete('all')
  canvas.create_line(canvas_center, (canvas_base - height),
                     (canvas_center - base / 2), canvas_base)  # A
  canvas.create_line(canvas_center, (canvas_base - height),
                     (canvas_center + base / 2), canvas_base)  # B
  canvas.create_line((canvas_center - base / 2), canvas_base,
                     (canvas_center + base / 2), canvas_base)  # C
  layout_items()
  #canvas.create_line(canvas_center, canvas_base - 20, canvas_center +20, canvas_base - 20)
  #canvas.create_line(canvas_center + 20, canvas_base - 20, canvas_center +20, canvas_base)


def layout_items():
  angle = calculate_angle()
  # Center, the very center of the triangle
  canvas.create_line(400, 0, 400, 375, fill='blue')
  # Base, from where the triangle starts
  canvas.create_line(0, 350, (canvas_center - base / 2), 350, fill='red')
  canvas.create_line((canvas_center + base / 2), 350, 795, 350, fill='red')

  # Text to show some stuff off.
  canvas.create_text(400, (canvas_base - 100),
                     text='<-- Center Line -->',
                     angle=90,
                     fill='yellow')
  canvas.create_text(canvas_center,
                     350,
                     text='<-- Base Line -->',
                     fill='yellow')
  # Data from the calculation
  canvas.create_text(40, 25, text='   Height = ' + str(height))
  canvas.create_text(40, 50, text='   Base = ' + str(base))
  canvas.create_text(40, 75, text='   Area = ' + str(area))
  canvas.create_text(canvas_center + (base / 4),
                     canvas_base - (height / 2),
                     text='Center of Hyp' + str(angle),
                     fill='yellow',
                     angle=90 + (angle))
  canvas.create_text(canvas_center,
                     canvas_base - height,
                     text=str(canvas_base - height) + ' . ' +
                     str(canvas_center),
                     fill='orange')


def submit():
  global base, height
  base = int(base_entry.get())
  height = int(height_entry.get())
  draw_triangle()
  return


# Create a representation of inches in pixels and convert when necessary
# 1 inch is 96 pixels, need to change that just a bit.
def inches_to_px():
  pass


# Error checking, int, float, alpha. Division by zero.
# input to large width or height.
def check_errors(value):
  pass


def reset():
  canvas.delete('all')


#layout_items()
window.mainloop()
