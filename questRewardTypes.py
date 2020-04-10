
class rewardType():

  def getType(self,value,language):
    switch = {
      0: {
          "de": "Nicht festgelegt",
          "en": "",
          "fr": ""
        },
      1: {
          "de": "Erfahrung",
          "en": "",
          "fr": ""
        },
      2: {
          "de": "item",
          "en": "",
          "fr": ""
        },
      3: {
          "de": "Sternenstaub",
          "en": "Stardust",
          "fr": ""
        },
      4: {
          "de": "Beeren",
          "en": "",
          "fr": ""
        },
      5: {
          "de": "Avatar Kleidung",
          "en": "",
          "fr": ""
        },
      6: {
          "de": "Suche",
          "en": "",
          "fr": ""
        },
      7: {
          "de": "Monsterbegegnung",
          "en": "",
          "fr": ""
        }
    }
    #return switch.get(value,lambda: str(value))
    return switch[value][language]