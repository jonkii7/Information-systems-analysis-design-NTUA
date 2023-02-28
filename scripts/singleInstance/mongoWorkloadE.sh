#!/bin/bash

#Load Phase for Workload E
for records in 100000 1000000 7000000
do
  ./bin/ycsb load mongodb -s -P workloads/workloade -p recordcount="${records}" -p mongodb.url=mongodb://localhost:27017/ycsb?w=0 | grep  -e "\[OVERALL\]" -e "\[INSERT\]"  > singleInstance_wlE_load_"${records}"Rec.txt
done

#Run Phase for Workload E
for threads in 4 16 48 96
do
  for ops in 10000 100000 300000 1000000
  do
    ./bin/ycsb run mongodb -s -P workloads/workloade -threads "${threads}" -p operationcount="${ops}"  -p mongodb.url=mongodb://localhost:27017/ycsb?w=0 | grep -e "\[OVERALL\]" -e "\[SCAN\]" -e "\[READ\]" -e "\[UPDATE\]" -e "\[INSERT\]" > singleInstance_wlE_run_"${threads}"Thr_"${ops}"Ops.txt
  done
done
