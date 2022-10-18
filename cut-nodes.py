#!/usr/bin/env python3

import os,sys
import pandas as pd
import numpy as np
import json

def cut_nodes(data,num_nodes):

    # identify inner n nodes based on num_nodes input
    total_nodes = len(data['nodeID'].unique())
    cut_nodes = int((total_nodes - num_nodes) / 2)

    # remove cut_nodes from dataframe
    data = data[data['nodeID'].between((cut_nodes)+1,(num_nodes+cut_nodes))]

    # replace empty spaces with nans
    data = data.replace(r'^\s+$', np.nan, regex=True)

    return data

def main():
    
    # load config.json
    with open('config.json','r') as config_f:
        config = json.load(config_f)
        
    # set input variables
    tractmeasures = pd.read_csv(config['tractmeasures'])
    num_nodes = config['num_nodes']

    # cut nodes
    tractmeasures_cut = cut_nodes(tractmeasures,num_nodes)
    
    # make output directory
    if not os.path.exists('output'):
        os.mkdir('output')
        
    # save cut nodes csv
    tractmeasures_cut.to_csv('./output/tractmeasures.csv',index=False)
    
if __name__ == '__main__':
    main()
