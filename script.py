import os
import json
import fnmatch
import matplotlib.pyplot as plt

from shutil import copyfile
from mako.template import Template


mytemplate = Template(filename='template.html')
detailed = Template(filename='detailed_template.html')
graphs = Template(filename='graphs_template.html')
template_data = {}

# index

with open('report/info.json') as json_file:
    data = json.load(json_file)

    template_data["url"] = data[0]["info"]["url"]

    template_data["rows"] = []
    rows = template_data["rows"]
    rows.append([])
    rows[0].append([
        "firstPaint",
        data[0]["statistics"]["timings"]["firstPaint"]["median"],
        data[0]["statistics"]["timings"]["firstPaint"]["p90"]])

    rows[0].append([
        "paintTiming",
        data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["median"],
        data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["p90"]])

    rows[0].append([
        "fullyLoaded",
        data[0]["statistics"]["timings"]["fullyLoaded"]["median"],
        data[0]["statistics"]["timings"]["fullyLoaded"]["p90"]])

    rows.append([])
    rows[1].append([
        "pageLoadTime",
        data[0]["statistics"]["timings"]["pageTimings"]["pageLoadTime"]["median"],
        data[0]["statistics"]["timings"]["pageTimings"]["pageLoadTime"]["p90"]])

    rows[1].append([
        "largestContentfulPaint",
        data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["median"],
        data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["p90"]])

    rows[1].append([
        "FirstVisualChange",
        data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["median"],
        data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["p90"]])

    rows.append([])
    rows[2].append([
        "LastVisualChange",
        data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["median"],
        data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["p90"]])

    rows[2].append([
        "SpeedIndex",
        data[0]["statistics"]["visualMetrics"]["SpeedIndex"]["median"],
        data[0]["statistics"]["visualMetrics"]["SpeedIndex"]["p90"]])

    rows[2].append([
        "PerceptualSpeedIndex",
        data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["median"],
        data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["p90"]])

    rows.append([])
    rows[3].append([
        "VisualReadiness",
        data[0]["statistics"]["visualMetrics"]["VisualReadiness"]["median"],
        data[0]["statistics"]["visualMetrics"]["VisualReadiness"]["p90"]])


    json_file.close()

f = open("report.html", "w")
f.write(mytemplate.render(
    rows=template_data["rows"],
    url=template_data["url"]
    )
)
f.close()

# detailed

detailed_data = []

