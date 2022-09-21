
class AntMan(Hero):
    def init(self, name, health, damage):
        super(AntMan, self).init(name, health, damage, SuperAbility.SHIELD)

    def apply_super_power(self, boss, heroes):
        a = ['big','small']
        size = random.choice(a)
        n = random.randint(1,10)
        if size == 'big':
            self.health += self.health + n
            self.damage += self.damage + n
            print(f'{self.name} увеличелся на {n} раз')
        elif size == 'small':
            self.health += self.health - n
            self.damage += self.damage - n
            print(f'{self.name} уменьшился на {n} раз')

import random
from enum import Enum
round_number = 0

class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    LIFE = 5
    THUNDER = 6


class GameEntity:
    def init(self, name, health, damage):
        self.name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str(self):
        return f'{self.name} Health: {self.__health} ' \
               f'[{self.__damage}]'


class Boss(GameEntity):
    def __init(self, name, health, damage):
        GameEntity.init(self, name, health, damage)


class Hero(GameEntity):
    def init(self, name, health, damage, skill):
        GameEntity.init(self, name, health, damage)
        self.skill = skill

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    def apply_super_power(self, boss, heroes):
        raise NotImplementedError("Must be implemented")


class Warrior(Hero):
    def __init(self, name, health, damage):
        Hero.init(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        boss.health = boss.health - coeff * self.damage
        print(f'{self.name} наносит крит урон: {coeff * self.damage}')


class Magic(Hero):
    def init(self, name, health, damage):
        Hero.init(self, name, health, damage, SuperAbility.HEAL)

    def apply_super_power(self, boss, heroes):
        boost = random.randint(5, 10)
        for h in heroes:
            if h.health > 0 and h.damage > 0:
                h.damage += boost
        print(f'{self.name} Бустил всех на {boost}')



class Medic(Hero):
    def init(self, name, health, damage, heal_points):
        Hero.init(self, name, health, damage, SuperAbility.HEAL)
        self.heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, value):
        self.__heal_points = value

    def apply_super_power(self, boss, heroes):
        for h in heroes:
            if h.health > 0 and self != h:
                h.health = h.health + self.__heal_points
        print(f'{self.name} подлатал всех на  {self.__heal_points}')


class Berserk(Hero):
    def __init(self, name, health, damage):
        Hero.init(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_power(self, boss, heroes):
        range = [5, 10, 15]
        saved = random.choice(range)
        self.health += saved
        boss.health -= saved
        print(f'{self.name} сохроняет {saved} xp от урона боса и след раунд '
              f'бет {self.damage} + {saved}')

class Witcher(Hero):
    def init(self, name, health,damage):
        Hero.init(self, name, health,damage,SuperAbility.LIFE)

    def apply_super_power(self, boss, heroes):
        for h in heroes:
            if h.health == 0 and self != h:
                h.health = self.health
                self.health = 0
                print(f'{self.name} отдала свою жизнь {h.name}')
                break

class Thor(Hero):
    def init(self, name, health,damage):
        Hero.init(self, name, health,damage,SuperAbility.THUNDER)

    def apply_super_power(self, boss, heroes):
        shans = random.randint(1,4)
        if shans == 1:
            if boss.health > 0 and self.health > 0:
                boss.damage = 0
                print('Босс оглушен на следуший раунд')
        else:
            boss.damage = 80
class AntMan(Hero):
    def init(self, name, health, damage):
        super(AntMan, self).init(name, health, damage, SuperAbility.SHIELD)

    def apply_super_power(self, boss, heroes):
        a = ['big','small']
        size = random.choice(a)
        n = random.randint(1,10)
        if size == 'big':
            self.health += self.health + n
            self.damage += self.damage + n
            print(f'{self.name} увеличелся на {n} раз')
        elif size == 'small':
            self.health += self.health - n
            self.damage += self.damage - n
            print(f'{self.name} уменьшился на {n} раз'
class AntMan(Hero):
    def init(self, name, health, damage):
        super(AntMan, self).init(name, health, damage, SuperAbility.SHIELD)

    def apply_super_power(self, boss, heroes):
        a = ['big','small']
        size = random.choice(a)
        n = random.randint(1,10)
        if size == 'big':
            self.health = self.health + n
            self.damage = self.damage + n
            print(f'{self.name} увеличелся на {n} раз')
        elif size == 'small':
            self.health = self.health - n
            self.damage = self.damage - n
            print(f'{self.name} уменьшился на {n} раз')
def start():
    boss = Boss("Аид", 2500, 60)

    warrior = Warrior("", 250, 15)
    medic_1 = Medic("Элиз", 300, 5, 15)
    magic = Magic("Мерселин", 260, 30)
    berserk = Berserk("John", 300, 10)
    medic_2 = Medic("Aibolit", 400, 10, 5)
    wedmag = Witcher("Anna",500,0)
    tor = Thor('Tor',200,15)
    antman = AntMan('mike',200,15,skill=SuperAbility.LIFE)
    heroes = [wedmag,magic,medic_2,medic_1,warrior,berserk,tor,antman]
    print_stats(boss, heroes)

    while (not is_game_finished(boss, heroes)):
        play_round(boss, heroes)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_skills(boss, heroes)
    print_stats(boss, heroes)


def boss_hits(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.health = h.health - boss.damage


def heroes_hit(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            boss.health = boss.health - h.damage


def heroes_skills(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.apply_super_power(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True

    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!!!")

    return all_heroes_dead


def print_stats(boss, heroes):
    print("------------- ROUND: " + str(round_number) + " -------------")
    print(boss)
    for h in heroes:
        print(h)


start()