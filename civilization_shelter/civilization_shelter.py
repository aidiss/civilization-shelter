from random import choice
import random


class Resource(object):
    def __init__(self, arg):
        super(Resource, self).__init__()
        self.arg = arg


class Improvement(object):
    def __init__(self, arg):
        super(Improvement, self).__init__()
        self.arg = arg


class Tile(object):
    def __init__(self, type_, resource=None, improvements=None, units=[], city=''):
        self.type_ = type_
        self.resource = resource
        self.improvements = improvements
        self.units = units
        self.city = city

    def __repr__(self):
        return self.type_ + ', ' + ', '.join(self.units) + ', ' + self.city

    @staticmethod
    def create_random_tile():
        tile_type = random.choice(['dessert', 'grassland', 'plain'])
        return tile_type

    def get_production(self):
        """gets prodution for current player"""
        pass


class World(object):
    map_ = {}

    def __init__(self):
        print('World initiated')
        return


class Tech(object):
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


class Unit(object):
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
        pass

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


class WorldGenerator(object):
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


class Player(object):
    research = 0
    culture = 0
    faith = 0
    required_research = 0
    required_culture = 0
    required_faith = 0

    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg

    def choose_religion(self):
        pass

    def choose_ideology(self):
        pass

    def choose_research(self):
        pass

    def choose_social_policy(self):
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


class City():
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


if __name__ == '__main__':

    World.map_ = {
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
    print(World.map_)

    Tile.create_random_tile()

    cities = [City() for x in range(10)]
    for city in cities:
        city.yield_research
        city.yield_faith
        city.yield_food
        city.yield_production
        city.yield_culture

    players = [Player(x) for x in range(10)]
    for player in players:
        if player.research >= player.required_research:
            player.choose_research
        if player.culture >= player.required_culture:
            player.choose_social_policy
        if player.faith >= player.required_faith:
            if random.random() > 0.5:  # todo
                player.choose_social_policy
