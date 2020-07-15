import os
import json
import fnmatch

from shutil import copyfile
from mako.template import Template

diff_data = []
template_data = {}

def row(name, helpLink, path):
    val1 = data[0]
    val2 = data2[0]
    for node in path:
        val1 = val1[node]
        val2 = val2[node]
    mark = "background-color: #9cffa3;"
    diff = abs(val1-val2)
    if (val1 < val2):
        mark = "background-color: #ff9c9c;"
    diff_data.append([name, helpLink, val1, val2, diff, mark])
    print([name, helpLink, val1, val2, diff, mark])

diff = Template(filename='html/diff_template.html')


with open('report/first/info.json') as json_file:
    data = json.load(json_file)
    template_data["url1"] = data[0]["info"]["url"]
    json_file.close()

with open('report/second/info.json') as json_file:
    data2 = json.load(json_file)
    template_data["url2"] = data2[0]["info"]["url"]
    json_file.close()

row(
 "RUMSpeed Index",
 "help.html#rumSpeedIndex",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "rumSpeedIndex", "median"]
)

row(
 "First Paint",
 "help.html#firstPaint",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "firstPaint", "median"]
)

row(
 "Fully Loaded",
 "help.html#fullyLoaded",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "fullyLoaded", "median"]
)

row(
 "Largest Contentful Paint",
 "help.html#largestContentfulPaint",
 ["statistics", "timings", "largestContentfulPaint", "renderTime", "median"]
)

row(
 "first-contentful-paint",
 "help.html#first-contentful-paint",
 ["statistics", "timings", "paintTiming", "first-contentful-paint", "median"]
)

row(
 "first-paint",
 "help.html#first-paint",
 ["statistics", "timings", "paintTiming", "first-paint", "median"]
)

row(
 "backEndTime",
 "help.html#backEndTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "backEndTime", "median"]
)

row(
 "domContentLoadedTime",
 "help.html#domContentLoadedTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "domContentLoadedTime", "median"]
)

row(
 "domInteractiveTime",
 "help.html#domInteractiveTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "domInteractiveTime", "median"]
)

row(
 "domainLookupTime",
 "help.html#domainLookupTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "domainLookupTime", "median"]
)

row(
 "frontEndTime",
 "help.html#frontEndTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "frontEndTime", "median"]
)

row(
 "pageDownloadTime",
 "help.html#pageDownloadTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "pageDownloadTime", "median"]
)

row(
 "pageLoadTime",
 "help.html#pageLoadTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "pageLoadTime", "median"]
)

row(
 "redirectionTime",
 "help.html#redirectionTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "redirectionTime", "median"]
)

row(
 "serverConnectionTime",
 "help.html#serverConnectionTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "serverConnectionTime", "median"]
)

row(
 "serverResponseTime",
 "help.html#serverResponseTime",
 ["statistics", "coach", "coachAdvice", "advice", "timings", "timings", "serverResponseTime", "median"]
)

row(
 "First Visual Change",
 "help.html#FirstVisualChange",
 ["statistics", "visualMetrics", "FirstVisualChange", "median"]
)

row(
 "Perceptual Speed Index",
 "help.html#PerceptualSpeedIndex",
 ["statistics", "visualMetrics", "PerceptualSpeedIndex", "median"]
)

row(
 "Contentful Speed Index",
 "help.html#ContentfulSpeedIndex",
 ["statistics", "visualMetrics", "ContentfulSpeedIndex", "median"]
)

row(
 "Visual Complete 85%",
 "help.html#VisualComplete85",
 ["statistics", "visualMetrics", "VisualComplete85", "median"]
)

row(
 "Visual Complete 95%",
 "help.html#VisualComplete95",
 ["statistics", "visualMetrics", "VisualComplete95", "median"]
)

row(
 "Visual Complete 99%",
 "help.html#VisualComplete99",
 ["statistics", "visualMetrics", "VisualComplete99", "median"]
)

row(
 "Last Visual Change",
 "help.html#LastVisualChange",
 ["statistics", "visualMetrics", "LastVisualChange", "median"]
)

f = open("diff.html", "w")
f.write(diff.render(
    rows=diff_data,
    url1=template_data["url1"],
    url2=template_data["url2"]
    )
)
f.close()

copyfile("diff.html", "report/diff.html")
copyfile("html/index.min.css", "report/index.min.css")
copyfile("html/help.html", "report/help.html")
