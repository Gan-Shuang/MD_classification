import os
import sys
import time
import pandas as pd
import numpy as np
import argparse
import multiprocessing
from subprocess import call

def cluster(input_file,out_dir):
    cluster_command=('singularity exec -B /mnt:/mnt,/fastzone:/fastzone /fastzone/soft/MD_classification/cluster_tensorflow.sif Rscript '+work_dir+'/scripts/ConsensusClusterPlus.r '+
                    '--input '+input_file+' '
                    '--outdir '+out_dir)
#     print(cluster_command)
    call(cluster_command,shell=True)
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for i in open(out_dir+"/class_pam","r"):
        i=i.rstrip()
        sample_name=i.split("\t")[0]
        cluster_type=i.split("\t")[1]
        if sample_name.startswith("GSM"):
            sample=sample_name.split("_")[0]
            sample_type=sample_name.split("_")[1]
        if not sample_name.startswith("GSM"):
            sample=sample_name.split("_")[0]
            new_sample=sample
            sample_type=sample
        if cluster_type=="1":
            list1.append(sample_type)
        if cluster_type=="2":
            list2.append(sample_type)
        if cluster_type=="3":
            list3.append(sample_type)
        if cluster_type=="4":
            list4.append(sample_type)
    if new_sample in list1:
        new_sample_type=max(list1,key=list1.count)
        cluster_ratio=(int(list1.count(new_sample_type))/(len(list1)-1))
    if new_sample in list2:
        new_sample_type=max(list2,key=list2.count)
        cluster_ratio=(int(list2.count(new_sample_type))/(len(list2)-1))
    if new_sample in list3:
        new_sample_type=max(list3,key=list3.count)
        cluster_ratio=(int(list3.count(new_sample_type))/(len(list3)-1))
    if new_sample in list4:
        new_sample_type=max(list4,key=list4.count)
        cluster_ratio=(int(list4.count(new_sample_type))/(len(list4)-1))
    return(new_sample_type,cluster_ratio)

def TF_NN(input_file,out_dir):
    NN_command=("singularity exec -B /mnt:/mnt,/fastzone:/fastzone /fastzone/soft/MD_classification/cluster_tensorflow.sif python3 "+work_dir+"/scripts/NN_load_model.py "+
               "-i "+input_file+" "
               "-o "+out_dir)
    call(NN_command,shell=True)

parser=argparse.ArgumentParser(description="MD prediction")
parser.add_argument("-i",dest="input_file",help="input_file",required=True)
parser.add_argument("-o",dest="out_dir",help="out_dir",required=True)
args = parser.parse_args()
input_file=args.input_file
out_dir=args.out_dir

if __name__=='__main__':
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    work_dir="/fastzone/soft/MD_classification"
    sample_type,cluster_ratio=cluster(input_file,out_dir)
    cluster_file=open(out_dir+"/Cluster_result","w")
    cluster_file.write("Cluster_subtype\tCluster_ratio\n"+sample_type+"\t"+str(cluster_ratio)+"\n")
    cluster_file.close()
    TF_NN(input_file,out_dir)
