#!/bin/bash

#variables
TASK_ID=3
TASK_DIR=/user/$USER/s1567343_task_$TASK_ID.out
HDP_DIR=/user/$USER/data
OUT_DIR=$HDP_DIR/output
INP_FILES=$HDP_DIR/input/duplicated_data
LOCAL_DIR=./

rm -R output/
hdfs dfs -rm -R $OUT_DIR

#reduce to a single task only
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper wc \
 -reducer reducerSumWc.sh \
 -file reducerSumWc.sh \
 -jobconf mapred.reduce.tasks=1 \
 -jobconf mapred.job.name="Adarsh'sJob" 

hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR
#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR/* $TASK_DIR

echo "Done. check local output directory"
