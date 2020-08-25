import os
import json
import fnmatch
import matplotlib.pyplot as plt

from shutil import copyfile
from mako.template import Template

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

lighthouse = Template(filename='html/lighthouse_template.html')

totalBlockingTime = []
firstContentfulPaint = []
speedIndex = []
largestContentfulPaint = []
timeToInteractive = []
cumulativeLayoutShift = []

detailed_data = []

urlCount = 0

for dirpath, dirs, files in os.walk("."):
  for file in files:
    if fnmatch.fnmatch(file, "*-lighthouse.json"):
        try:
            with open(os.path.join(dirpath, file)) as json_file:
                data = json.load(json_file)
                firstContentfulPaint.append(data["audits"]["first-contentful-paint"]["numericValue"])
                speedIndex.append(data["audits"]["speed-index"]["numericValue"])
                largestContentfulPaint.append(data["audits"]["largest-contentful-paint"]["numericValue"])
                timeToInteractive.append(data["audits"]["interactive"]["numericValue"])
                totalBlockingTime.append(data["audits"]["total-blocking-time"]["numericValue"])
                cumulativeLayoutShift.append(data["audits"]["cumulative-layout-shift"]["numericValue"])
                urlCount += 1
        except Exception:
            print("Problem with " + os.path.join(dirpath, file))
        finally:
            json_file.close()

finalUrl = data["finalUrl"]

detailed_data.append([
 "first-contentful-paint",
 "https://web.dev/first-contentful-paint/",
 min(firstContentfulPaint),
 median(firstContentfulPaint),
 max(firstContentfulPaint),
 "15%"
])

detailed_data.append([
 "speed-index",
 "https://web.dev/speed-index/",
 min(speedIndex),
 median(speedIndex),
 max(speedIndex),
 "15%"
])

detailed_data.append([
 "largest-contentful-paint",
 "https://web.dev/lcp/",
 min(largestContentfulPaint),
 median(largestContentfulPaint),
 max(largestContentfulPaint),
 "25%"
])

detailed_data.append([
 "Time to Interactive",
 "https://web.dev/interactive/",
 min(timeToInteractive),
 median(timeToInteractive),
 max(timeToInteractive),
 "15%"
])

detailed_data.append([
 "total-blocking-time",
 "https://web.dev/lighthouse-total-blocking-time/",
 min(totalBlockingTime),
 median(totalBlockingTime),
 max(totalBlockingTime),
 "25%"
])

detailed_data.append([
 "cumulative-layout-shift",
 "https://web.dev/cls/",
 min(cumulativeLayoutShift),
 median(cumulativeLayoutShift),
 max(cumulativeLayoutShift),
 "5%"
])

f = open("lighthouse.html", "w")
f.write(lighthouse.render(
    data=detailed_data,
    url=finalUrl,
    times=urlCount
    )
)
f.close()


plt.clf()
plt.title('total-blocking-time')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(totalBlockingTime, bins=500)
plt.savefig("totalBlockingTime.png")

plt.clf()
plt.title('first-contentful-paint')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(firstContentfulPaint, bins=500)
plt.savefig("firstContentfulPaint.png")

plt.clf()
plt.title('speed-index')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(speedIndex, bins=500)
plt.savefig("speedIndex.png")

plt.clf()
plt.title('largest-contentful-paint')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(largestContentfulPaint, bins=500)
plt.savefig("largestContentfulPaint.png")

plt.clf()
plt.title('Time to Interactive')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(timeToInteractive, bins=500)
plt.savefig("timeToInteractive.png")


copyfile("html/index.min.css", "report/index.min.css")
copyfile("lighthouse.html", "report/lighthouse.html")

copyfile("firstContentfulPaint.png", "report/firstContentfulPaint.png")
copyfile("speedIndex.png", "report/speedIndex.png")
copyfile("largestContentfulPaint.png", "report/largestContentfulPaint.png")
copyfile("timeToInteractive.png", "report/timeToInteractive.png")
copyfile("totalBlockingTime.png", "report/totalBlockingTime.png")
