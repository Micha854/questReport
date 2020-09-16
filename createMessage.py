import json
import time
import datetime

class createMessage():

  def create(self,Sql,send,sleep,cfg,values):
    overview = ""
    overview2= ""
    bolt_line= ""

    stardust = values["stardust"]
    item = values["item"]
    pokemon = values["pokemon"]

    pokemon.sort(key=lambda x: self.getPokemon(value=x, language=cfg.language))
    item.sort(key=lambda x: self.getItem(value=x, language="icon"))

    i = 0 # all found today quests
    x = 0 # all filtered quests
    id = 0  

    # sum of limit + puffer is the total limit
    limit = 70 # limit of a list, you can personalize this value
    puffer= 15 # split when reached in group 
    
    now = datetime.datetime.now()
    print("####################==========\\ *** Quest *** Update " + cfg.areaName+cfg.areaNumber + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " /==========####################\n")

    print("stardust melden: " + str(stardust))
    print("item ids melden: " + str(item))
    print("pokemon ids melden: " + str(pokemon))

    #return
    try:
      for stop in Sql.pokestop_id:
        name = "Unknown Pokestop" if Sql.name[i] is None else Sql.name[i]
        task = Sql.quest_task[i]

        if self.getForm(Sql.quest_pokemon_form_id[i],cfg.language):
          getform = "(" + self.getForm(Sql.quest_pokemon_form_id[i],cfg.language) + ")"
        else:
          getform = ""

        if self.getCostume(Sql.quest_pokemon_costume_id[i],cfg.language):
          getcostume = "(" + self.getCostume(Sql.quest_pokemon_costume_id[i],cfg.language) + ")"
        else:
          getcostume = ""

        if Sql.pokestop_id:
          if Sql.quest_stardust[i] in (stardust) or Sql.quest_item_id[i] in (item) or Sql.quest_pokemon_id[i] in (pokemon):

            ## MEGA ENGINE
            if Sql.quest_pokemon_id[i] in (pokemon) and Sql.quest_reward_type[i] == 12:
              bolt_line = self.getItem("0","icon") + " <b>" + " " + str(Sql.quest_item_amount[i]) + " " + str(self.getPokemon(Sql.quest_pokemon_id[i],cfg.language) + getform + getcostume) + " " + str(self.getType(Sql.quest_reward_type[i],cfg.language))
              if Sql.quest_pokemon_id[i-1] != Sql.quest_pokemon_id[i] and not Sql.quest_pokemon_id[i] == Sql.quest_pokemon_id[i+1]:
                msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                msg2= "\n"
              elif Sql.quest_pokemon_id[i-1] != Sql.quest_pokemon_id[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_pokemon_id[i] == Sql.quest_pokemon_id[i+1] or not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""

            ## STARDUST
            elif not Sql.quest_stardust[i] == 0:
              bolt_line = "\u2728 <b>" + str(Sql.quest_stardust[i]) + " " + str(self.getType(Sql.quest_reward_type[i],cfg.language))
              if Sql.quest_stardust[i-1] != Sql.quest_stardust[i] and not Sql.quest_stardust[i] == Sql.quest_stardust[i+1]:
                msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                msg2= "\n"
              elif Sql.quest_stardust[i-1] != Sql.quest_stardust[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_stardust[i] == Sql.quest_stardust[i+1] or not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""
            
            ## ITEM
            elif Sql.quest_item_id[i] in (item):
              bolt_line = self.getItem(Sql.quest_item_id[i],"icon") + " <b>" + str(Sql.quest_item_amount[i]) + " " + str(self.getItem(Sql.quest_item_id[i],cfg.language))
              if Sql.quest_item_id[i-1] != Sql.quest_item_id[i] and not Sql.quest_item_id[i] == Sql.quest_item_id[i+1]:
                msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                msg2= "\n"
              elif Sql.quest_item_id[i-1] != Sql.quest_item_id[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_item_id[i] == Sql.quest_item_id[i+1] or not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""
            
            ## POKEMON
            elif Sql.quest_pokemon_id[i] in (pokemon) and not Sql.quest_reward_type[i] == 12:
              bolt_line = "\U0001F47E <b>" + str(self.getPokemon(Sql.quest_pokemon_id[i],cfg.language) + getform + getcostume)
              if Sql.quest_pokemon_id[i-1] != Sql.quest_pokemon_id[i] and not Sql.quest_pokemon_id[i] == Sql.quest_pokemon_id[i+1]:
                msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                msg2= "\n"
              elif Sql.quest_pokemon_id[i-1] != Sql.quest_pokemon_id[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              elif not Sql.quest_task[i-1] == Sql.quest_task[i]:
                if not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n└ "
                  msg2 = "\n"
                else:
                  msg = "\n" + str(bolt_line + "</b>\n├ " + task) + "\n├ "
                  msg2 = ""
              else:
                if not Sql.quest_pokemon_id[i] == Sql.quest_pokemon_id[i+1] or not Sql.quest_task[i] == Sql.quest_task[i+1]:
                  msg = "\n└ "
                  msg2= "\n"
                else:
                  msg = "\n├ "
                  msg2= ""

            #singlemessage
            singlemessage = bolt_line + "</b>\n\U0001F4DC " + task
            gmaps = "\n\n\U0001f4cd" + "<a href='https://maps.google.de/?q=" + str(Sql.latitude[i]) + "," + str(Sql.longitude[i]) + "'><b>" + name + "</b></a>\n" + singlemessage

            if send.list_output.__contains__(stop):
              f = open(cfg.areaName+cfg.areaNumber+"/output.txt", "r")
                # Split the string based on space delimiter 
              list_string = f.read()
              list_string = list_string[1:len(list_string)-1]
              f.close()
              list_string = list_string.split(', ') 
              id = list_string[send.list_output.index(stop)]
            else:
              if cfg.singlechatId:
                print("===> found [" + str(i) + "]")
                id = send.send(Sql.latitude[i],Sql.longitude[i],bolt_line.replace("<b>", ""),name,gmaps,stop,cfg.venue)
            if cfg.singlechatId:
              linked = cfg.singlechatUrl + "/" + str(id)
            else:
              linked = "https://maps.google.de/?q=" + str(Sql.latitude[i]) + ", " + str(Sql.longitude[i])
            
            #split the lists
            if x < limit:
              overview += msg + "<a href='" + linked + "'>" + str(name) + "</a>" + msg2
            else:
              if len(overview2) > 5:
                overview2+= msg + "<a href='" + linked + "'>" + str(name) + "</a>" + msg2
              elif Sql.quest_task[i-1] == Sql.quest_task[i] and not puffer == 0:
                #split list after new quest task
                overview += msg + "...<a href='" + linked + "'>" + str(name) + "</a>" + msg2
                puffer -=1
              else:
                overview2+= msg + "<a href='" + linked + "'>" + str(name) + "</a>" + msg2
            x +=1
        i +=1

      date = datetime.datetime.now()
      data = date.day,date.month,date.year
      weekday = self.getTranslate(date.strftime("%A"),cfg.language)

      header = "\U0001F4C6 " + str(weekday) + ", " + str(data[0]) + ". " + str(data[1]) + ". " + str(data[2]) + "\n(" + str(i-1) + " " + self.getTranslate("scanned",cfg.language) + ")\n"

      if not x == 0:
        send.sendOverview(header+overview,overview2,self.getTranslate("noQuest",cfg.language))
      else:
        send.sendOverview(overview,overview2,self.getTranslate("noQuest",cfg.language))
      print("\nAktuell " + str(x) + " Meldungen von " + str(i-1) + " Stops\n")

      # DEBUG:
      #f = open("TEST.txt", "a")
      #f.writelines("\n\n####################==========\\ " + str(datetime.datetime.now()) + " /==========####################")
      #f.writelines("len ==> " + str(len(overview)) + "\n")
      #f.writelines(str(overview))
      #f.close()
      
    except Exception as e:
        outF = open(cfg.areaName+cfg.areaNumber+"/error.txt","w")
        ausgabe = "Passierte in der CreateMessage.py\n"
        ausgabe += "pokestop_id: " + str(Sql.pokestop_id.__len__) + "\n"
        ausgabe += "name: " + str(Sql.name.__len__) + "\n"
        ausgabe += "latitude: " + str(Sql.latitude.__len__) + "\n"
        ausgabe += "longitude: " + str(Sql.longitude.__len__) + "\n"
        ausgabe += "quest_task: " + str(Sql.quest_task.__len__) + "\n"
        ausgabe += "quest_stardust: " + str(Sql.quest_stardust.__len__) + "\n"
        ausgabe += "quest_pokemon_id: " + str(Sql.quest_pokemon_id.__len__) + "\n"
        ausgabe += "quest_reward_type: " + str(Sql.quest_reward_type.__len__) + "\n"
        ausgabe += "quest_item_id: " + str(Sql.quest_item_id.__len__) + "\n"
        ausgabe += "quest_item_amount: " + str(Sql.quest_item_amount.__len__) + "\n"
        ausgabe += "quest_pokemon_form_id: " + str(Sql.quest_pokemon_form_id.__len__) + "\n"
        ausgabe += "quest_pokemon_costume_id: " + str(Sql.quest_pokemon_costume_id.__len__) + "\n"
        ausgabe += "Wert i" + str(i) + "\n"
        ausgabe += "All Variable: " + str(len(all))
        outF.writelines(ausgabe + str(e))
        outF.close()

  ### get quest reward
  def getItem(self,value,language):
    data = open('json/QuestReward.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]
  
  ### get quest reward type
  def getType(self,value,language):
    data = open('json/QuestRewardType.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]
  
  ### get pokemon name
  def getPokemon(self,value,language):
    data = open('json/Pokemon.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon form
  def getForm(self,value,language):
    data = open('json/Form.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon costume
  def getCostume(self,value,language):
    data = open('json/Costume.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### tranlate some other text
  def getTranslate(self,value,language):
    text = {
      "noQuest": {
        "de": "Keine Quest gefunden",
        "en": "No Quest found",
        "fr": "Aucune quêtes trouvées"
      },
      "scanned": {
        "de": "Stops wurden gescannt",
        "en": "stops were scanned",
        "fr": "Pokéstops ont été scannés"
      },
      "Monday": {
        "de": "Montag",
        "en": "Monday",
        "fr": "Lundi"
      },
      "Tuesday": {
        "de": "Dienstag",
        "en": "Tuesday",
        "fr": "Mardi"
      },
      "Wednesday": {
        "de": "Mittwoch",
        "en": "Wednesday",
        "fr": "Mercredi"
      },
      "Thursday": {
        "de": "Donnerstag",
        "en": "Thursday",
        "fr": "Jeudi"
      },
      "Friday": {
        "de": "Freitag",
        "en": "Friday",
        "fr": "Vendredi"
      },
      "Saturday": {
        "de": "Samstag",
        "en": "Saturday",
        "fr": "Samedi"
      },
      "Sunday": {
        "de": "Sonntag",
        "en": "Sunday",
        "fr": "Dimanche"
      }
    }
    return text[value][language]
