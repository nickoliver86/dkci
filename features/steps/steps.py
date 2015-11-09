__author__ = 'Nick'

from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from SendKeys import SendKeys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import statistics
from statistics import mean, stdev
import pdb
import numpy as np
import scipy as st

QB = dict()
RB = dict()
WR = dict()
TE = dict()

ffx = webdriver.Firefox()
ffx.maximize_window()
ffx.get('https://www.draftkings.com')
ffx.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a').click()
SendKeys("confidenceintervals")
SendKeys("{TAB}")
SendKeys("confidence95")
SendKeys("{ENTER}")
time.sleep(20)
ffx.find_element_by_xpath('/html/body/div[2]/div[2]/div/a[2]/span[2]').click()
time.sleep(0.5)
radios = ffx.find_elements_by_name("contest-type")
for radio in radios:
    parent = radio.find_element_by_xpath("..")
    if parent.text == "NFL":
        radio.click()
        break
# ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[2]/div[1]/p/label[5]/input').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[2]/div[2]/div/p/label[1]/input').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[3]/a[2]/span').click()
time.sleep(0.5)

# QB
for y in range(200):
   try:
        ffx.weekly_totals = []
        time.sleep(0.3)
        if y % 10 == 1 and y != 1:
            time.sleep(2)
        row = ffx.find_element_by_xpath('//div[@row = "{0}"]'.format(y))  # locate player's row
        time.sleep(1)
        player = row.find_element_by_css_selector("a.pop")  # locate player's name link
        saldiv = row.find_element_by_css_selector("div.slick-cell.l5.r5.sal")
        salspan = saldiv.find_element_by_css_selector("span")
        salary = salspan.text.replace("$", "")
        salary = salary.replace(",", "")
        ffx.weekly_totals.append(int(salary))
        player.click()
        time.sleep(0.5)
        ffx.find_element_by_xpath('//*[@id="player-info"]/div[4]/ul/li[2]/a').click()  # switch to game log
        time.sleep(0.5)
        player = ffx.find_element_by_xpath('//*[@id="player-info"]/div[1]/h1')  # player's full name
        print(str(player.text) + ": ")

        for x in range(2, 17):
            try:
                points = ffx.find_element_by_xpath("//*[@id='wrte-gamelog']/tbody/tr[{0}]/td[19]".format(x))  # weekly point total
                ffx.weekly_totals.append(float(points.text))
                # print(points.text)
            except NoSuchElementException:

                price = ffx.weekly_totals[0]
                required_pts = float((price/1000) * 2.9)
                average = mean(ffx.weekly_totals[1:])
                standard_deviation = stdev(ffx.weekly_totals[1:])
                z_score = (required_pts - average)/standard_deviation
                sample_size = len(ffx.weekly_totals[1:])
                confidence = st.norm.cdf(z_score)
                print(confidence)
                QB[player.text] = ffx.weekly_totals
                break

        ffx.find_element_by_xpath('//*[@id="fancybox-close"]').click()
        time.sleep(0.5)

   except NoSuchElementException:
       break

ActionChains(ffx).key_down(Keys.CONTROL).perform()
ffx.refresh()
ActionChains(ffx).key_up(Keys.CONTROL).perform()
time.sleep(3)
radios = ffx.find_elements_by_name("contest-type")
for radio in radios:
    parent = radio.find_element_by_xpath("..")
    if parent.text == "NFL":
        radio.click()
        break
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[2]/div[2]/div/p/label[1]/input').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[3]/a[2]/span').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[4]/div[2]/div[6]/ul/li[2]').click()
time.sleep(1)

# RB
for i in range(200):
   try:
        time.sleep(0.3)
        if i % 10 == 1 and i != 1:
            time.sleep(2)
        row = ffx.find_element_by_xpath('//div[@row = "{0}"]'.format(i))
        time.sleep(1)
        player = row.find_element_by_css_selector("a.pop")
        saldiv = row.find_element_by_css_selector("div.slick-cell.l5.r5.sal")
        salspan = saldiv.find_element_by_css_selector("span")
        salary = salspan.text.replace("$", "")
        salary = salary.replace(",", "")
        ffx.weekly_totals.append(int(salary))
        player.click()
        time.sleep(0.5)
        ffx.find_element_by_xpath('//*[@id="player-info"]/div[4]/ul/li[2]/a').click()
        time.sleep(0.5)
        player = ffx.find_element_by_xpath('//*[@id="player-info"]/div[1]/h1')
        print(str(player.text) + ": ")

        ffx.weekly_totals = []
        for x in range(2, 17):
            try:
                points = ffx.find_element_by_xpath("//*[@id='wrte-gamelog']/tbody/tr[{0}]/td[15]".format(x))  # weekly point total
                ffx.weekly_totals.append(float(points.text))
                print(points.text)
            except NoSuchElementException:
                RB[player.text] = ffx.weekly_totals
                break

        ffx.find_element_by_xpath('//*[@id="fancybox-close"]').click()
        time.sleep(0.5)

   except NoSuchElementException:
       break

