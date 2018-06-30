from agents import *

class Food(Thing):
    pass

class Water(Thing):
    pass


class BlindDog(Agent):
    location = 1

    def movedown(self):
        self.location += 1

    def eat(self, thing):
        if isinstance(thing, Food):
            #print("Dog: Ate food at {}.".format(self.location))
            return True
        return False

    def drink(self, thing):
        if isinstance(thing, Water):
            #print("Dog: Drank water at {}.".format(self.location))
            return True
        return False


class Park(Environment):
    def percept(self, agent):
        things = self.list_things_at(agent.location)
        return things

    def execute_action(self, agent, action):
        if action == "move down":
            print('{} decided to {} at location: {}'.format(
                str(agent)[1:-1], action, agent.location))
            agent.movedown()
        elif action == "eat":
          items = self.list_things_at(agent.location, tclass=Food)
          if len(items) != 0:
            if agent.eat(items[0]):
                    print('{} ate {} at location: {}'
                          .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])
        elif action == "drink":
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]): #Have the dog drink the first item
                    print('{} drank {} at location: {}'
                          .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0]) #Delete it from the Park after.

    def is_done(self):
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles

def program(percepts):
      '''Returns an action based on it's percepts'''
      for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
      return 'move down'

park = Park()
dog = BlindDog(program)
dogFood = Food()
water = Water()
water2 = Water()
park.add_thing(dog, 1)
park.add_thing(dogFood, 5)
park.add_thing(water, 7)
park.add_thing(water2, 15)
# park.run(5)
