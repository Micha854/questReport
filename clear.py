import telebot
import time

class Clear():
  def clear(self,token,chatID,singlechatID,cfg):
    bot = telebot.TeleBot(token)
    
    ## delete old overviewLists
    try:
      f = open(cfg.areaName+cfg.areaNumber+"/lists.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(chatID,message_id=messageID)
      except:
        print("Alte LISTE konnte nicht entfernt werden")

    ## delete old venue messages
    try:
      f = open(cfg.areaName+cfg.areaNumber+"/output.txt", "r")
    except:
      return
    oldMessages = f.read()
    f.close()
    oldMessages = oldMessages[1:len(oldMessages)-1]
    oldMessages = oldMessages.split(', ') 
    for messageID in oldMessages:
      try:
        bot.delete_message(singlechatID,message_id=messageID)
      except:
        print("Alte Map Nachricht konnte nicht entfernt werden")
