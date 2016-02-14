#!/bin/bash

#variables
TASK_ID=7
TASK_DIR=/user/$USER/s1567343_task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/matrixLarge.txt
OUT_DIR=$HDP_DIR/output
OUT_DIR_2=$HDP_DIR/output_2
LOCAL_DIR=./

rm -R ./output_2
hdfs dfs -rm -R $OUT_DIR
hdfs dfs -rm -R $OUT_DIR_2

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.reduce.tasks=5 \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=-k1,2 \
 -D mapreduce.partition.keycomparator.options='-k1n -k2n' \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapMatrixInv.py \
 -file mapMatrixInv.py \
 -reducer reduceMatrixInv.py \
 -file reduceMatrixInv.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.reduce.tasks=1 \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D stream.num.map.output.key.fields=1 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=-k1,1 \
 -D mapreduce.partition.keycomparator.options='-k1n' \
 -input $OUT_DIR \
 -output $OUT_DIR_2 \
 -mapper cat \
 -reducer cat


hdfs dfs -copyToLocal $OUT_DIR_2 $LOCAL_DIR
#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR_2/* $TASK_DIR

echo "Done. check local output directory"
