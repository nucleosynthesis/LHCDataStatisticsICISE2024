import pandas as pd

def histogramToDataframe(weights,channel,process,sys='nominal'):
    
    df = {'channel':[],'process':[],'systematic':[],'bin':[],'sum_w':[],'sum_ww':[]}
    nbins = len(weights)
    df['bin']=range(nbins)
    df['channel']=[channel for i in range(nbins)]
    df['process']=[process for i in range(nbins)]
    df['systematic']=[sys for i in range(nbins)]
    df['sum_w']=list(weights)
    df['sum_ww']=list(weights)
    ret = pd.DataFrame.from_dict(df)
    return ret
