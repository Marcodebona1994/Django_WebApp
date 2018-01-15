import numpy as np
import scipy.spatial as sp
import scipy.cluster

def normalize(A):
 W,D = A.shape
 z = A.sum(axis=0)
 #s = z + (z==0); If a document has all zeros, control it beforehand
 M = A / np.tile(z, [W,1]);
 return M

def init(counts,T):
 W,D = counts.shape
 #Init zeros wt
 wt = np.zeros((W,T),dtype=float)
 # Compute pairwise distance matrix
 Y = sp.distance.pdist(np.transpose(counts), 'euclidean')
 print(len(np.unique(Y)))
 U = np.random.rand(len(Y))
 print(np.shape(U))
 U = U / 10000
 #Y = Y + U
 # Generate hierarchy using complete link
 Z = scipy.cluster.hierarchy.linkage(Y,method='complete')
 # Cut the tree so that exactly T clusters are found
 clust = scipy.cluster.hierarchy.fcluster(Z,T,'maxclust')

 print(clust)
 cluster=[]
 for i in range(1, 6):
  cluster.insert(i - 1, sum(clust == i))
 print(cluster)
 # Parse label and average counts
 for i in range(1,T+1,1):
  crit = clust==i
  sub = counts[np.ix_(np.arange(W),crit)]
  tmp = np.mean(sub,axis=1)
  wt[:,i-1] = tmp



 return normalize(wt)


def plsa(counts,T,epsilon,learn):
 #non modificare se non ci son valore negativi
 counts = counts+abs(np.min(counts))
 counts = counts.astype(float)

 W,D = counts.shape
 
 # Initialize p(w|z) and p(z|d)
 wt = init(counts,T)
 td = normalize(np.ones((T,D),dtype=float))



 # Total counts in the document
 tot  = np.sum(counts)
 
 # Initialize variables for the loop
 done = False
 it = 1

 tmp = counts * np.log( np.dot(wt,td) + np.spacing(1) ) 
 E = tmp.sum(axis=0)
 F = np.sum(E) / tot

 # MAIN LOOP
 while not(done):
  it+=1

  tmp = np.dot(wt.transpose(), counts / (np.dot(wt,td) + np.spacing(1)))
  td = normalize(td * tmp)

  if learn:
   tmp = np.dot(counts / (np.dot(wt,td) + np.spacing(1)), td.transpose())
   wt = normalize(wt * tmp)

  tmp = counts * np.log( np.dot(wt,td) + np.spacing(1) ) 
  E = tmp.sum(axis=0)
  F_new = np.sum(E)/tot
  F = np.hstack((F,F_new))

  # Convergence check
  rel_ch = (F[it-1] - F[it-2]) / abs(F[it-2])
  if (rel_ch < epsilon) & ( it > 5 ):
   done=True
 #servono i plot grafici per vedere il risultato della plsa
 return (wt,td,F,it)







