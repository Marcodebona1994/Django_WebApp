import scipy.spatial.distance as siod
import scipy.cluster.hierarchy as sioh
import numpy as np
import time
import scipy.io as sy

def BOP_buildingDictionary(peaksPpm,DictSize,DictRange,verbose):



    #estrazione di peaksPpm su colonna per poter utilizzare pdist che richiede un vettore colonna
    raw,column =np.shape(peaksPpm)
    num=raw*column

    dataTemp=[]
    for i in range(0,column):
        temp=peaksPpm[:,i]
        temp=temp.tolist()
        dataTemp=dataTemp+temp


    dataTemp=np.array(dataTemp,dtype=float)
    data=dataTemp.reshape(num,1)
    raw, column = np.shape(data)

    # calcolo distaza utilizzando pdist
    Y = siod.pdist(data, metric='euclidean')

    Y = np.array(Y,dtype=float)

    Unic=np.unique(Y)
    print(len(Unic))


    print(len(np.unique(Y)))


    if verbose ==1 :
        print("Clusterin peaks ...")

    Z = sioh.linkage(Y,method='complete')

    if verbose ==1 :
        print("done")

    nW=DictSize;
    if verbose ==1 :
        print("Buildind Dictionary :", nW , "peaks")

    clust=sioh.fcluster(Z,t=nW,criterion="maxclust")

    cluster = []
    time.sleep(0.5)
    for i in range(1, 11):
        cluster.insert(i - 1, sum(clust == i))
    print(cluster)

    print(len(clust))
    nclus =len(set(clust))
    lab = np.array(clust,dtype=float)
    peakDict =[]
    count=0
    for i in range(1,nclus+1):
        l=0
        for k in range(0,len(clust)):

            if i == lab[k]:
                count = count + 1
                l=l+float(data[k])

        med=(l/count)
        count=0
        peakDict.insert(i,med)

    if verbose==1:
        print("done")

    return peakDict