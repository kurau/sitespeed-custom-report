import os
import json
import fnmatch
import matplotlib.pyplot as plt

from shutil import copyfile
from mako.template import Template

urlCount = 0
LHMetrics = dict()
# fcp si lcp tti tbt cls
LHMetrics["mobile"] = [4000, 5800, 4000, 7300, 600, 0.25]
LHMetrics["desktop"] = [1600, 2300, 2400, 4500, 350, 0.25]

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    #   3%2=1=true
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

def saveMetrics(filePath):
    try:
        with open(filePath) as json_file:
            data = json.load(json_file)
            firstContentfulPaint.append(data["audits"]["first-contentful-paint"]["numericValue"])
            speedIndex.append(data["audits"]["speed-index"]["numericValue"])
            largestContentfulPaint.append(data["audits"]["largest-contentful-paint"]["numericValue"])
            timeToInteractive.append(data["audits"]["interactive"]["numericValue"])
            totalBlockingTime.append(data["audits"]["total-blocking-time"]["numericValue"])
            cumulativeLayoutShift.append(data["audits"]["cumulative-layout-shift"]["numericValue"])
            serverResponseTime.append(data["audits"]["server-response-time"]["numericValue"])
            return 1
    except Exception:
        print("Problem with " + filePath)
        return 0
    finally:
        json_file.close()

lighthouse = Template(filename='html/lighthouse_template_a.html')

totalBlockingTime = []
firstContentfulPaint = []
speedIndex = []
largestContentfulPaint = []
timeToInteractive = []
cumulativeLayoutShift = []
serverResponseTime = []

score = []
scoreDict = dict()

detailed_data = []

cookieEnv = os.environ['COOKIE']
formFactor = os.environ['DEVICE']

# ==========
# find score

for dirpath, dirs, files in os.walk("."):
  for file in files:
    if fnmatch.fnmatch(file, "*-lighthouse.json"):
        try:
            with open(os.path.join(dirpath, file)) as json_file:
                data = json.load(json_file)
                tmpScore = data["categories"]["performance"]["score"]
                if tmpScore is None: break
                score.append(tmpScore)
                scoreDict[os.path.join(dirpath, file)] = tmpScore
        except Exception:
            print("Problem with " + os.path.join(dirpath, file))
        finally:
            json_file.close()

scoreSorted=sorted(score)
ind = (len(score)-1) // 2
scoreMedian=scoreSorted[ind]
filesMed = []
for (key, value) in scoreDict.items():
   if (value == scoreMedian):
       filesMed.append(key)

for filePath in filesMed:
    urlCount += saveMetrics(filePath)

finalUrl = data["finalUrl"]

# to HTML

fcpMed = median(firstContentfulPaint)
fcpLHMed = LHMetrics[formFactor][0]
fcpDelta = abs(fcpLHMed - fcpMed)
markStyle = "background-color: #ff9c9c;"
if (fcpLHMed > fcpMed):
    markStyle = "background-color: #9cffa3;"

detailed_data.append([
 "first-contentful-paint",
 "https://web.dev/first-contentful-paint/",
 min(firstContentfulPaint),
 median(firstContentfulPaint),
 fcpLHMed,
 fcpDelta,
 markStyle,
 max(firstContentfulPaint),
 "15%"
])


siMed = median(speedIndex)
siLHMed = LHMetrics[formFactor][1]
siDelta = abs(siLHMed - siMed)
markStyle = "background-color: #ff9c9c;"
if (siLHMed > siMed):
    markStyle = "background-color: #9cffa3;"

detailed_data.append([
 "speed-index",
 "https://web.dev/speed-index/",
 min(speedIndex),
 median(speedIndex),
 siLHMed,
 siDelta,
 markStyle,
 max(speedIndex),
 "15%"
])


lcpMed = median(largestContentfulPaint)
lcpLHMed = LHMetrics[formFactor][2]
lcpDelta = abs(lcpLHMed - lcpMed)
markStyle = "background-color: #ff9c9c;"
if (lcpLHMed > lcpMed):
    markStyle = "background-color: #9cffa3;"

