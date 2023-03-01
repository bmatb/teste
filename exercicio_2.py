import matplotlib.pyplot as plt
import numpy as np
import random
import copy
import statistics as st
import math

def generateMultivariate():
        mean=[3,3]
        cov=[[1,0],[0,1]]
        a=np.random.multivariate_normal(mean,cov,500).T
        mean=[-3,-3]
        cov=[[2,0],[0,5]]
        b=np.random.multivariate_normal(mean,cov,500).T
        c=np.concatenate((a,b),axis=1)
        c=c.T
        np.random.shuffle(c)
        c=c.T
        x=c[0]
        y=c[1]
        return [c ,a, b]
    
def setRandomPoints(c):

        index = np.random.randint(0,len(c[0])-1)
        r1 = [c[0][index], c[1][index]]
        index = np.random.randint(0,len(c[0])-1)
        r2 = [c[0][index],c[1][index]]
        return [r1, r2]
    
def setCloserR1R2toA(r1, r2, a, b, cluster1x, cluster2x):
    distR1toA = math.dist([r1[0], r1[1]], [a[0][0], a[1][0]])
    distR2toA = math.dist([r2[0], r2[1]], [a[0][0], a[1][0]])
    closerR1x = []
    closerR1y = []
    closerR2x = []
    closerR2y = []
    if distR1toA > distR2toA:
        for index, j in enumerate(a[0]):
            if j not in cluster2x:
                 closerR1x.append(a[0][index])
                 closerR1y.append(a[1][index])
        index = 0
        for index, z in enumerate(b[0]):
            if z not in cluster1x:
                 closerR2x.append(b[0][index])
                 closerR2y.append(b[1][index])
    else:
         for index, j in enumerate(a[0]):
            if j not in cluster1x:
                 closerR2x.append(a[0][index])
                 closerR2y.append(a[1][index])
         index = 0
         for index, z in enumerate(b[0]):
            if z not in cluster2x:
                 closerR1x.append(b[0][index])
                 closerR1y.append(b[1][index])
    return [[closerR1x, closerR1y], [closerR2x, closerR2y]]

def plotValues(cluster1, cluster2, r1, r2, closerR1, closerR2):
        labels = ['cluster 1', 'cluster 2', 'Closest R1', 'Closest R2', 'Cons. Values R1', 'Cons. Values R2']
        plt.title("Final values whith R1 and R2 and closest")
        plt.scatter(cluster1[0], cluster1[1], marker = 'x', c="yellow", label = labels[0])
        plt.scatter(cluster2[0], cluster2[1], marker = 'x', c="#0093DC", label = labels[1])
        plt.scatter(closerR1[0], closerR1[1], marker = 'x', c="green", label = labels[2])
        plt.scatter(closerR2[0], closerR2[1], marker = 'x', c="#08007E", label = labels[3])
        plt.scatter(r1[0], r1[1], marker = 'x', c="red", label = labels[4])
        plt.scatter(r2[0], r2[1], marker = 'x', c="red", label = labels[5])
        plt.text(r1[0][-1], r1[1][-1],'R1')
        plt.text(r2[0][-1], r2[1][-1],'R2')
        plt.legend()
        plt.show()
def plotValuesConsecutiveR(cluster1, cluster2, r1, r2, closerR1, closerR2):
        labels = ['cluster 1', 'cluster 2', 'Closest R1', 'Closest R2', 'Cons. Values R1', 'Cons. Values R2']
        plt.title("Consecutive positions of r1 and r2 from begin to end, 30 passages")
        plt.scatter(cluster1[0], cluster1[1], marker = 'x', c="#FEF4A7", label = labels[0])
        plt.scatter(cluster2[0], cluster2[1], marker = 'x', c="#C5FBFF", label = labels[1])
        plt.scatter(closerR1[0], closerR1[1], marker = 'x', c="green", label = labels[2])
        plt.scatter(closerR2[0], closerR2[1], marker = 'x', c="#08007E", label = labels[3])
        plt.scatter(r1[0], r1[1], marker = 'x', c="red", label = labels[4])
        plt.scatter(r2[0], r2[1], marker = 'x', c="red", label = labels[5])
        plt.text(r1[0][0], r1[1][0],'B-R1', c="green")
        plt.text(r2[0][0], r2[1][0],'B-R2', c="green")
        plt.text(r1[0][-1], r1[1][-1],'E-R1', c="#920303")
        plt.text(r2[0][-1], r2[1][-1],'E-R2', c="#920303")
        plt.legend()
        plt.show()
