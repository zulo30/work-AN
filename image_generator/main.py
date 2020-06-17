import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.ticker

from data import x, y, xpi, ypi, xpf, ypf, coeff

FONT = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 20}

IMAGE_FILE = "Figura1.png"
IMAGES_DIRECTORY =  os.path.normpath(os.path.join(os.getcwd(),"..","images"))
IMAGE_PATH = os.path.join(IMAGES_DIRECTORY, IMAGE_FILE)


coeff = np.array(coeff)


def get_axes_of_turtle_image():
    ## configure the font for the labels on figure 
    matplotlib.rc('font', **FONT)

    fig = plt.figure(figsize=(20,20))
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
   plt.show()

def make_figure_three():
    ax = get_axes_of_turtle_image()
    ax.plot(x,y,'ro-',markersize=15, linewidth = 5)
    plt.show()

def make_figure_four():
    ax = get_axes_of_turtle_image()
    draw_red_dot(ax,-13.4,1.3)
    draw_red_dot(ax, 10, 1.6)
    draw_blue_line(ax, xpi, ypi)
    draw_blue_line(ax, xpf, ypf)
    plt.show()


def make_figure_eight():
    ax = get_axes_of_turtle_image()
    ax.plot(x,y,'ro-',markersize=15, linewidth = 5)
    spline_y = get_spline_y()
    spline_x = np.arange(-13.4, 10.1, 0.1)
    ax.plot(spline_x,spline_y,'b-', linewidth = 5)
    plt.savefig(os.path.join(IMAGES_DIRECTORY,"Figura8.png"))

def get_spline_y():
    count = x[0]

    spline_y = np.empty(0)
    for i in range(0,25):
        limit = x[i+1]
        while count < limit:
            value = (coeff[i,3]*(count-x[i])**3)+(coeff[i,2]*(count-x[i])**2)+(coeff[i,1]*(count-x[i]))+(coeff[i,0])
            spline_y  = np.append(spline_y, value)
            count+=0.1
    return spline_y

def draw_blue_line(axes,x_coordenates,y_coordenates):
    axes.plot(x_coordenates, y_coordenates,'bo-',markersize=15, linewidth = 1)

def draw_red_dot(axes,x_coordenates,y_coordenates):
    axes.plot(x_coordenates, y_coordenates,'ro',markersize=15, linewidth = 5)


def main():
    print("successful ...!")
    make_figure_eight()

if __name__ == "__main__":
    main()