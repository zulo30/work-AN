import os

from sympy.interactive import printing
printing.init_printing(use_latex=True)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.ticker
# from sympy import Piecewise, log, ITE, piecewise_fold
# from sympy.abc import x, y


from data import data

FONT = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 20}

IMAGE_FILE = "Figura1.png"
IMAGES_DIRECTORY =  os.path.normpath(os.path.join(os.getcwd(),"..","assets"))
IMAGE_PATH = os.path.join(IMAGES_DIRECTORY, IMAGE_FILE)

print(data.slope_list[1].y)

data.coeff = np.array(data.coeff)

# count = data.points.x[0]
# funs = []
# conds = []
# for i in range(0,25):
#   limit = data.points.x[i+1]
#   while count <= limit:
#     fun = (data.coeff[i,3]*(x-data.points.x[i])**3)+(data.coeff[i,2]*(x-data.points.x[i])**2)+(data.coeff[i,1]*(x-data.points.x[i]))+(data.coeff[i,0])
#     funs.append(fun)
#     cond = data.points.x[i] < x
#     conds.append(cond)
#     cond = x > data.points.x[i+1]
#     conds.append(cond)
#     count+=1
  

# pieces = []
# for i in range(0,24):
#   piece = (funs[i],conds[2*i])
#   pieces.append(piece)
#   piece = (funs[i],conds[2*i+1])
#   pieces.append(piece)


# pprint(Piecewise(*pieces),use_unicode=False)


def get_axes_of_turtle_image():
    ## configure the font for the labels on figure 
    matplotlib.rc('font', **FONT)

    fig = plt.figure(figsize=(14.86, 6.67), dpi = 72)
    a = fig.add_subplot(1, 1, 1)
    # add the turtle image as background 
    img = mpimg.imread(IMAGE_PATH)
    imgplot = plt.imshow(img[::-1], extent=[-14,13,-4,8], origin='lower')
    # set the corresponding labels 
    a.set_xlabel("x")
    a.set_ylabel("f (x)")

    # we add the ticks and set the grid 
    plt.minorticks_on()
    plt.gca().xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))
    plt.gca().yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))
    plt.grid(which="both", linewidth=0.72,color="c")
    plt.tick_params(which="minor", length=0)

    return plt.gca()


def make_figure_two():
   ax = get_axes_of_turtle_image()
   plt.savefig(os.path.join(IMAGES_DIRECTORY,"Figura2.png"), bbox_inches="tight", dpi = 72)

def make_figure_three():
    ax = get_axes_of_turtle_image()
    ax.plot(data.points.x,data.points.y,'ro-',markersize=12, linewidth = 4)
    plt.savefig(os.path.join(IMAGES_DIRECTORY,"Figura3.png"), bbox_inches="tight", dpi = 72)

def make_figure_four():
    ax = get_axes_of_turtle_image()
    draw_red_dot(ax,-13.4,1.3)
    draw_red_dot(ax, 10, 1.6)
    draw_blue_line(ax, data.slope_list[0].x, data.slope_list[0].y)
    draw_blue_line(ax, data.slope_list[1].x, data.slope_list[1].y)
    plt.savefig(os.path.join(IMAGES_DIRECTORY,"Figura4.png"), bbox_inches="tight", dpi = 72)


def make_figure_eight():
    ax = get_axes_of_turtle_image()
    ax.plot(data.points.x,data.points.y,'ro-',markersize=12, linewidth = 4)
    spline_y = get_spline_y()
    spline_x = np.arange(-13.4, 10.1, 0.1)
    ax.plot(spline_x,spline_y,'b-', linewidth = 4)
    plt.savefig(os.path.join(IMAGES_DIRECTORY,"Figura8.png"), bbox_inches="tight", dpi = 72)

def get_spline_y():
    count = data.points.x[0]

    spline_y = np.empty(0)
    for i in range(0,25):
        limit = data.points.x[i+1]
        while count < limit:
            value = (data.coeff[i,3]*(count-data.points.x[i])**3)+(data.coeff[i,2]*(count-data.points.x[i])**2)+(data.coeff[i,1]*(count-data.points.x[i]))+(data.coeff[i,0])
            spline_y  = np.append(spline_y, value)
            count+=0.1
    return spline_y

def draw_blue_line(axes,x_coordenates,y_coordenates):
    axes.plot(x_coordenates, y_coordenates,'bo-',markersize=12, linewidth = 1)

def draw_red_dot(axes,x_coordenates,y_coordenates):
    axes.plot(x_coordenates, y_coordenates,'ro',markersize=12, linewidth = 4)

def make_(parameter_list):
    pass


def main():
    make_figure_two()
    make_figure_three()
    make_figure_four()
    make_figure_eight()
    print("the images were generated sucessfully ...! ")
    print("you can find them on ../assets")

if __name__ == "__main__":
    main()