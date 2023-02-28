#!/bin/bash

#Load Phase for Workload B
for records in 100000 500000 1500000
do
  ./bin/ycsb load mongodb -s -P workloads/workloadb -p recordcount="${records}" -p mongodb.url=mongodb://localhost:29999/ycsb?w=0 | grep  -e "\[OVERALL\]" -e "\[INSERT\]"  > mongo3Shards_wlB_load_"${records}"Rec.txt
done

#Run Phase for Workload B
for threads in 1 2 4 16 48 96
do
  for ops in 10000 100000 300000 1000000 1500000
  do
    ./bin/ycsb run mongodb -s -P workloads/workloadb -threads "${threads}" -p operationcount="${ops}"  -p mongodb.url=mongodb://localhost:29999/ycsb?w=0 | grep -e "\[OVERALL\]" -e "\[SCAN\]" -e "\[READ\]" -e "\[UPDATE\]" -e "\[INSERT\]" > mongo3Shards_wlB_run_"${threads}"Thr_"${ops}"Ops.txt
  done
done
