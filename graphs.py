import os
import json
import fnmatch
import matplotlib.pyplot as plt

from shutil import copyfile
from mako.template import Template

graphs = Template(filename='html/graphs_template.html')

with open('report/info.json') as json_file:
    data = json.load(json_file)
    json_file.close()


# graphs

f = open("graphs.html", "w")
f.write(graphs.render(url=data[0]["info"]["url"])
)
f.close()

lvc = []
fp = []
dit = []

for dirpath, dirs, files in os.walk("report/custom"):
  for file in files:
    if fnmatch.fnmatch(file, "*-metric.json"):
      with open(os.path.join(dirpath, file)) as json_file:
        data = json.load(json_file)
        lvc.append(data[0]['visualMetrics']['LastVisualChange'])
        fp.append(data[0]['browserScripts']['timings']['firstPaint'])
        dit.append(data[0]['browserScripts']['timings']['pageTimings']['domInteractiveTime'])

plt.clf()
plt.title('Last Visual Change')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(lvc, bins=500)
plt.savefig("lvc.png")

plt.clf()
plt.title('First Paint')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(fp, bins=500)
plt.savefig("fp.png")

plt.clf()
plt.title('Dom Interactive Time')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(dit, bins=500)
plt.savefig("dit.png")

copyfile("graphs.html", "report/graphs.html")
copyfile("fp.png", "report/fp.png")
copyfile("lvc.png", "report/lvc.png")
copyfile("dit.png", "report/dit.png")
