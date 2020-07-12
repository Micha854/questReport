
class rewardType():

  def getType(self,value,language):
    switch = {
      0: {
          "de": "Nicht festgelegt",
          "en": "Not fixed",
          "fr": "Non précisé"
        },
      1: {
          "de": "Erfahrung",
          "en": "Experience",
          "fr": "L'expérience"
        },
      2: {
          "de": "item",
          "en": "Item",
          "fr": "Item"
        },
      3: {
          "de": "Sternenstaub",
          "en": "Stardust",
          "fr": "Stardust"
        },
      4: {
          "de": "Beeren",
          "en": "Berries",
          "fr": "Baies"
        },
      5: {
          "de": "Avatar Kleidung",
          "en": "Avatar Clothes",
          "fr": "Vêtements d'avatar"
        },
      6: {
          "de": "Suche",
          "en": "Search",
          "fr": "Recherche"
        },
      7: {
          "de": "Monsterbegegnung",
          "en": "monster encounter",
          "fr": "rencontre monstre"
        }
    }
    #return switch.get(value,lambda: str(value))
    return switch[value][language]