ActionChains(ffx).key_down(Keys.CONTROL).perform()
ffx.refresh()
ActionChains(ffx).key_up(Keys.CONTROL).perform()
time.sleep(3)
radios = ffx.find_elements_by_name("contest-type")
for radio in radios:
    parent = radio.find_element_by_xpath("..")
    if parent.text == "NFL":
        radio.click()
        break
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[2]/div[2]/div/p/label[1]/input').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[3]/a[2]/span').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[4]/div[2]/div[6]/ul/li[3]').click()
time.sleep(1)

# WR
for y in range(200):
   try:
        time.sleep(0.3)
        if y % 10 == 1 and y != 1:
            time.sleep(2)
        row = ffx.find_element_by_xpath('//div[@row = "{0}"]'.format(y))
        time.sleep(1)
        player = row.find_element_by_css_selector("a.pop")
        saldiv = row.find_element_by_css_selector("div.slick-cell.l5.r5.sal")
        salspan = saldiv.find_element_by_css_selector("span")
        salary = salspan.text.replace("$", "")
        salary = salary.replace(",", "")
        ffx.weekly_totals.append(int(salary))
        player.click()
        time.sleep(0.5)
        ffx.find_element_by_xpath('//*[@id="player-info"]/div[4]/ul/li[2]/a').click()
        time.sleep(0.5)
        player = ffx.find_element_by_xpath('//*[@id="player-info"]/div[1]/h1')
        print(str(player.text) + ": ")

        ffx.weekly_totals = []
        for x in range(2, 17):
            try:
                points = ffx.find_element_by_xpath("//*[@id='wrte-gamelog']/tbody/tr[{0}]/td[15]".format(x))  # weekly point total
                ffx.weekly_totals.append(float(points.text))
                print(points.text)
            except NoSuchElementException:
                WR[player.text] = ffx.weekly_totals
                break

        ffx.find_element_by_xpath('//*[@id="fancybox-close"]').click()
        time.sleep(0.5)

   except NoSuchElementException:
       break

ActionChains(ffx).key_down(Keys.CONTROL).perform()
ffx.refresh()
ActionChains(ffx).key_up(Keys.CONTROL).perform()
time.sleep(3)
radios = ffx.find_elements_by_name("contest-type")
for radio in radios:
    parent = radio.find_element_by_xpath("..")
    if parent.text == "NFL":
        radio.click()
        break
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[2]/div[2]/div/p/label[1]/input').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[3]/div[3]/a[2]/span').click()
time.sleep(0.5)
ffx.find_element_by_xpath('//*[@id="lineup-card-container"]/div[1]/div[4]/div[2]/div[6]/ul/li[4]').click()
time.sleep(1)

# TE
for y in range(200):
   try:
        time.sleep(0.3)
        if y % 10 == 1 and y != 1:
            time.sleep(2)
        row = ffx.find_element_by_xpath('//div[@row = "{0}"]'.format(y))
        time.sleep(1)
        saldiv = row.find_element_by_css_selector("div.slick-cell.l5.r5.sal")
        salspan = saldiv.find_element_by_css_selector("span")
        salary = salspan.text.replace("$", "")
        salary = salary.replace(",", "")
        ffx.weekly_totals.append(int(salary))
        player = row.find_element_by_css_selector("a.pop")
        player.click()
        time.sleep(0.5)
        ffx.find_element_by_xpath('//*[@id="player-info"]/div[4]/ul/li[2]/a').click()
        time.sleep(0.5)
        player = ffx.find_element_by_xpath('//*[@id="player-info"]/div[1]/h1')
        print(str(player.text) + ": ")

        ffx.weekly_totals = []
        for x in range(2, 17):
            try:
                points = ffx.find_element_by_xpath("//*[@id='wrte-gamelog']/tbody/tr[{0}]/td[15]".format(x))  # weekly point total
                ffx.weekly_totals.append(float(points.text))
                print(points.text)
            except NoSuchElementException:
                TE[player.text] = ffx.weekly_totals
                break

        ffx.find_element_by_xpath('//*[@id="fancybox-close"]').click()
        time.sleep(0.5)

   except NoSuchElementException:
       break

print("DATA SCRAPING COMPLETE")



pdb.set_trace()
