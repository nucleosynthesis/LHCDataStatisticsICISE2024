import ROOT 
import numpy as np 

# Funtion to read data_obs TGraphAsymmErrors from fitDiagnostics.root
# convert to [x],[y],[eyL],[eyU]
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

# Funtion to read TH1F from fitDiagnostics.root
# convert to [x],[y],[ey]
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

# Funtion to Loop through folder (channel) in fitDiagnostics.root
# returns dictionary with data, total and list of samples from folder
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

# Function to read "limit" TTree (tree) which yields 2*deltaNLL vs xvar (default "r")
# returns [x],[2*deltaNLL(x)] sorted in ascending x value
def get2DeltaNLLScan(tree,xvar='r'):
    xvs   = []
    npts = tree.GetEntries()
    for i in range(npts):
        tree.GetEntry(i)
        xvs.append([getattr(tree,xvar),2*tree.deltaNLL])
    xvs.sort()
    return np.array([x[0] for x in xvs]),np.array([x[1] for x in xvs])
