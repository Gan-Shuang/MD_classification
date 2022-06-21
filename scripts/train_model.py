import os
import sys
import pandas as pd
import numpy as np
import argparse
import tensorflow as tf
from tensorflow.python.keras import layers
from tensorflow.python.keras import models
df=pd.read_csv("/mnt/13d1/ganshuang/MD_classification/deseq2_counts/selected_merge_df.txt",sep="\t",index_col="geneid")
for i in df.index:
    df.loc[i,"type"]=str(i).split("_")[1].replace("WNT","0").replace("SHH","1").replace("Group3","2").replace("Group4","3").replace("FPKM","0")
index_train=list(range(0,52))
index_test=list(range(0,15))
train_df=df.iloc[index_train,:]
test_df=df.iloc[index_test,:]
train_x=np.array(train_df.drop("type",axis=1))
train_y=np.array(train_df["type"]).astype(np.int64)
test_x=np.array(test_df.drop("type",axis=1))
test_y=np.array(test_df["type"]).astype(np.int64)
##############################################
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(493,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(4,activation="softmax")
])

model.compile(optimizer="adam",
              loss='sparse_categorical_crossentropy',
              metrics=['acc'])
history=model.fit(train_x, train_y, epochs=1000)
model.save("/fastzone/soft/MD_classification/data/MD_model")
