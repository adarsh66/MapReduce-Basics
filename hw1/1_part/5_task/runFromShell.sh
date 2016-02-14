#!/bin/bash

#variables
TASK_ID=5
TASK_DIR=/user/$USER/s1567343_task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/duplicated_data
RE_INP_DIR=$HDP_DIR/input/word_pairs
OUT_DIR=$HDP_DIR/output
LOCAL_DIR=./

rm -R output/
hdfs dfs -rm -R $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapTwoWordsWithCombiner.py \
 -file mapTwoWordsWithCombiner.py \
 -combiner aggregate \
 -reducer aggregate \
 -jobconf mapred.reduce.tasks=50 \
 -jobconf mapred.job.name="Adarsh'sJob"

hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR
hdfs dfs -rm $RE_INP_DIR/*
hdfs dfs -cp $OUT_DIR/part* $RE_INP_DIR
#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR/* $TASK_DIR

echo "Done. check local output directory"
