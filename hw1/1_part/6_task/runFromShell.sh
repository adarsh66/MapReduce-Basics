#!/bin/bash

#variables
TASK_ID=6
TASK_DIR=/user/$USER/s1567343_task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/word_pairs
OUT_DIR=$HDP_DIR/output
LOCAL_DIR=./

rm -R output/
hdfs dfs -rm -R $OUT_DIR

#Running the same map and reduce command but reducing to a single reducer.
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapReduce.sh \
 -reducer mapReduce.sh \
 -file mapReduce.sh \
 -jobconf mapred.reduce.tasks=1 \
 -jobconf mapred.job.name="Adarsh'sJob"

hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR
#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR/* $TASK_DIR

echo "Done. check local output directory"
