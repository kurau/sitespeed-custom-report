import os
import json
import fnmatch

from shutil import copyfile
from mako.template import Template

diff_data = []
template_data = {}

# detailed_parallels_runs.py
# name, link, min, med, avg, percentile, max

def row(i):
    val1 = dataNew[i]
    val2 = dataOld[i]

    if (val1[0] != val2[0]):
        print("data not correspond " + val1[0] + " and " + val2[0])

    mark = "background-color: #ff9c9c;"
    diff = abs(val1[3]-val2[3])
    if (val1[3] < val2[3]):
        mark = "background-color: #9cffa3;"
    diff_data.append([val1[0], val1[1], val1[3], val2[3], diff, mark])
    print([val1[0], val1[1], val1[3], val2[3], diff, mark])

diff = Template(filename='html/diff_template.html')


with open('report/old/detailed_data.json') as json_file:
    dataOld = json.load(json_file)
    json_file.close()

with open('report/new/detailed_data.json') as json_file:
    dataNew = json.load(json_file)
    json_file.close()

with open('report/old/1-metric.json') as json_file:
    urlOld = json.load(json_file)
    json_file.close()

with open('report/new/1-metric.json') as json_file:
    urlNew = json.load(json_file)
    json_file.close()

if (len(dataOld) == len(dataNew)):
    for i in range(len(dataOld)):
        row(i)


f = open("diff.html", "w")
f.write(diff.render(
    rows=diff_data,
    url1=urlNew[0]["url"],
    url2=urlOld[0]["url"]
    )
)
f.close()

copyfile("diff.html", "report/diff.html")
copyfile("html/index.min.css", "report/index.min.css")
copyfile("html/help.html", "report/help.html")
