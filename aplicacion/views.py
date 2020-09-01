
from django.shortcuts import render
# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO


# def home(request):
    
#     return render(request,'home.html')
    
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np


# Create your views here.



# def home(request):
    
    
#     return render(request,('home.html'))




def home (request):  

    #FUNCIONA NO TOPAR
    # figura, variablederango = plt.subplots()

    # variablederango.set_xlim(1, 20)
    # variablederango.set_ylim(1, 20)
    # variablederango.set_box_aspect(1)

    #FUNCIONA NO TOPAR
    # figura, (linea,rango)= plt.subplots(ncols=2, sharey=True)
    # linea.plot([1,0],[0,10])
    # rango.plot([0,10],[0,10])
    #linea.set_box_aspect(1)
    #rango.set_box_aspect(1)


    buf= io.BytesIO()
    figura.savefig(buf, format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri= urllib.parse.quote(string)
    return render(request, 'home.html', {'data':uri})


