import numpy as np
from app import findpeaks as fp


def BOP_extractPeaks(data,ppm,topn,verbose):

 """
    Extract ntop peaks from the traces.

    :param data: D x L matrix (traces are per raw), containing D traces each long L points
    :param ppm: 1 x L vector, containing location
    :param topn: number of peaks to retain from every trace
    :param verbose: display some information
    :return:

    """
 raw, column  = np.shape(data)

 peaksHe =  np.zeros((raw,topn),dtype=float)
 peaksPpm = np.zeros((raw,topn),dtype=float)

 if verbose==1 :
     print("Extracting peaks...")

 for i in range(0,raw):
    trace=data[i, :]
    pks,locs = fp.findpeaks(trace)
    pks=np.array(pks)

    sortP = np.sort(pks)
    sortP = sortP[::-1]
    sortNdx= np.argsort(pks)
    sortNdx= sortNdx[::-1]

    peaksHe[i,:]=sortP[0:topn]
    temp2 = []

    for j in range(0, topn):
         index = sortNdx[j]
         temp = locs[index]
         # per ppm lista
         #temp2.insert(j,ppm[temp])
         # per ppm np array
         temp2.insert(j, ppm[0, temp])
    peaksPpm[i,:] = temp2
 if verbose==1 :
    print("done")

 return peaksHe, peaksPpm

"""
 if verbose == 1:
     print("Extracting peaks from", i, "trace")
     plt.plot(ppm, trace.reshape(1, column))
     plt.plot(peaksPpm[i, :], peaksHe[i, :], 'ro')
"""