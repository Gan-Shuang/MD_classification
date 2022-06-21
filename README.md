# Medulloblastoma(MD) classification
Medulloblastoma(MD) subtype classification toolkit
 
## Introduction
Medulloblastoma(MD) subtype is a indicator of clinical prognosis.Previous researchs classified MD subtypes by hierarchical clustering of microarray or rna-seq(WNT,SHH,Group3,Group4). \
\
This toolkit provide two strategies : Hierarchical clustering & Neural networks \
\
Train datas were downloaded from GSE151519 and GSE164677(total 53 samples were used).With 493 DEG(qadj<0.005,log2foldchange>2) feature were seleted by Deseq2,those feature had best HC performance.

## Install
### build singularity evironment 
Reqired R tools and tensorflow in this env 
```
cd MD_classification
singularity build cluster_tensorflow.sif docker://ganshuang0925/cluster_tensorflow
```
### Trian model
```  
cd scripts
singularity exec ../cluster_tensorflow.sif python3 train_model.py
```

## Method
```
python3 run_MD_classification.py -h
usage: run_MD_classification.py [-h] -i INPUT_FILE -o OUT_DIR
MD prediction
optional arguments:
  -h, --help     show this help message and exit
  -i INPUT_FILE  input_file
  -o OUT_DIR     out_dir
```
## Test
```
cd MD_classificationcd  
python3 ./run_MD_classification.py -i ./test/test_result_FPKM -o ./test/output/
```
## Result
> Cluster_result \
|Hierarchical clustering result,Cluster_ratio=samples of same type in this cluster/samples of all type in this cluster
```
Cluster_subtype	Cluster_ratio
Group3	0.9
```
> NN_result \
|Neural networks result,NN_ratio was calculated by softmax method.
```
NN_subtype	NN_ratio
Group3	0.9998830556869507
```

