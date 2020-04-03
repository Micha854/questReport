
class rewardType():

  def getType(self,value):
    switch = {
      0: "Nicht festgelegt",
      1: "Erfahrung",
      2: "item",
      3: "Sternenstaub",
      4: "Beeren",
      5: "Avatar Kleidung",
      6: "Suche",
      7: "Monsterbegegnung"

    }
    return switch.get(value,lambda: str(value))