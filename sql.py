import MySQLdb
import time
import json

class questReward():
  def getItem(self,value,language):
    data = open('json/QuestReward.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  def getPokemon(self,value,language):
    data = open('json/Pokemon.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

class Sql():
  pokestop_id = []
  name = []
  latitude = []
  longitude = []
  quest_task = []
  quest_stardust = []
  quest_pokemon_id = []
  quest_reward_type = []
  quest_item_id = []
  quest_item_amount = []
  quest_pokemon_form_id = []
  quest_pokemon_costume_id = []

  def startSQL(self,cfg, values):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.startSQL(cfg,values)
    self.pokestop_id.clear()
    self.name.clear()
    self.latitude.clear()
    self.longitude.clear()
    self.quest_task.clear()
    self.quest_stardust.clear()
    self.quest_pokemon_id.clear()
    self.quest_reward_type.clear()
    self.quest_item_id.clear()
    self.quest_item_amount.clear()
    self.quest_pokemon_form_id.clear()
    self.quest_pokemon_costume_id.clear()

    # Sortieren anhand der Pokemon Namen
    quest = questReward()

    item = values["item"]
    item.sort(key=lambda x: quest.getItem(value=x, language="icon"))
    sort_item = str(item).replace("[", "").replace("]", "")

    pokemon = values["pokemon"]
    pokemon.sort(key=lambda x: quest.getPokemon(value=x, language=cfg.language))
    sort_pokemon = str(pokemon).replace("[", "").replace("]", "")

    if sort_item:
      item_sort = "FIELD(q.quest_item_id," + sort_item + ")"
    else:
      item_sort = "q.quest_item_id DESC"
    
    if sort_pokemon:
      pokemon_sort = "FIELD(q.quest_pokemon_id," + sort_pokemon + ")"
    else:
      pokemon_sort = "q.quest_pokemon_id DESC"
    
    # Abfragen der Daten aus der Datenbank
    cursor.execute("SELECT p.pokestop_id, p.name, p.latitude, p.longitude, q.quest_task, q.quest_stardust, q.quest_pokemon_id, q.quest_reward_type, q.quest_item_id, q.quest_item_amount, q.quest_pokemon_form_id, q.quest_pokemon_costume_id FROM `trs_quest` q INNER JOIN pokestop p ON q.GUID = p.pokestop_id WHERE FROM_UNIXTIME(quest_timestamp,'%Y-%m-%d') = CURDATE() AND p.longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND p.latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + "ORDER BY q.quest_stardust DESC, " + pokemon_sort + ", " + item_sort + ", q.quest_item_amount DESC, q.quest_task, p.name")
    #all = cursor.fetchall()
    all = list(cursor.fetchall())
    
    i = 0
    try:
      while i < len(all):
        self.pokestop_id.append(all[i][0])
        self.name.append(all[i][1])
        self.latitude.append(all[i][2])
        self.longitude.append(all[i][3])
        self.quest_task.append(all[i][4])
        self.quest_stardust.append(all[i][5])
        self.quest_pokemon_id.append(all[i][6])
        self.quest_reward_type.append(all[i][7])
        self.quest_item_id.append(all[i][8])
        self.quest_item_amount.append(all[i][9])
        self.quest_pokemon_form_id.append(all[i][10])
        self.quest_pokemon_costume_id.append(all[i][11])
        i +=1
      
      self.pokestop_id.append("end")
      self.name.append("end")
      self.latitude.append("end")
      self.longitude.append("end")
      self.quest_task.append("end")
      self.quest_stardust.append("end")
      self.quest_pokemon_id.append("end")
      self.quest_reward_type.append("end")
      self.quest_item_id.append("end")
      self.quest_item_amount.append("end")
      self.quest_pokemon_form_id.append("end")
      self.quest_pokemon_costume_id.append("end")

    except Exception as e:
      outF = open(cfg.areaName+cfg.areaNumber+"/error.txt","w")
      ausgabe = "Passierte in der SQL.py\n"
      ausgabe += "pokestop_id: " + str(self.pokestop_id.__len__) + "\n"
      ausgabe += "name: " + str(self.name.__len__) + "\n"
      ausgabe += "latitude: " + str(self.latitude.__len__) + "\n"
      ausgabe += "longitude: " + str(self.longitude.__len__) + "\n"
      ausgabe += "quest_task: " + str(self.quest_task.__len__) + "\n"
      ausgabe += "quest_stardust: " + str(self.quest_stardust.__len__) + "\n"
      ausgabe += "quest_pokemon_id: " + str(self.quest_pokemon_id.__len__) + "\n"
      ausgabe += "quest_reward_type: " + str(self.quest_reward_type.__len__) + "\n"
      ausgabe += "quest_item_id: " + str(self.quest_item_id.__len__) + "\n"
      ausgabe += "quest_item_amount: " + str(self.quest_item_amount.__len__) + "\n"
      ausgabe += "quest_pokemon_form_id: " + str(self.quest_pokemon_form_id.__len__) + "\n"
      ausgabe += "quest_pokemon_costume_id: " + str(self.quest_pokemon_costume_id.__len__) + "\n"
      ausgabe += "Wert i" + str(i) + "\n"
      ausgabe += "All Variable: " + str(len(all))
      outF.writelines(ausgabe + str(e))
      outF.close()

    cursor = cursor.close()
    connection.close()