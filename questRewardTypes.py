
class rewardType():

  def getType(self,value,language):
    switch = {
      0: {
          "de": "Nicht festgelegt",
          "en": "",
          "fe": ""
        },
      1: {
          "de": "Erfahrung",
          "en": "",
          "fe": ""
        },
      2: {
          "de": "item",
          "en": "",
          "fe": ""
        },
      3: {
          "de": "Sternenstaub",
          "en": "Stardust",
          "fe": ""
        },
      4: {
          "de": "Beeren",
          "en": "",
          "fe": ""
        },
      5: {
          "de": "Avatar Kleidung",
          "en": "",
          "fe": ""
        },
      6: {
          "de": "Suche",
          "en": "",
          "fe": ""
        },
      7: {
          "de": "Monsterbegegnung",
          "en": "",
          "fe": ""
        }
    }
    #return switch.get(value,lambda: str(value))
    return switch[value][language]