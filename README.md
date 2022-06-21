# Medulloblastoma(MD) classification
Medulloblastoma(MD) subtype classification toolkit
 
## Introduction
Medulloblastoma(MD) subtype is a indicator of clinical prognosis.Previous researchs classified MD subtypes by hierarchical clustering of microarray or rna-seq(WNT,SHH,Group3,Group4). 
This toolkit provide two strategies:Hierarchical clustering and Neural networks,and provide two result.
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
> Cluster_result
```
Cluster_subtype	Cluster_ratio
Group3	0.9
```
> NN_result
```
NN_subtype	NN_ratio
Group3	0.9998830556869507
```

