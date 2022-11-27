class Digimon:
  def __init__(self, name, type, level = 5):
    self.name = name
    self.level = level
    self.health = level * 5
    self.max_health = level * 5
    self.type = type
    self.is_knocked_out = False

def __repr__(self):
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Digimon".format(level = self.level, name = self.name, health=self.health, type = self.type)

a = Digimon("Augumon", "Fire", 7)
b = Digimon("Alraumon", "Plant", 7)
c = Digimon("Chibimon", "Dragon", 9)
d = Digimon("Culumon", "Holy", 10)
e = Digimon("Patamon", "Holy")
f = Digimon("Lunamon", "Holy", 4)


class Trainer:
  def __init__(self, digimon_list, num_potions, name):
    self.digimons = digimon_list
    self.potions = num_potions
    self.current_digimon = 0
    self.name = name

def __repr__(self):
        print("The trainer {name} has the following digimon".format(name = self.name))
        for digimon in self.digimons:
            print(digimon)
        return "The current active digimon is {name}".format(name = self.digimons[self.current_digimon].name)