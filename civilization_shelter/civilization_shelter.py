import random
from random import choice

class BaseObject():
    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)

class Resource(object):
    def __init__(self, arg):
        super(Resource, self).__init__()
        self.arg = arg


class Improvement(object):
    def __init__(self, arg):
        super(Improvement, self).__init__()
        self.arg = arg


class Tile(BaseObject):
    def __init__(self, type_, resource=None, improvements=None, units=[], city=''):
        self.type_ = type_
        self.resource = resource
        self.improvements = improvements
        self.units = units
        self.city = city

    def __repr__(self):
        # return self.type_ + ', ' + ', '.join(self.units) + ', ' + self.city
        return self.__dict__

    @staticmethod
    def create_random_tile():
        tile_type = random.choice(['dessert', 'grassland', 'plain'])
        return tile_type

    def get_production(self):
        """gets prodution for current player"""
        pass


class World(BaseObject):
    def __init__(self):
        self.map = {
            (0, 0): Tile(type_='desert'),
            (0, 1): Tile(type_='hill'),
            (0, 2): Tile(type_='hill'),
            (1, 0): Tile(type_='desert', improvements=['road', 'irrigation']),
            (1, 1): Tile(type_='grassland', units=['warrior', 'worker'], city='Kaunas'),
            (1, 2): Tile(type_='grassland'),
            (2, 0): Tile(type_='desert'),
            (2, 1): Tile(type_='grassland'),
            (2, 2): Tile(type_='grassland'),
        }


class Tech(BaseObject):
    def __init__(
            self,
            name: str,
            cost: int,
            era: str,
            required_techs: list,
            leads_to: list,
            units_enabled: list,
            buildings_enabled: list,
            wonders_enabled: list):
        self.name = name
        self.cost = cost
        self.era = era
        self.required_techs = required_techs
        self.leads_to = leads_to
        self.units_enabled = units_enabled
        self.building_enabled = buildings_enabled


class Unit(BaseObject):
    def __init__(
            self,
            location,
            required_tech,
            production_cost,
            movement_points,
            attack_strength_melee,
            attack_range_ranged,
            technology,
            upgrade_unit,
            owner,
            level,
            promotions):
        super(Unit, self).__init__()

        self.location = location
        self.required_tech = required_tech  # for type
        self.production_cost = production_cost

        self.movement_points = movement_points  # for type

        self.attack_strength_melee = attack_strength_melee
        self.attack_range_ranged = attack_range_ranged

        self.defence_bonus = 0
        self.technology = technology
        self.upgrade_unit = upgrade_unit
        self.upgradable = False
        self.owner = owner
        self.level = level
        self.promotions = promotions

    def move(self):
        (0, 1)
        (1, 1)
        (1, 0)
        (1, -1)
        (0, -1)
        (-1, 0)

    def get_promotion(self):
        pass

    def ranged_attack(self):
        pass

    def build_city(self):
        pass

    def pillage(self):
        pass

    def build_improvment(self):
        pass


class WorldGenerator(BaseObject):
    def __init__(self, arg):
        super(WorldGenerator, self).__init__()

    @staticmethod
    def generate_tile_type(tile_types):
        tile_type = choice(tile_types)
        return tile_type

    @staticmethod
    def generate_unit_type(unit_types):
        tile_type = choice(unit_types)
        return tile_type

    @staticmethod
    def generate_unit(unit_types):
        tile_type = choice(unit_types)
        return tile_type

    @staticmethod
    def generate_habitation(habitation_types):
        tile_type = choice(habitation_types)
        return tile_type

    @staticmethod
    def generate_river(starting_point, direction=None):
        # Generates river on map
        # Find two tiles to start a river from
        starting_point = ((1, 1), (1, 2),
                          (2, 2))
        end_point = ''
        direction = ['NE', 'NW', 'S']

    @staticmethod
    def get_starting_locations():
        pass


class Player(BaseObject):
    def __init__(self):
        super(Player, self).__init__()
        self.research = 0
        self.culture = 0
        self.faith = 0
        self.required_research = 0
        self.required_culture = 0
        self.required_faith = 0

    def choose_religion(self):
        pass

    def choose_ideology(self):
        pass

    def choose_research(self):
        if self.research >= self.required_research:
            pass

    def choose_social_policy(self):
        if self.culture >= self.required_culture: 
            pass

    def choose_city_production(self, city):
        pass

    def choose_unit_action(self, unit, action):
        pass

    def get_civilopedia(self):
        """generated from docs"""
        pass

    def get_city_overview(self):
        pass

    def get_trade_overview(self):
        pass

    def get_unit_overview(self):
        pass

    def get_social_policy_overview(self):
        pass

    def get_research_tree(self):
        pass

    def get_demographics(self, player=None):
        demographic = {}
        demographic['Population']
        demographic['Production']
        demographic['....']

    def step(self):
        self.choose_research()
        self.choose_social_policy()


class City(BaseObject):
    """A city is a large human settlement.[4][5] Cities generally have extensive systems for housing, transportation, sanitation, utilities, land use, and communication. Their density facilitates interaction between people, government organizations and businesses, sometimes benefiting different parties in the process."""

    def yield_research(self):
        pass

    def yield_faith(self):
        pass

    def yield_food(self):
        pass

    def yield_production(self):
        pass

    def yield_culture(self):
        pass

    def step(self):
        self.yield_research
        self.yield_faith
        self.yield_food
        self.yield_production
        self.yield_culture


class Game:
    def __init__(self, *args, **kwargs):
        self.world = World()
        self.cities = [City() for x in range(10)]
        self.players = [Player() for x in range(10)]

    def step1(self):
        for city in self.cities:
            city.step()

    def step2(self):
        for player in self.players:
            player.step()

    def run_model(self):
        for x in range(10):
            self.step1()
            self.step2()
        print(self.players)
