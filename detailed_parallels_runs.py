import os
import json
import fnmatch
import math

from shutil import copyfile
from mako.template import Template

# =========== UTILS ============

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return int(sortedLst[index])
    else:
        return int((sortedLst[index] + sortedLst[index + 1])/2.0)

def max(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1)
    return int(sortedLst[lstLen - 1])

def min(lst):
    sortedLst = sorted(lst)
    return int(sortedLst[0])

def avg(lst):
    sum_num = 0
    for t in lst:
        sum_num = sum_num + t

    avg = sum_num / len(lst)
    return int(avg)

def percentile(lst, percentile):
    size = len(lst)
    return int(sorted(lst)[int(math.ceil((size * percentile) / 100)) - 1])

def addData(metricsList, dataSet, stringPath):
    try:
        tmpData = dataSet.copy()
        listPaths = stringPath.split(".")
        for step in listPaths:
            tmpData = tmpData[step]
        metricsList.append(tmpData)
    except Exception:
        print("Problem with " + stringPath)

# ========== METRICS =============

rumSpeedIndex = []
firstPaint = []
fullyLoaded = []
renderTime = []
firstcontentfulpaint = []
firstpaint = []
backEndTime = []
domContentLoadedTime = []
domInteractiveTime = []
domainLookupTime = []
frontEndTime = []
pageDownloadTime = []
pageLoadTime = []
redirectionTime = []
serverConnectionTime = []
serverResponseTime = []
FirstVisualChange = []
PerceptualSpeedIndex = []
ContentfulSpeedIndex = []
VisualComplete85 = []
VisualComplete95 = []
VisualComplete99 = []
LastVisualChange = []

timeToDomContentFlushed = []
SpeedIndex = []
timeToFirstInteractive = []
timeToContentfulPaint =[]

# ========== GATHER =============

