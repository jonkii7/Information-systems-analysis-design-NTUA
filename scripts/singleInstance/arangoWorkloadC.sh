#!/bin/bash

#Load Phase for Workload C
for records in 100000 1000000 7000000
do
  ./bin/ycsb load arangodb -s -P workloads/workloadc -p arangodb.ip=127.0.0.1 -p arangodb.port=8529 -p recordcount="${records}" -p arangodb.dropDBBeforeRun=true | grep -e "\[OVERALL\]" -e "\[INSERT\]" > singleArango_wlC_load_"${records}"Rec.txt
done

#Run Phase for Workload C
for threads in 1 2 4 16 48 96
do
  for ops in 10000 100000 300000 1000000 1500000
  do
    ./bin/ycsb run arangodb -s -P workloads/workloadc -threads "${threads}" -p operationcount="${ops}"  -p arangodb.ip=127.0.0.1 -p arangodb.port=8529 | grep -e  "\[OVERALL\]"  -e "\[SCAN\]" -e "\[READ\]" -e "\[UPDATE\]" -e "\[INSERT\]" > singleArango_wlC_run_"${threads}"Thr_"${ops}"Ops.txt
  done
done