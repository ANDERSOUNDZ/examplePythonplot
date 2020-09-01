
from django.shortcuts import render

import matplotlib
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np


# Create your views here.

# def home(request):
#     return render(request,('home.html'))


def home (request):  

    # Ejemplo 1  FUNCIONA NO TOPAR
    # figura, variablederango = plt.subplots()

    # variablederango.set_xlim(1, 20)
    # variablederango.set_ylim(1, 20)
    # variablederango.set_box_aspect(1)

    # Ejemplo 2FUNCIONA NO TOPAR
    # figura, (linea,rango)= plt.subplots(ncols=2, sharey=True)
    # linea.plot([1,0],[0,10])
    # rango.plot([0,10],[0,10])
    #linea.set_box_aspect(1)
    #rango.set_box_aspect(1)

    # Ejemplo 3 NO TOPAR
    # t = np.linspace(0.0, 1.0, 100)
    # s = np.tan(4 * np.pi * t) + 2
    # figura, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
    # ax.plot(t, s)

    # ax.set_xlabel(r'Rango en X', fontsize=8)
    # ax.set_ylabel('Rango en Y', fontsize=8)

    # Ejemplo 4 NO TOPAR
    # x = np.linspace(-10, 10, 1000)
    # y = x**2 + 2*x + 2 
    # figura, ax = plt.subplots()
    # ax.plot(x, y)

    # Ejemplo 5 NO TOPAR
    x = np.linspace(-5,5,4000)
    y = np.sin(x)

    # figura
    figura = plt.figure()
    ax = figura.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    #ax.set_xlabel(r'Rango en X', fontsize=8)
    #ax.set_ylabel('Rango en Y', fontsize=8)

    # plot the function
    plt.plot(x,y, 'g')


    buf= io.BytesIO()
    figura.savefig(buf, format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri= urllib.parse.quote(string)
    return render(request, 'home.html', {'data':uri})


