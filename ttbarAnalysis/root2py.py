import ROOT 
import numpy as np 

def readData(g):
  retX = []
  retY = []
  retYU = []
  retYL = []

  for i in range(g.GetN()):
    retX.append(g.GetX()[i])
    retY.append(g.GetY()[i])
    retYU.append(g.GetErrorYhigh(i))
    retYL.append(g.GetErrorYlow(i))

  return np.array(retX),np.array(retY),np.array(retYL),np.array(retYU)

def readHist(h):

  retX = []
  retY = []
  errY = []
    
  for i in range(1,h.GetNbinsX()+1):
    retX.append(h.GetBinLowEdge(i))
    retY.append(h.GetBinContent(i))
    errY.append(h.GetBinError(i))

  retX.append(h.GetBinLowEdge(h.GetNbinsX()+1))
  
  return np.array(retX),np.array(retY),np.array(errY)

def getHistogramCountsAndData(folder):
    total = readHist(folder.Get("total"))
    data  = readData(folder.Get("data"))
    
    histograms = {
        "data"    : data
        ,"total"  : total
        ,"samples": []
    }
    
    contributions = folder.GetListOfKeys()
    for c in contributions: 
        if "total" in c.GetName(): continue
        if "data"  in c.GetName(): continue 
        else : 
            obj = c.ReadObj()
            histograms['samples'].append([c.GetName(),readHist(obj)])

    return histograms