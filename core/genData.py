#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------
#
# heatMap export
#               -- get data from heatmap and generate information 
#
# genData.py: #TODO DESC HERE
#
#--------------------------------------------------------------
#
# Date:     2015-06-24
#
# Author:   gewu@baidu.com
#
#
import time
import datetime
from HeatMapExport import HeatMapExport
#--------------------------------------------------------------
# Globl Constants & Functions
#--------------------------------------------------------------

#--------------------------------------------------------------
# Classes
#--------------------------------------------------------------
class GenData(HeatMapExport):
    
    def __init__(self):
        super(GenData, self).__init__()

    def getDate(self, dateBegin, dateEnd):
        """the format is %Y-%m-%d"""
        begin = int(time.mktime(time.strptime(dateBegin, '%Y-%m-%d')))
        end = int(time.mktime(time.strptime(dateEnd, '%Y-%m-%d')))
        ret = []
        with open("timestamp") as t:
            for line in t:
                if int(line) >= end:
                    break
                elif int(line) > begin:
                    ret.append(int(line))
        return ret

    def generateData(self, timeList):
        for tL in timeList:
            ret = dict(timestamp=tL)
            infos = self.getInfo(ret)
            self.writeCsv(infos, ret['timestamp'])

if __name__ == "__main__":
    gd = GenData()
    now = datetime.date.today()
    #weekday = int(now.strftime("%w")) - 1
    #delta = datetime.timedelta(days=weekday)
    oneday = datetime.timedelta(days=3)
    datastr = now - oneday
    timeList = gd.getDate(str(datastr), str(now))
    gd.generateData(timeList)