for dirpath, dirs, files in os.walk("report"):
  for file in files:
    if fnmatch.fnmatch(file, "*-metric.json"):
      with open(os.path.join(dirpath, file)) as json_file:

        data = json.load(json_file)
        json_file.close()
        addData(rumSpeedIndex, data[0], "browserScripts.coach.coachAdvice.advice.timings.rumSpeedIndex")
        addData(firstPaint, data[0], "browserScripts.coach.coachAdvice.advice.timings.firstPaint")
        addData(fullyLoaded, data[0], "browserScripts.coach.coachAdvice.advice.timings.fullyLoaded")
        addData(renderTime, data[0], "browserScripts.timings.largestContentfulPaint.renderTime")
        addData(timeToDomContentFlushed, data[0], "browserScripts.timings.timeToDomContentFlushed")
        addData(timeToFirstInteractive, data[0], "browserScripts.timings.timeToFirstInteractive")
        addData(timeToContentfulPaint, data[0], "browserScripts.timings.timeToContentfulPaint")
        addData(firstcontentfulpaint, data[0], "browserScripts.timings.paintTiming.first-contentful-paint")
        addData(firstpaint, data[0], "browserScripts.timings.paintTiming.first-paint")
        addData(backEndTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.backEndTime")
        addData(domContentLoadedTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.domContentLoadedTime")
        addData(domInteractiveTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.domInteractiveTime")
        addData(domainLookupTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.domainLookupTime")
        addData(frontEndTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.frontEndTime")
        addData(pageDownloadTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.pageDownloadTime")
        addData(pageLoadTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.pageLoadTime")
        addData(redirectionTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.redirectionTime")
        addData(serverConnectionTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.serverConnectionTime")
        addData(serverResponseTime, data[0], "browserScripts.coach.coachAdvice.advice.timings.timings.serverResponseTime")
        addData(FirstVisualChange, data[0], "visualMetrics.FirstVisualChange")
        addData(SpeedIndex, data[0], "visualMetrics.SpeedIndex")
        addData(PerceptualSpeedIndex, data[0], "visualMetrics.PerceptualSpeedIndex")
        addData(ContentfulSpeedIndex, data[0], "visualMetrics.ContentfulSpeedIndex")
        addData(VisualComplete85, data[0], "visualMetrics.VisualComplete85")
        addData(VisualComplete95, data[0], "visualMetrics.VisualComplete95")
        addData(VisualComplete99, data[0], "visualMetrics.VisualComplete99")
        addData(LastVisualChange, data[0], "visualMetrics.LastVisualChange")


# ========== ANALISE AND PRINT =============


detailed = Template(filename='html/detailed_template.html')

# detailed

detailed_data = []

def to_detailed_data(name, link, metrics):
    if not metrics:
        return
    detailed_data.append([
        name,
        link,
        min(metrics),
        median(metrics),
        avg(metrics),
        percentile(metrics, 90),
        max(metrics)
    ])

to_detailed_data("RUMSpeed Index", "help.html#rumSpeedIndex", rumSpeedIndex)
to_detailed_data("First Paint", "help.html#firstPaint", firstPaint)
to_detailed_data("Fully Loaded", "help.html#fullyLoaded", fullyLoaded)
to_detailed_data("DomContentFlushed", "help.html#timeToDomContentFlushed", timeToDomContentFlushed)
to_detailed_data("timeToFirstInteractive", "help.html#timeToFirstInteractive", timeToFirstInteractive)
to_detailed_data("timeToFirstInteractive", "help.html#timeToFirstInteractive", timeToFirstInteractive)
to_detailed_data("timeToContentfulPaint", "help.html#time-to-contentful-paint", timeToContentfulPaint)
to_detailed_data("first-contentful-paint", "help.html#first-contentful-paint", firstcontentfulpaint)
to_detailed_data("first-paint", "help.html#first-paint", firstpaint)
to_detailed_data("backEndTime", "help.html#backEndTime", backEndTime)
to_detailed_data("domContentLoadedTime", "help.html#domContentLoadedTime", domContentLoadedTime)
to_detailed_data("domInteractiveTime", "help.html#domInteractiveTime", domInteractiveTime)
to_detailed_data("domainLookupTime", "help.html#domainLookupTime", domainLookupTime)
to_detailed_data("frontEndTime", "help.html#frontEndTime", frontEndTime)
to_detailed_data("pageDownloadTime", "help.html#pageDownloadTime", pageDownloadTime)
to_detailed_data("pageLoadTime", "help.html#pageLoadTime", pageLoadTime)
to_detailed_data("redirectionTime", "help.html#redirectionTime", redirectionTime)
to_detailed_data("serverConnectionTime", "help.html#serverConnectionTime", serverConnectionTime)
to_detailed_data("serverResponseTime", "help.html#serverResponseTime", serverResponseTime)
to_detailed_data("First Visual Change", "help.html#FirstVisualChange", FirstVisualChange)
to_detailed_data("Speed Index", "help.html#SpeedIndex", SpeedIndex)
to_detailed_data("Perceptual Speed Index", "help.html#PerceptualSpeedIndex", PerceptualSpeedIndex)
to_detailed_data("Contentful Speed Index", "help.html#ContentfulSpeedIndex", ContentfulSpeedIndex)
to_detailed_data("Visual Complete 85%", "help.html#VisualComplete85", VisualComplete85)
to_detailed_data("Visual Complete 95%", "help.html#VisualComplete95", VisualComplete95)
to_detailed_data("Visual Complete 99%", "help.html#VisualComplete99", VisualComplete99)
to_detailed_data("Last Visual Change", "help.html#LastVisualChange", LastVisualChange)

f = open("detailed.html", "w")
f.write(detailed.render(
    data=detailed_data,
    url=data[0]["url"]
    )
)
f.close()

with open('detailed_data.json', 'w') as f:
    json.dump(detailed_data, f)
    f.close()

copyfile("detailed_data.json", "report/detailed_data.json")
copyfile("detailed.html", "report/detailed.html")
copyfile("html/index.min.css", "report/index.min.css")
copyfile("html/help.html", "report/help.html")