detailed_data.append([])
detailed_data[0]= [
 "RUMSpeed Index",
 "help.html#rumSpeedIndex",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["rumSpeedIndex"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["rumSpeedIndex"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["rumSpeedIndex"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["rumSpeedIndex"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["rumSpeedIndex"]["max"]
]

detailed_data.append([])
detailed_data[1]= [
 "First Paint",
 "help.html#firstPaint",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["firstPaint"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["firstPaint"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["firstPaint"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["firstPaint"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["firstPaint"]["max"]
]

detailed_data.append([])
detailed_data[2]= [
 "Fully Loaded",
 "help.html#fullyLoaded",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["fullyLoaded"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["fullyLoaded"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["fullyLoaded"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["fullyLoaded"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["fullyLoaded"]["max"]
]

detailed_data.append([])
detailed_data[3]= [
 "Largest Contentful Paint",
 "help.html#largestContentfulPaint",
 data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["min"],
 data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["median"],
 data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["mean"],
 data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["p90"],
 data[0]["statistics"]["timings"]["largestContentfulPaint"]["renderTime"]["max"]
]

detailed_data.append([])
detailed_data[4]= [
 "first-contentful-paint",
 "help.html#first-contentful-paint",
 data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["min"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["median"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["mean"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["p90"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-contentful-paint"]["max"]
]

detailed_data.append([])
detailed_data[5]= [
 "first-paint",
 "help.html#first-paint",
 data[0]["statistics"]["timings"]["paintTiming"]["first-paint"]["min"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-paint"]["median"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-paint"]["mean"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-paint"]["p90"],
 data[0]["statistics"]["timings"]["paintTiming"]["first-paint"]["max"]
]

detailed_data.append([])
detailed_data[6]= [
 "backEndTime",
 "help.html#backEndTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["backEndTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["backEndTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["backEndTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["backEndTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["backEndTime"]["max"]
]

detailed_data.append([])
detailed_data[7]= [
 "domContentLoadedTime",
 "help.html#domContentLoadedTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domContentLoadedTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domContentLoadedTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domContentLoadedTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domContentLoadedTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domContentLoadedTime"]["max"]
]

detailed_data.append([])
detailed_data[8]= [
 "domInteractiveTime",
 "help.html#domInteractiveTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domInteractiveTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domInteractiveTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domInteractiveTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domInteractiveTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domInteractiveTime"]["max"]
]

detailed_data.append([])
detailed_data[9]= [
 "domainLookupTime",
 "help.html#domainLookupTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domainLookupTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domainLookupTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domainLookupTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domainLookupTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["domainLookupTime"]["max"]
]

detailed_data.append([])
detailed_data[10]= [
 "frontEndTime",
 "help.html#frontEndTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["frontEndTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["frontEndTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["frontEndTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["frontEndTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["frontEndTime"]["max"]
]

detailed_data.append([])
detailed_data[11]= [
 "pageDownloadTime",
 "help.html#pageDownloadTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageDownloadTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageDownloadTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageDownloadTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageDownloadTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageDownloadTime"]["max"]
]

detailed_data.append([])
detailed_data[12]= [
 "pageLoadTime",
 "help.html#pageLoadTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageLoadTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageLoadTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageLoadTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageLoadTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["pageLoadTime"]["max"]
]

detailed_data.append([])
detailed_data[13]= [
 "redirectionTime",
 "help.html#redirectionTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["redirectionTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["redirectionTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["redirectionTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["redirectionTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["redirectionTime"]["max"]
]

detailed_data.append([])
detailed_data[14]= [
 "serverConnectionTime",
 "help.html#serverConnectionTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverConnectionTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverConnectionTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverConnectionTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverConnectionTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverConnectionTime"]["max"]
]

detailed_data.append([])
detailed_data[15]= [
 "serverResponseTime",
 "help.html#serverResponseTime",
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverResponseTime"]["min"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverResponseTime"]["median"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverResponseTime"]["mean"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverResponseTime"]["p90"],
 data[0]["statistics"]["coach"]["coachAdvice"]["advice"]["timings"]["timings"]["serverResponseTime"]["max"]
]

detailed_data.append([])
detailed_data[16]= [
 "First Visual Change",
 "help.html#FirstVisualChange",
 data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["min"],
 data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["median"],
 data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["mean"],
 data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["p90"],
 data[0]["statistics"]["visualMetrics"]["FirstVisualChange"]["max"]
]

detailed_data.append([])
detailed_data[17]= [
 "Perceptual Speed Index",
 "help.html#PerceptualSpeedIndex",
 data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["min"],
 data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["median"],
 data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["mean"],
 data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["p90"],
 data[0]["statistics"]["visualMetrics"]["PerceptualSpeedIndex"]["max"]
]

detailed_data.append([])
detailed_data[18]= [
 "Contentful Speed Index",
 "help.html#ContentfulSpeedIndex",
 data[0]["statistics"]["visualMetrics"]["ContentfulSpeedIndex"]["min"],
 data[0]["statistics"]["visualMetrics"]["ContentfulSpeedIndex"]["median"],
 data[0]["statistics"]["visualMetrics"]["ContentfulSpeedIndex"]["mean"],
 data[0]["statistics"]["visualMetrics"]["ContentfulSpeedIndex"]["p90"],
 data[0]["statistics"]["visualMetrics"]["ContentfulSpeedIndex"]["max"]
]

detailed_data.append([])
detailed_data[19]= [
 "Visual Complete 85%",
 "help.html#VisualComplete85",
 data[0]["statistics"]["visualMetrics"]["VisualComplete85"]["min"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete85"]["median"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete85"]["mean"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete85"]["p90"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete85"]["max"]
]

detailed_data.append([])
detailed_data[20]= [
 "Visual Complete 95%",
 "help.html#VisualComplete95",
 data[0]["statistics"]["visualMetrics"]["VisualComplete95"]["min"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete95"]["median"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete95"]["mean"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete95"]["p90"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete95"]["max"]
]

detailed_data.append([])
detailed_data[21]= [
 "Visual Complete 99%",
 "help.html#VisualComplete99",
 data[0]["statistics"]["visualMetrics"]["VisualComplete99"]["min"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete99"]["median"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete99"]["mean"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete99"]["p90"],
 data[0]["statistics"]["visualMetrics"]["VisualComplete99"]["max"]
]

detailed_data.append([])
detailed_data[22]= [
 "Last Visual Change",
 "help.html#LastVisualChange",
 data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["min"],
 data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["median"],
 data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["mean"],
 data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["p90"],
 data[0]["statistics"]["visualMetrics"]["LastVisualChange"]["max"]
]

f = open("detailed.html", "w")
f.write(detailed.render(
    data=detailed_data,
    url=template_data["url"]
    )
)
f.close()

# graphs

graphs_data = []

lvc = []
fp = []
dit = []

for dirpath, dirs, files in os.walk("./custom"):
  for file in files:
    if fnmatch.fnmatch(file, "*.json"):
      with open(file) as json_file:
        data = json.load(json_file)
        lvc.append(data[0]['visualMetrics']['LastVisualChange'])
	    fp.append(data[0]['browserScripts']['timings']['firstPaint'])
        dit.append(data[0]['browserScripts']['timings']['pageTimings']['domInteractiveTime'])

plt.hist(lvc, bins=1000)
plt.savefig("lvc.png")

plt.clf()
plt.hist(fp, bins=1000)
plt.savefig("fp.png")

plt.clf()
plt.hist(dit, bins=1000)
plt.savefig("dit.png")

f = open("graphs.html", "w")
f.write(detailed.render(
    data=graphs_data,
    url=template_data["url"]
    )
)
f.close()

copyfile("report.html", "report/report.html")
copyfile("detailed.html", "report/detailed.html")
copyfile("graphs.html", "report/graphs.html")
copyfile("index.min.css", "report/index.min.css")
copyfile("help.html", "report/help.html")
