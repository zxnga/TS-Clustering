import math
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster, inconsistent
from scipy import fftpack
from scipy.interpolate import CubicSpline
import time
from fastdtw import fastdtw
from collections import Counter
import matplotlib.pyplot as plt

colormap=np.array(['blue','#d10a3c','#6f7bbb','#3ac467','#c69942','#FF00FF','#DE9816','#87591A','#D473D4','#54F98D','#B3B191'])

def ComputeDtw_Matrix(mat,window=1): #Apply DTW to matrix. Return dissimilarity matrix
    res=np.zeros((mat.shape[0],mat.shape[0]))
    nb=res.shape[0]
    
    for i in range(nb):
        for j in range(i):
            res[i,j]=fastdtw(mat[i],mat[j],window)[0]
            
    return (res+res.T)

def ComputeCurveDerivate_Matrix(DF):#retourne la derivee des series temporelles 
    #r=lignes c=colonnes
    r,c=DF.shape
    #matrice nulle de taille r,
    M_derivate=np.zeros((r,len(np.arange(1,c+1))))
    
    for i in range(0,r):
        cs=CubicSpline(np.arange(1,c+1),DF.values[i])
        M_derivate[i]=cs(np.arange(1,c+1),1)#derivee premiere 

    return pd.DataFrame(M_derivate,columns=np.arange(1,c+1),index=DF.index)

def ComputeDerivativeSpectrum_Matrix(DF): #retourne la matrice des spectres
    r,c=DF.shape
    spectre=np.zeros((r,c))
    
    for i,sensor in enumerate(DF.values):
        #Fast Fourier Transfo        
        spectre[i]=abs(np.fft.fft(sensor))
    return spectre


def get_indice_individus(clust):#renvoie la position des individus de chaque cluster
    return [list(np.where(clust==elem)[0]) for elem in np.sort(list(Counter(clust)))]

#def get_individus(clust,data):#renvoie les individus composants chaque cluster
#    return [data.iloc[list(np.where(clust==elem)[0])].values for elem in np.sort(list(Counter(clust)))]

def get_individus(clust, data):
    dic={}
    for i,classe in enumerate(clust):
        if str(classe) not in dic.keys():
            dic[str(classe)]=[]
        dic[str(classe)].append(data.index[i])

    return (dic) 

def apply_clustering(data,k=2,critere="ward",window=1):
    
    #derivee    
    derivees=ComputeCurveDerivate_Matrix(data)

    #Fourier
    spectres=ComputeDerivativeSpectrum_Matrix(derivees)

    #DTW
    dist=ComputeDtw_Matrix(spectres,window)
    #print(dist)
    
    Z=linkage(dist,critere)
    clus=list(fcluster(Z,k,criterion="maxclust"))
    f=fcluster(Z,k,criterion="maxclust")
    
    return clus,Z,f

def get_dist(data, window=1):
    derivees=ComputeCurveDerivate_Matrix(data)
    spectres=ComputeDerivativeSpectrum_Matrix(derivees)
    dist=ComputeDtw_Matrix(spectres,window)
    return dist
    