detailed_data.append([
 "largest-contentful-paint",
 "https://web.dev/lcp/",
 min(largestContentfulPaint),
 median(largestContentfulPaint),
 lcpLHMed,
 lcpDelta,
 markStyle,
 max(largestContentfulPaint),
 "25%"
])


ttiMed = median(timeToInteractive)
ttiLHMed = LHMetrics[formFactor][3]
ttiDelta = abs(ttiLHMed - ttiMed)
markStyle = "background-color: #ff9c9c;"
if (ttiLHMed > ttiMed):
    markStyle = "background-color: #9cffa3;"

detailed_data.append([
 "Time to Interactive",
 "https://web.dev/interactive/",
 min(timeToInteractive),
 median(timeToInteractive),
 ttiLHMed,
 ttiDelta,
 markStyle,
 max(timeToInteractive),
 "15%"
])

tbtMed = median(totalBlockingTime)
tbtLHMed = LHMetrics[formFactor][4]
tbtDelta = abs(tbtLHMed - tbtMed)
markStyle = "background-color: #ff9c9c;"
if (tbtLHMed > tbtMed):
    markStyle = "background-color: #9cffa3;"

detailed_data.append([
 "total-blocking-time",
 "https://web.dev/lighthouse-total-blocking-time/",
 min(totalBlockingTime),
 median(totalBlockingTime),
 tbtLHMed,
 tbtDelta,
 markStyle,
 max(totalBlockingTime),
 "25%"
])


clsMed = median(cumulativeLayoutShift)
clsLHMed = LHMetrics[formFactor][5]
clsDelta = abs(clsLHMed - clsMed)
markStyle = "background-color: #ff9c9c;"
if (clsLHMed > clsMed):
    markStyle = "background-color: #9cffa3;"

detailed_data.append([
 "cumulative-layout-shift",
 "https://web.dev/cls/",
 min(cumulativeLayoutShift),
 median(cumulativeLayoutShift),
 clsLHMed,
 clsDelta,
 markStyle,
 max(cumulativeLayoutShift),
 "5%"
])

markStyle = "background-color: #9cffa3;"
detailed_data.append([
 "(TTFB) server-response-time",
 "https://web.dev/time-to-first-byte/",
 min(serverResponseTime),
 median(serverResponseTime),
 "?",
 "?",
 markStyle,
 max(serverResponseTime),
 "-"
])

f = open("lighthouse_a.html", "w")
f.write(lighthouse.render(
    data=detailed_data,
    url=finalUrl,
    times=urlCount,
    cookie=cookieEnv,
    scoreMed=int(scoreMedian*100),
    device=formFactor
    )
)
f.close()


plt.clf()
plt.title('total-blocking-time')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(totalBlockingTime, bins=500)
plt.savefig("totalBlockingTime_a.png")

plt.clf()
plt.title('first-contentful-paint')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(firstContentfulPaint, bins=500)
plt.savefig("firstContentfulPaint_a.png")

plt.clf()
plt.title('speed-index')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(speedIndex, bins=500)
plt.savefig("speedIndex_a.png")

plt.clf()
plt.title('largest-contentful-paint')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(largestContentfulPaint, bins=500)
plt.savefig("largestContentfulPaint_a.png")

plt.clf()
plt.title('Time to Interactive')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(timeToInteractive, bins=500)
plt.savefig("timeToInteractive_a.png")

plt.clf()
plt.title('TTFB')
plt.xlabel("time in ms")
plt.ylabel("Frequency")
plt.hist(serverResponseTime, bins=500)
plt.savefig("serverResponseTime_a.png")


copyfile("html/index.min.css", "report/index.min.css")
copyfile("lighthouse_a.html", "report/lighthouse_a.html")

copyfile("firstContentfulPaint_a.png", "report/firstContentfulPaint_a.png")
copyfile("speedIndex_a.png", "report/speedIndex_a.png")
copyfile("largestContentfulPaint_a.png", "report/largestContentfulPaint_a.png")
copyfile("timeToInteractive_a.png", "report/timeToInteractive_a.png")
copyfile("totalBlockingTime_a.png", "report/totalBlockingTime_a.png")
copyfile("serverResponseTime_a.png", "report/serverResponseTime_a.png")
