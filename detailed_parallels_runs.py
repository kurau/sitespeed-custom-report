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

# ========== GATHER =============

for dirpath, dirs, files in os.walk("report"):
  for file in files:
    if fnmatch.fnmatch(file, "*-metric.json"):
      with open(os.path.join(dirpath, file)) as json_file:

        data = json.load(json_file)
        json_file.close()
        rumSpeedIndex.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["rumSpeedIndex"])
        firstPaint.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["firstPaint"])
        fullyLoaded.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["fullyLoaded"])
        renderTime.append(data[0]["browserScripts"]["timings"]["largestContentfulPaint"]["renderTime"])
        firstcontentfulpaint.append(data[0]["browserScripts"]["timings"]["paintTiming"]["first-contentful-paint"])
        firstpaint.append(data[0]["browserScripts"]["timings"]["paintTiming"]["first-paint"])
        backEndTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["backEndTime"])
        domContentLoadedTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domContentLoadedTime"])
        domInteractiveTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domInteractiveTime"])
        domainLookupTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domainLookupTime"])
        frontEndTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["frontEndTime"])
        pageDownloadTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageDownloadTime"])
        pageLoadTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageLoadTime"])
        redirectionTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["redirectionTime"])
        serverConnectionTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverConnectionTime"])
        serverResponseTime.append(data[0]["browserScripts"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverResponseTime"])
        FirstVisualChange.append(data[0]["visualMetrics"]["FirstVisualChange"])
        PerceptualSpeedIndex.append(data[0]["visualMetrics"]["PerceptualSpeedIndex"])
        ContentfulSpeedIndex.append(data[0]["visualMetrics"]["ContentfulSpeedIndex"])
        VisualComplete85.append(data[0]["visualMetrics"]["VisualComplete85"])
        VisualComplete95.append(data[0]["visualMetrics"]["VisualComplete95"])
        VisualComplete99.append(data[0]["visualMetrics"]["VisualComplete99"])
        LastVisualChange.append(data[0]["visualMetrics"]["LastVisualChange"])


# ========== ANALISE AND PRINT =============


detailed = Template(filename='html/detailed_template.html')

# detailed

detailed_data = []

def to_detailed_data(name, link, metrics):
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
to_detailed_data("Largest Contentful Paint", "help.html#largestContentfulPaint", renderTime)
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


copyfile("detailed.html", "report/detailed.html")
copyfile("html/index.min.css", "report/index.min.css")
copyfile("html/help.html", "report/help.html")
