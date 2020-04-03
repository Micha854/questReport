#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

class sendMessage():
  chatID = 0
  bot = ""
  list_output = [] ##Beinhaltet alle Encounters welche versendet wurden
  list_message_ID = []
  list_lists_ID = []
  overview_old = ""
  overviewId = 0
  areaName = ""
  
  def send(self,gmaps,stop):
    try:
      #id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      id = self.bot.send_message(self.singlechatID,gmaps,parse_mode='HTML',disable_web_page_preview=False,disable_notification=True)
      self.list_output.append(stop)
      self.list_message_ID.append(id.message_id)
      outF = open(self.areaName+"output.txt","w")
      outF.writelines(str(self.list_message_ID))
      outF.close()
      return id.message_id
    except:
      print(self.areaName+" Nachricht konnte nicht versendet werden")
  
  def sendOverview(self,message):
    if message == "":
      message = "Keine Quest gefunden"
    if not message == self.overview_old:
      if len(message) <= len(self.overview_old):
        try:
          self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewId.message_id, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht 
          self.overview_old = message
        except:
          try:
            print(self.areaName+" Konnte aber nicht editiern")
            self.bot.delete_message(self.chatID,self.overviewId.message_id)
            self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML')
            self.list_lists_ID.append(self.overviewId.message_id)
            self.clearOldList(self.areaName,self.list_lists_ID)
            self.overview_old = message
          except:
            print(self.areaName+" Nachricht konnte nicht editiert werden")    
      else:
        try: 
          self.bot.delete_message(self.chatID,self.overviewId.message_id)
          self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML')
          self.list_lists_ID.append(self.overviewId.message_id)
          self.clearOldList(self.areaName,self.list_lists_ID)
          self.overview_old = message
        except:
          try:
            self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML',disable_web_page_preview=True,disable_notification=False)
            self.list_lists_ID.append(self.overviewId.message_id)
            self.clearOldList(self.areaName,self.list_lists_ID)
            self.overview_old = message
          except:
            print(self.areaName+" Nachricht konnte nicht gesendet werden")
   
  def clearOldList (self, areaName, list_lists_ID):
    filename_list_lists_ID = self.areaName+"lists.txt"
    outF = open(filename_list_lists_ID,"w")
    outF.writelines(str(self.list_lists_ID))
    outF.close()

  def clearOutputList(self,encounter):
    i = 0
    print(self.areaName+" Checke Outputliste")
    for encount in self.list_output:
      if not encounter.__contains__(encount):
        try:
          print(self.areaName+" Entferne Nachricht")
          self.bot.delete_message(self.singlechatID,self.list_message_ID[i])
          self.list_message_ID.__delitem__(i)
          self.list_output.__delitem__(i)
        except:
          print(self.areaName+" Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()

  def setConfig(self,token,singlechatID,chatID,areaName):
    self.areaName = areaName
    self.singlechatID = singlechatID
    self.chatID = chatID
    self.bot = telebot.TeleBot(token)
