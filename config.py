#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import ast

####Hier wird die Config aus dem Configfile geladen und den einzelen
####Werten zugewiesen

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  token = ""
  chatId = ""
  chatUrl = ""
  singlechatId = ""
  singlechatUrl = ""
  language = ""
  venue = bool
  areaName = ""
  areaNumber = ""
  min_latitude = ""
  max_latitude = ""
  min_longitude = ""
  max_longitude = ""
  sleepTime = ""

  def readConfig(self,cfgFile):  
    parser = ConfigParser()
    parser.read(cfgFile, encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')

    self.token = parser.get('Bot Settings', 'token')
    self.chatId = parser.get('Bot Settings', 'chat_id')
    self.chatUrl = parser.get('Bot Settings', 'chat_url')
    self.singlechatId = parser.get('Bot Settings', 'singlechat_id')
    self.singlechatUrl = parser.get('Bot Settings', 'singlechat_url')

    self.language = parser.get('Option', 'language')
    self.venue = parser.getboolean('Option', 'venue')

    self.areaName = parser.get('Geofence', 'areaName')
    self.areaNumber = parser.get('Geofence', 'areaNumber')
    
    self.min_latitude = parser.get('Geofence', 'minLat')
    self.max_latitude = parser.get('Geofence', 'maxLat')
    self.min_longitude = parser.get('Geofence', 'minLon')
    self.max_longitude = parser.get('Geofence', 'maxLon')

    self.sleepTime = parser.get('Message', 'sleep_time')