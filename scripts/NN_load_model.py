import os
import sys
import pandas as pd
import numpy as np
import argparse
import tensorflow as tf
from tensorflow.python.keras import layers
from tensorflow.python.keras import models

def model_prediction(input_file,work_dir):
    load_model=models.load_model("/fastzone/soft/MD_classification/data/MD_model")
    df_merge=pd.read_csv(input_file,sep="\t",index_col="geneid")
    gene_list=[]
    for i in open(work_dir+"/data/deseq2_selected_genes.txt","r"):
        gene_list.append(i.rstrip())
    gene_list.remove("gene")
    df_select=df_merge.loc[gene_list]
    test_x=np.array(df_select.T)
    prediction=load_model.predict(test_x).tolist()[0]
    subtype=prediction.index(max(prediction))
    if subtype==0:
        MD_type="WNT"
    if subtype==1:
        MD_type="SHH"
    if subtype==2:
        MD_type="Group3"
    if subtype==3:
        MD_type="Group4"
    return(MD_type,prediction[prediction.index(max(prediction))])

parser=argparse.ArgumentParser(description="NN prediction")
parser.add_argument("-i",dest="input_file",help="input_file",required=True)
parser.add_argument("-o",dest="out_dir",help="out_dir",required=True)
args = parser.parse_args()
input_file=args.input_file
out_dir=args.out_dir

if __name__=='__main__':
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    work_dir="/fastzone/soft/MD_classification"
    subtype,ratio=model_prediction(input_file,work_dir)
    out_file=open(out_dir+"/NN_result","w")
    out_file.write("NN_subtype\tNN_ratio\n"+subtype+"\t"+str(ratio)+"\n")
    out_file.close()
