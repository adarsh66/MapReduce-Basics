#!/bin/bash

#variables
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/matrixSmall.txt
OUT_DIR=$HDP_DIR/output
LOCAL_DIR=./

rm -R ./output
hdfs dfs -rm -R $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapMatrixInv.py \
 -file mapMatrixInv.py \
 -reducer reduceMatrixInv.py \
 -file reduceMatrixInv.py \
 -jobconf mapred.reduce.tasks=2 \
 -jobconf stream.num.map.output.key.fields=2 \
 -jobconf num.key.fields.for.partition=1 \
 -jobconf mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
 -jobconf mapred.text.key.comparator.options='-k1n -k2n' 

hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR

echo "Done. check local output directory"
