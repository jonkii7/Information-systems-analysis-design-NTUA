import matplotlib.pyplot as plt
import pandas as pd

throughput = [['100000'], ['1000000'], ['7000000']]

i=0

for workload in "B", "C", "E", "A":
    for records in "100000", "1000000", "7000000":
      a = f"./drive/MyDrive/mongodb/mongo_Workload{workload}/singleInstance_wl"
      b = "_load_"
      c = "Rec.txt"
      fileToOpen = a + workload + b + records + c
      f = open(fileToOpen, "r")
      content = f.read()
      w = content[content.find("[OVERALL], Throughput(ops/sec), ")+len("[OVERALL], Throughput(ops/sec), "):content.rfind("[INSERT], Operations,")]
      y = float(w)
      f.close()
      throughput[i].append(y)
      i= i + 1
      if(i>2):
        i=0
df = pd.DataFrame(throughput,columns=['Operations', 'Workload B', 'Workload C', 'Workload E', 'Workload A'])
df.plot(x='Operations',
        kind='bar',
        stacked=False,
        title=f'Single Instance MongoDB, Loading Phase: Throughput-Operations Diagram')
plt.ylabel("Throuput ops/sec")
throughput = [['100000'], ['1000000'], ['7000000']]