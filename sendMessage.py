#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import time

class sendMessage():
  chatID = 0
  bot = ""
  list_output = [] ##Beinhaltet alle Encounters welche versendet wurden
  list_message_ID = []
  list_lists_ID = []
  overview_old = ""
  overview_old2= ""
  overviewId = 0
  overviewId2= 0
  areaName = ""
  
  def send(self,latitude,longitude,bolt_line,normal_line,gmaps,stop,venue):
    try:
      if venue == True:
        id = self.bot.send_venue(self.singlechatID,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      else:
        id = self.bot.send_message(self.singlechatID,gmaps,parse_mode='HTML',disable_web_page_preview=False,disable_notification=True)
      self.list_output.append(stop)
      self.list_message_ID.append(id.message_id)
      outF = open(self.areaName+"output.txt","w")
      outF.writelines(str(self.list_message_ID))
      outF.close()
      return id.message_id
    except:
      print(".................... wait 30 seconds, too many messages")
      sleep = time.sleep(30)
      return sleep
  
  def sendOverview(self,message,message2,text):
    print("\nmessage1 ==> " + str(len(message)) + " (" + str(len(self.overview_old)) + ")")
    print("message2 ==> " + str(len(message2)) + " (" + str(len(self.overview_old2)) + ")")
    
    ## Wenn der Quest Zähler sich erhöht, liste 1 nur editieren
    if len(self.overview_old) == len(message) and not message == self.overview_old:
      self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewId.message_id, parse_mode='HTML',disable_web_page_preview=True)
      self.overview_old = message

    ## liste 1 & 2 haben sich nicht verändert ==> return
    if self.overview_old == message and self.overview_old2 == message2:
      return

    ## alte liste 2 ist vorhanden, hat aber keinen inhalt mehr ==> löschen
    if not message2 and self.overview_old2:
      try:
        self.bot.delete_message(self.chatID,self.overviewId2.message_id)
        self.list_lists_ID.remove(self.overviewId2.message_id)
        self.overview_old2 = message2
      except:
        print("Liste 2 konnte nicht entfernt werden !")

    ## liste 1 oder 2 hat sich verändert ==> neu senden
    try:
      if not message:
        message = text
        self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewId.message_id, parse_mode='HTML',disable_web_page_preview=True)
        self.overview_old = ""
        self.clearOldList(self.areaName,self.list_lists_ID)
        return
      if self.chatID != self.singlechatID:
        self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewId.message_id, parse_mode='HTML',disable_web_page_preview=True)
      else:
        self.bot.delete_message(self.chatID,self.overviewId.message_id)
        self.list_lists_ID.remove(self.overviewId.message_id)
        self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML',disable_web_page_preview=True)
        self.list_lists_ID.append(self.overviewId.message_id)
      self.overview_old = message
    except:
      try:
        self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML',disable_web_page_preview=True)
        self.list_lists_ID.append(self.overviewId.message_id)
        self.overview_old = message
      except:
        print("no message")
    
    ## liste 2 versenden wenn vorhanden
    if message2 and self.overview_old:
      try:
        if self.chatID != self.singlechatID:
          self.bot.edit_message_text(message2,chat_id=self.chatID, message_id=self.overviewId2.message_id, parse_mode='HTML',disable_web_page_preview=True)
        else:
          self.bot.delete_message(self.chatID,self.overviewId2.message_id)
          self.list_lists_ID.remove(self.overviewId2.message_id)
          self.overviewId2 = self.bot.send_message(self.chatID,message2,parse_mode='HTML',disable_web_page_preview=True)
          self.list_lists_ID.append(self.overviewId2.message_id)
        self.overview_old2 = message2
      except:
        try:
          self.overviewId2 = self.bot.send_message(self.chatID,message2,parse_mode='HTML',disable_web_page_preview=True)
          self.list_lists_ID.append(self.overviewId2.message_id)
          self.overview_old2 = message2
        except:
          print("no message_2")
    
    self.clearOldList(self.areaName,self.list_lists_ID)

   
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
