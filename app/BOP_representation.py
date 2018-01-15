import numpy as np
import numpy.matlib as m

import warnings
warnings.filterwarnings("ignore")

def BOP_representation(peaksHe,peaksPpm,peakDict):

    """
    BOP derive the Bag of Peaks representation

    :param peaksHe:     D x topn matrix: heights of topn peaks to be represented
    :param peaksPpm:    D x topn matrix: location of topn peaks to be represented
    :param peakDict:    vector nPx1 containing the location of the nP peaks of the Dictionary
    :return: BOP:       D x nP matrix containing the Bag of Peaks representation
    """

    peaksHe = np.matrix(peaksHe,dtype=float)
    peaksPpm = np.matrix(peaksPpm,dtype=float)
    peakDict = np.matrix(peakDict,dtype=float)

    nel = np.size(peaksHe, axis=0)
    topn = np.size(peaksHe, axis=1)

    peakDict = np.reshape(peakDict,(10,1))
    nWDict = len(peakDict)

    BOP = np.zeros((nel, nWDict),dtype=float)
    BOP = np.matrix(BOP,dtype=float)

    for i in range(0, nel):
        p = peaksPpm[i,:]
        d = np.absolute(m.repmat(peakDict,1,topn) - m.repmat(p,nWDict,1))
        pd = np.argmin(d,axis=0)
        h = peaksHe[i,:]
        h = h / np.max(h,axis=1)
        xBP = np.zeros((1,nWDict))

        for j in range(0, nWDict):
            z = np.argwhere(pd == j)
            indici = z[:, 1]
            s = 0
            for idx in indici:
                s = s + h[0, idx]
            xBP[0,j] = s

        BOP[i,:] = xBP

    return BOP

