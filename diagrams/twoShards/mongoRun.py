import matplotlib.pyplot as plt
import pandas as pd

#Throughput-Operations Diagrams
throughput = [['10000'], ['100000'], ['300000'], ['1000000'], ['1500000']]
i=0
for threads in "1","2","4","16","48","96":
  for workload in "B", "C", "E", "A":
    for ops in "10000", "100000", "300000", "1000000", "1500000":
      a = f"./drive/MyDrive/mongodb2Shards/mongo2Shards_Workload{workload}/mongo2Shards_wl"
      b = "_run_"
      c = "Thr_"
      d = "Ops.txt"
      fileToOpen = a + workload + b + threads + c + ops + d
      try:
        f = open(fileToOpen, "r")
      except:
        f.close()
        y=float(0)
        throughput[i].append(y)
        i= i + 1
        if(i>4):
          i=0
        continue
      content = f.read()
      try:
        w = content[content.find("[OVERALL], Throughput(ops/sec), ")+len("[OVERALL], Throughput(ops/sec), "):content.rfind("[READ], Operations,")]
        y = float(w)
      except ValueError:
        w = content[content.find("[OVERALL], Throughput(ops/sec), ")+len("[OVERALL], Throughput(ops/sec), "):content.rfind("[INSERT], Operations,")]
        y = float(w)
      f.close()
      throughput[i].append(y)
      i= i + 1
      if(i>4):
        i=0=
  df = pd.DataFrame(throughput,columns=['Operations', 'Workload B', 'Workload C', 'Workload E', 'Workload A'])

  df.plot(x='Operations',
        kind='bar',
        stacked=False,
        title=f'Two Shards MongoDB, {threads} Thread: Throughput-Operations Diagram')
  plt.ylabel("Throughput ops/sec")
  throughput = [['10000'], ['100000'], ['300000'], ['1000000'], ['1500000']]

#Latency-Operations Diagrams
latency = [['10000'], ['100000'], ['300000'], ['1000000'], ['1500000']]
i=0
for threads in "1","2","4","16","48","96":
  for workload in "B", "C", "E", "A":
    for ops in "10000", "100000", "300000", "1000000", "1500000":
      a = f"./drive/MyDrive/mongodb2Shards/mongo2Shards_Workload{workload}/mongo2Shards_wl"
      b = "_run_"
      c = "Thr_"
      d = "Ops.txt"
      fileToOpen = a + workload + b + threads + c + ops + d
      try:
        f = open(fileToOpen, "r")
      except:
        f.close()
        y=float(0)
        latency[i].append(y)
        i= i + 1
        if(i>4):
          i=0
        continue
      content = f.read()
      if(workload == "A"):
        avg1 = content[content.find("[READ], AverageLatency(us), ")+len("[READ], AverageLatency(us), "):content.rfind("\n[READ], MinLatency(us),")]
        
        avg2 = content[content.find("[UPDATE], AverageLatency(us), ")+len("[UPDATE], AverageLatency(us), "):content.rfind("\n[UPDATE], MinLatency(us),")]
        xa = float(avg1)
        xb = float(avg2)
        w = (xa + xb)/2
        y = float(w)
        f.close()
        latency[i].append(y)
        i= i + 1
        if(i>4):
          i=0
        continue
      
      try:
        w = content[content.find("[READ], AverageLatency(us), ")+len("[READ], AverageLatency(us), "):content.rfind("[READ], MinLatency(us),")]
        y = float(w)
      except ValueError:
        w = content[content.find("[SCAN], AverageLatency(us), ")+len("[SCAN], AverageLatency(us), "):content.rfind("[SCAN], MinLatency(us),")]
        y = float(w)
      f.close()
      latency[i].append(y)
      i= i + 1
      if(i>4):
        i=0
  df = pd.DataFrame(latency,columns=['Operations', 'Workload B', 'Workload C', 'Workload E', 'Workload A'])
  
  df.plot(x='Operations',
        kind='bar',
        stacked=False,
        title=f'Two Shards MongoDB, {threads} Thread: Latency-Operations Diagram')
  plt.ylabel("Latency (us)")
  latency = [['10000'], ['100000'], ['300000'], ['1000000'], ['1500000']]