
def findpeaks(trace):
    """
    metodo che ritorna i picchi di un array in pks e la posizione in cui si trovano questi picchi
    :param trace:
    :return:
    """

    pks=[]
    locs=[]


    for i in range(0,len(trace)-1) :
        if i == 0 :
            if trace[i]> trace[i+1] :
                pks.append(trace[i])
                locs.append(i+1)
        elif i > 0 and i < len(trace)-1:
            if trace[i]> trace[i-1] and trace[i] > trace[i+1] :
                pks.append(trace[i])
                locs.append(i+1)
        elif i==len(trace)-1 :
            if trace[i]>trace[i-1] :
                pks.append(trace[i])
                locs.append(i+1)

    return pks,locs