def plotValuesStart(cluster1, cluster2, r1, r2, closerR1, closerR2):
        labels = ['cluster 1', 'cluster 2', 'Closest R1', 'Closest R2', 'Cons. Values R1', 'Cons. Values R2']
        plt.title("Firts passage values whith R1 and R2 and closest")
        plt.scatter(cluster1[0], cluster1[1], marker = 'x', c="yellow", label = labels[0])
        plt.scatter(cluster2[0], cluster2[1], marker = 'x', c="#0093DC", label = labels[1])
        plt.scatter(r1[0], r1[1], marker = 'x', c="red", label = labels[4])
        plt.scatter(r2[0], r2[1], marker = 'x', c="red", label = labels[5])
        plt.text(r1[0], r1[1],'R1')
        plt.text(r2[0], r2[1],'R2')
        plt.legend()
        plt.show()
        


def kMeans(r, c, a, b):
    r1 = r[0]
    r2 = r[1]
    alpha = 50E-3
    passage = 0
    consecutiveR1x = []
    consecutiveR1y = []
    consecutiveR2x = []
    consecutiveR2y = []
    while passage < 30:
        passage +=1
        cluster1x = []
        cluster1y = []
        cluster2x = []
        cluster2y = []
        dAx = 0
        dAy = 0
        dBx = 0
        dBy = 0
        for  index, x in enumerate(c[0]):
            dist1 = math.dist([c[0][index], c[1][index]], [r1[0], r1[1]])
            dist2 = math.dist([c[0][index], c[1][index]], [r2[0], r2[1]])
            if dist1 < dist2:
              dAx += c[0][index] - r1[0]
              dAy += c[1][index] - r1[1]
              cluster1x.append(c[0][index])
              cluster1y.append(c[1][index])
            else: 
              cluster2x.append(c[0][index])
              cluster2y.append(c[1][index])
              dBx += c[0][index] - r2[0]
              dBy += c[1][index] - r2[1]
        r1[0] += (alpha / len(cluster1x)) * dAx
        r1[1] += (alpha / len(cluster1y)) * dAy
        r2[0] += (alpha / len(cluster2x)) * dBx
        r2[1] += (alpha / len(cluster2y)) * dBy
        consecutiveR1x.append(r1[0])
        consecutiveR1y.append(r1[1])
        consecutiveR2x.append(r2[0])
        consecutiveR2y.append(r2[1])
        setCR1toR2 = setCloserR1R2toA(r1, r2, a, b, cluster1x, cluster2x)
        if passage == 1:
            plotValuesStart([cluster1x, cluster1y], [cluster2x, cluster2y], r1, r2, [setCR1toR2[0][0],setCR1toR2[0][1]], [setCR1toR2[1][0],setCR1toR2[1][1]])
    plotValuesConsecutiveR([cluster1x, cluster1y], [cluster2x, cluster2y], [consecutiveR1x, consecutiveR1y], [consecutiveR2x, consecutiveR2y], [setCR1toR2[0][0],setCR1toR2[0][1]], [setCR1toR2[1][0],setCR1toR2[1][1]])      
    plotValues([cluster1x, cluster1y], [cluster2x, cluster2y], [consecutiveR1x, consecutiveR1y], [consecutiveR2x, consecutiveR2y], [setCR1toR2[0][0],setCR1toR2[0][1]], [setCR1toR2[1][0],setCR1toR2[1][1]])
    
gMVariable = generateMultivariate()
kMeans(setRandomPoints(gMVariable[0]), gMVariable[0], gMVariable[1], gMVariable[2])
         
        


#        
