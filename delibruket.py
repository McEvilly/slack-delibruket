#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import re
import urllib
import os
from bs4 import BeautifulSoup
import sys

def week_menu():
  link = "http://www.delibruket.se/"
  html = urllib.urlopen(link)
  soup = BeautifulSoup(html, "html.parser")

  text = soup.get_text()
  text = text.split("VECKANS LUNCH")[1]
  volvo = text.split("DELIBRUKET UPPLANDS MOTOR")[1]
  volvo = volvo.split("DELIBRUKET HEDIN BIL")[0]
  hedin = text.split("DELIBRUKET HEDIN BIL")[1]
  hedin = hedin.split("Inkl.")[0]
  return volvo, hedin

def day_menu_volvo(volvo, day_index):
  if(day_index > 4):
    return "Det är helg!"
  veckodagar_volvo = ["MÅNDAG".decode('utf-8'), "TISDAG", "ONSDAG", "TORSDAG", "FREDAG","SALLADER"]
  dishtypes_volvo = ["Dagens Rustik", "Dagens Alternativ", "Dagens special"]

  veckans_vegetariska = volvo.split('VECKANS VEGETARISKA')[1]
  veckans_vegetariska = veckans_vegetariska.replace('\n', '')

  idag_volvo = veckodagar_volvo[day_index]
  imorrn_volvo = veckodagar_volvo[day_index + 1]

  volvo = volvo.split(idag_volvo)[1]
  volvo = volvo.split(imorrn_volvo)[0]

  volvo_dishes = []
  for i in range(0, len(dishtypes_volvo)):
    if(dishtypes_volvo[i] in volvo):
      volvo_dishes.append(volvo.split(dishtypes_volvo[i])[1])
    if i != len(dishtypes_volvo)-1:
      volvo_dishes[i] = volvo_dishes[i].split(dishtypes_volvo[i+1])[0]
    if i < len(volvo_dishes):
      volvo_dishes[i] = volvo_dishes[i].replace('\n', '')
  volvo_dishes.append(veckans_vegetariska)

  menu = "*Volvo*\n"
  for dish in volvo_dishes:
    menu += "- " + dish + "\n"
  return menu

def day_menu_hedin(hedin, day_index):
  if(day_index > 4):
    return "Det är helg!"
  veckodagar_hedin = ["Måndag".decode('utf-8'), "Tisdag", "Onsdag", "Torsdag", "Fredag","Veckans Sallader och Burgare"]
  dishtypes_hedin = ["Dagens Rustik", "Dagens Alternativ:"]

  idag_hedin = veckodagar_hedin[day_index]
  imorrn_hedin = veckodagar_hedin[day_index + 1]

  hedin = hedin.split(idag_hedin)[1]
  hedin = hedin.split(imorrn_hedin)[0]

  hedin_dishes = []

  for i in range(0, len(dishtypes_hedin)):
    hedin_dishes.append(hedin.split(dishtypes_hedin[i])[1])
    if i != len(dishtypes_hedin)-1:
      hedin_dishes[i] = hedin_dishes[i].split(dishtypes_hedin[i+1])[0]
    hedin_dishes[i] = hedin_dishes[i].replace('\n', '')

  menu = "\n" + "*Hedin*\n"
  for dish in hedin_dishes:
    menu += "- " + dish + "\n"

  return menu

def menu_today():
  veckodagar = ["Måndag".decode('utf-8'), "Tisdag", "Onsdag", "Torsdag", "Fredag"]
  day_index = datetime.datetime.today().weekday()
  if(day_index > 4):
    return "Det är helg!"
  menu = "*" + veckodagar[day_index] + "*\n"
  volvo, hedin = week_menu()
  menu += day_menu_volvo(volvo, day_index)
  menu += day_menu_hedin(hedin, day_index)
  print menu
  return menu

if __name__ == "__main__":
  menu_today()
