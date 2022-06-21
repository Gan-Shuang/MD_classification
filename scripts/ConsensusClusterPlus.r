library(optparse)
library(ConsensusClusterPlus)
option_list <- list(make_option("--input",type="character",help = "RNAseq dataframe."),
                    make_option("--outdir",type="character",help = "Output Dir."))
opt <- parse_args(OptionParser(option_list=option_list))
df_file=opt$input
out_dir=opt$outdir
################################
gene_list_file=read.table("/fastzone/soft/MD_classification/data/deseq2_selected_genes.txt",header = T,sep = "\t")
df_data=read.table("/fastzone/soft/MD_classification/data/merge_fpkm.txt",header = T,sep = "\t")
df_sample=read.table(df_file,header = T,sep = "\t")
df=merge(df_data,df_sample,by="geneid")
gene_list=gene_list_file$gene
df_test <- df[which(df$geneid %in% gene_list),]
df_test=df_test[,2:54]
df_test=as.matrix(as.data.frame(lapply(df_test,as.numeric)))
df_test <- na.omit(df_test)
results_pam <- ConsensusClusterPlus(df_test,
                                   maxK = 6,
                                   reps = 50,
                                   pItem = 0.8,
                                   pFeature = 0.8,
                                   clusterAlg = "pam",
                                   distance = "pearson",
                                   title = paste0(out_dir,"/pam"),
                                   plot = "png") 
res=data.frame(results_pam[[4]][["consensusClass"]])
write.table(res,file=paste0(out_dir,"/class_pam"),quote = F,sep="\t",col.names = F)
#write.table(t(df_test),file=paste0(out_dir,"/selected_merge_df.txt"),quote = F,sep="\t",col.names = F)
