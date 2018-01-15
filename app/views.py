from django.shortcuts import render,HttpResponseRedirect, redirect
from app.models import BOP ,PLSA
from .forms import BopForm , PlsaForm
from django.http import HttpResponse
import numpy as np
from app.BOP_main import main
import scipy.io as sy
import sys
import os
import shutil

def home(request):
    return render(request,'app/home.html', {})


def guide(request):
    return render(request, 'app/guide.html', {})


def contact(request):
    return render(request, 'app/contact.html', {})


def Bop(request):
    if request.method == "POST":

        topn = request.POST['topn']

        DictSize = request.POST['DictSize']

        data = request.FILES['data']
        ppm = request.FILES['ppm']
        try :
            U = BOP(topn=topn, DictSize=DictSize, data=data, ppm=ppm)
            U.save()

            topn=int(topn)
            DictSize=int(DictSize)

            folderId= U.pk
            folderId= str(folderId)
            newpath = "/home/marco/Scrivania/server/app/static/app/Img/BOP/"
            if os.path.exists("/home/marco/Scrivania/server/app/static/app/Img/BOP/"):
                shutil.rmtree("/home/marco/Scrivania/server/app/static/app/Img/BOP/")
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            print("ciao")
            data = sy.loadmat(U.data.path)
            print("ciao2")

            #data = sy.loadmat('/home/marco/Scrivania/server/media/uploads/data.mat') #anche ppm
            data = data['data']
            data = np.array(data, dtype=float)

            ppm = sy.loadmat(U.ppm.path)
            ppm = ppm['ppm']
            ppm = np.array(ppm)
            HttpResponseRedirect('/resultTemp')
            os.remove("/home/marco/Scrivania/server/media/uploads/data.mat") #immagine salvata
            os.remove("/home/marco/Scrivania/server/media/uploads/ppm.mat")
            prog=1
            print("ciao")
            main(topn,DictSize,data,ppm,newpath,-1,prog)
        except :
            print(sys.exc_info()[0])
            return render(request, 'app/invalid.html', {})

        #return redirect('result')
        files = os.listdir(newpath)
        files.sort()
        files=files[1:]
        print(files)
        path="/app/Img/"+folderId+'/'
        return render(request, 'app/result.html', {'files': files},{'path':path})

    else:
        form = BopForm()

    return render(request, 'app/BOP.html', {'form': form})


def result(request):
    files=os.listdir("/home/marco/Scrivania/server/app/static/app/Img/BOP/")
    return render(request, 'app/result.html', {'files':files})


def invalid(request):
    return render(request,'app/invalid.html', {})


def resultTemp(request):
    return render(request, 'app/resultTemp.html', {})

def Plsa(request):
    if request.method == "POST":
        topic= request.POST['topic']
        topn = request.POST['topn']

        DictSize = request.POST['DictSize']

        data = request.FILES['data']
        ppm = request.FILES['ppm']
        try:
            U = PLSA(topic=topic, topn=topn, DictSize=DictSize, data=data, ppm=ppm)
            U.save()
            print("ciao")
            topic=int(topic)
            topn = int(topn)
            DictSize = int(DictSize)
            print("ciao")
            folderId = U.pk
            folderId = str(folderId)
            newpath = "/home/marco/Scrivania/server/app/static/app/Img/PLSA/"
            if os.path.exists("/home/marco/Scrivania/server/app/static/app/Img/PLSA/"):
                shutil.rmtree("/home/marco/Scrivania/server/app/static/app/Img/PLSA/")
            if not os.path.exists(newpath):
                os.makedirs(newpath)

            data = sy.loadmat(U.data.path)
            data = data['data']
            data = np.array(data, dtype=float)

            ppm = sy.loadmat(U.ppm.path)
            ppm = ppm['ppm']
            ppm = np.array(ppm)
            print("ciao")
            HttpResponseRedirect('/resultTemp')

            os.remove("/home/marco/Scrivania/server/media/uploads/data.mat")
            os.remove("/home/marco/Scrivania/server/media/uploads/ppm.mat")
            print("ciao")
            prog=2

            main(topn, DictSize, data, ppm, newpath,topic,prog)

        except:
            print(sys.exc_info()[0])
            return render(request, 'app/invalid.html', {})

        # return redirect('result')
        files = os.listdir(newpath)
        files.sort()
        files = files[1:]
        print(files)
        return render(request, 'app/resultPLSA.html')

    else:
        form = PlsaForm()

    return render(request, 'app/BOP.html', {'form': form})


def resultPLSA(request):
    return render(request, 'app/resultPLSA.html')