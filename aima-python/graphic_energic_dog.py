from random import choice
from agents import *

class Food(Thing):
    pass

class Water(Thing):
    pass

TURN = False

class EnergeticBlindDog(Agent):
    location = [1, 1]
    direction = Direction("down")

    def move_forward(self, shd_turn=True):
        global TURN
        if not shd_turn:
            TURN = True
            return
        print(self.direction.direction, Direction.R)
        if self.direction.direction == Direction.R:
            self.location[0] += 1
        elif self.direction.direction == Direction.L:
            self.location[0] -= 1
        elif self.direction.direction == Direction.D:
            self.location[1] += 1
        elif self.direction.direction == Direction.U:
            self.location[1] -= 1

    def turn(self, d):
        self.direction = self.direction + d

    def eat(self, thing):
        if isinstance(thing, Food):
            return True
        return False

    def drink(self, thing):
        if isinstance(thing, Water):
            return True
        return False


def program(percepts):
    global TURN
    for p in percepts:
        print(p)
        if isinstance(p, Food):
            print('eat')
            return 'eat'
        elif isinstance(p, Water):
            print('drink')
            return 'drink'
        if TURN:
            TURN = False
            ch = random.choice((1, 2))
        else:
            ch = random.choice((1, 2, 3, 4))

        if ch == 1:
            return 'turn_right'
        elif ch == 2:
            return 'turn_left'
        else:
            return 'move_forward'


class Park2D(GraphicEnvironment):

    def percept(self, agent):
        things = self.list_things_at(agent.location)
        return things

    def execute_action(self, agent, action):
        if action == 'turn_right':
            print('{} decided to {} at location: {}'.format(
                str(agent)[1:-1], action, agent.location))
            agent.turn(Direction.R)
        elif action == 'turn_left':
            print('{} decided to {} at location: {}'.format(
                str(agent)[1:-1], action, agent.location))
            agent.turn(Direction.L)
        elif action == 'move_forward':
            loc = copy.deepcopy(agent.location)
            if agent.direction.direction == Direction.R:
                loc[0] += 1
            elif agent.direction.direction == Direction.L:
                loc[0] -= 1
            elif agent.direction.direction == Direction.D:
                loc[1] += 1
            elif agent.direction.direction == Direction.U:
                loc[1] -= 1
            #print('{} at {} facing {}'.format(agent, loc, agent.direction.direction))
            if self.is_inbounds(loc):  # move only if the target is a valid location
                print('{} decided to move {}wards at location: {}'.format(
                    str(agent)[1:-1], agent.direction.direction, agent.location))
                agent.move_forward()
            else:
                print('{} decided to move {}wards at location: {}, but couldnt'.format(
                    str(agent)[1:-1], agent.direction.direction, agent.location))
                agent.move_forward(False)
        elif action == "eat":
            print('eat')
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]):
                    print('{} ate {} at location: {}'
                          .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])
        elif action == "drink":
            print('drink')
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]):
                    print('{} drank {} at location: {}'
                          .format(str(agent)[1:-1], str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])

    def is_done(self):
        '''By default, we're done when we can't find a live agent,
        but to prevent killing our cute dog, we will stop before itself - when there is no more food or water'''
        no_edibles = not any(isinstance(thing, Food) or isinstance(
            thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles


park = Park2D(5, 5, color={'EnergeticBlindDog': (200,0,0), 'Water': (0, 200, 200), 'Food': (230, 115, 40)}, display= True)
dog = EnergeticBlindDog(program)
dogfood = Food()
water = Water()
park.add_thing(dog, [0, 0])
park.add_thing(dogfood, [1, 2])
park.add_thing(water, [2, 1])
morewater = Water()
park.add_thing(morewater, [0, 2])
print(
    'dog started at [0,0], facing down. Lets see if he found any food or water!')
park.run(20)
