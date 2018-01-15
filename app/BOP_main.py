import numpy as np
import scipy.io as sy
from app import BOP_extractPeaks as ex
from app import BOP_buildingDictionary as bd
from app import BOP_representation as rep
import time as time
from app import plsa
import matplotlib.pyplot as plt

"""
    Main of BOP_program

    :param DictSize: desired size of dictionary. if DictSize == -1, then the size is automatically estimated via the Davies Bouldin index
    :param DictRange: vector containing the possible dictionary size (to be investigated in the automatic search)
    :param data: D x L matrix (traces are per raw), containing D traces each long L points
    :param topn: number of peaks to retain from every trace
    :param verbose: display some information

"""


def main(topn,DictSize,data,ppm,newfolder,topic,prog):
    tempoIniziale=time.time()

    #data = data['data']
    #data = np.array(data,dtype=float)

    #ppm = ppm['ppm']
    #ppm = np.array(ppm,dtype=float)
    """
    data = np.genfromtxt('data_csv', delimiter=',')
    data = np.array(data)
    
    ppm = np.genfromtxt('ppm_csv', delimiter=',')
    ppm= np.array(ppm)
    """

    raw,column =np.shape(data)
    verbose=1
    DictRange = np.arange(5,50,2)

    print("BAG OF PEAKS : \n" , "Verbose =",verbose ,"\n", "topn =",topn,"\n", "DictSize =",DictSize)

    """
        ExtractPeaks : Extracting all peaks from all traces
        :param data: data: D x L matrix (traces are per row), containing D traces each long L points
        :param ppm: ppm: 1 x L vector, containing locations
    """

    peaksHe,peaksPpm = ex.BOP_extractPeaks(data, ppm, topn, verbose)

    """
        BOP_BuldingDictionary :   Building Dictionary with 10 entries
    
        :param DictSize: desired size of dictionary. if DictSize == -1, then the size is automatically estimated via the Davies Bouldin index
        :param DictRange: vector containing the possible dictionary size (to be investigated in the automatic search)
        :param verbose: display some information
    """


    peakDict = bd.BOP_buildingDictionary(peaksPpm,DictSize,DictRange,verbose)

    print("PeakDict =",np.round(peakDict,decimals=4))
    """
         BOP_representation : Extract BOP Representation, if traces used to build the dictionary
         are different from those to be represented, use again BOP_extractPeak
    """
    if verbose==1 :
        print("Representation of Dictionary ...")

    BOP=rep.BOP_representation(peaksHe,peaksPpm,peakDict)

    if topic ==-1 :
        plt.imshow(BOP, aspect='auto', interpolation='none', origin='lower')
        plt.colorbar()
        plt.xticks(range(0,DictSize))
        plt.xlabel("Words")
        plt.savefig(newfolder+'BOP.png')
        print("ciao1")
        if(prog==1) :
            for i in range(10):
                plt.imshow(BOP[i,:], aspect='auto', interpolation='none', origin='lower') #chiedere per impostazioni immagini
                k=i+1
                s= repr(k)
                plt.savefig(newfolder+'BOP'+s+'.png')


        if verbose==1 :
            print("done\n", "End of BAG OF PEAKS program")

        tempoFinale=time.time()

        if verbose==1 :
            print("Running time :",tempoFinale-tempoIniziale,"s")
        plt.close()
    #va salvata la matrice BOP in un file(.mat o .txt)
    if topic !=-1 :
        epsilon = 0.000001
        learn=1

        raw,column =np.shape(BOP)

        BOP_plsa=np.zeros((column,raw))

        for i in range(0, raw):
            temp = BOP[i,:]
            BOP_plsa[:,i]=temp

        [wt, td, F,it] = plsa.plsa(BOP_plsa,topic,epsilon,learn)

        # plt.imshow(wt, aspect='auto', interpolation='none', origin='lower')
        # plt.colorbar()
        # plt.xticks(range(0, 10))
        # plt.xlabel("Words")
        # plt.savefig(newfolder + 'BOP.png')
        plt.close()
        wt=np.transpose(wt)
        raw, column = np.shape(wt)
        plt.imshow(wt, aspect='auto', interpolation='none', origin='lower')
        plt.colorbar()
        plt.xticks(range(0,column))
        plt.yticks(range(0,raw))
        plt.savefig(newfolder+'wt.png')

        plt.close()
        td=np.transpose(td)
        raw, column = np.shape(td)
        plt.imshow(td, aspect='auto', interpolation='none', origin='lower')
        plt.colorbar()
        plt.xticks(range(0,column))
        plt.yticks(range(0,raw,5))
        plt.savefig(newfolder+'td.png')
        plt.close()

        # if prog == 3 :
        #     for i in range(raw):
        #         print(td[i,:])
        #         plt.imshow(td[i,:], aspect='auto', interpolation='none', origin='lower') #chiedere per impostazioni immagini
        #         k=i+1
        #         s= repr(k)
        #         plt.savefig('Img/PLSA/td'+s+'.png')







