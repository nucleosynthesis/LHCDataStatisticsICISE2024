import pandas as pd

def histogramToDataframe(weights,channel,process,sys='nominal'):
    
    df = {'channel':[],'process':[],'systematic':[],'bin':[],'sum_w':[],'sum_ww':[]}
    nbins = len(weights)+1
    df['bin']=range(nbins)
    df['channel']=[channel for i in range(nbins)]
    df['process']=[process for i in range(nbins)]
    df['systematic']=[sys for i in range(nbins)]
    df['sum_w']=list(weights)+[0] # append 0 to the end as fake overflow bin
    df['sum_ww']=list(weights)+[0] # append 0 to the end as fake overflow bin
    ret = pd.DataFrame.from_dict(df)
    return ret
