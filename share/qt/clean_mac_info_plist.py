#!/usr/bin/env python
# Jonas Schnelli, 2013
# make sure the Marsmello-Qt.app contains the right plist (including the right version)
# fix made because of serval bugs in Qt mac deployment (https://bugreports.qt-project.org/browse/QTBUG-21267)

from string import Template
from datetime import date

MarsmelloDir = "./";

inFile     = MarsmelloDir+"/share/qt/Info.plist"
outFile    = "Marsmello-Qt.app/Contents/Info.plist"
version    = "unknown";

fileForGrabbingVersion = MarsmelloDir+"Marsmello-qt.pro"
for line in open(fileForGrabbingVersion):
	lineArr = line.replace(" ", "").split("=");
	if lineArr[0].startswith("VERSION"):
		version = lineArr[1].replace("\n", "");

fIn = open(inFile, "r")
fileContent = fIn.read()
s = Template(fileContent)
newFileContent = s.substitute(VERSION=version,YEAR=date.today().year)

fOut = open(outFile, "w");
fOut.write(newFileContent);

print "Info.plist fresh created"
