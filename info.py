import os
import json
import fnmatch
import matplotlib.pyplot as plt

from shutil import copyfile
from mako.template import Template


mytemplate = Template(filename='html/template.html')
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

copyfile("report.html", "report/report.html")
copyfile("html/index.min.css", "report/index.min.css")
copyfile("html/help.html", "report/help.html")
