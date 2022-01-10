"""Tests for Actor class"""
from common import actor_attributes, entity, item, status_effect
from common.potion import Potion, PotionFactory, heal, poison
from common.weapon import Weapon


def test_actor_type():
    """Test Actor's type"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    assert test_actor._entity_type == entity.EntityType.PLAYER

    test_player = entity.Player()
    assert test_player._entity_type == entity.EntityType.PLAYER

    test_enemy = entity.Enemy()
    assert test_enemy._entity_type == entity.EntityType.ENEMY


def test_actor_attributes():
    """Test setting and getting the actor's attributes"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    test_enemy = entity.Enemy()
    test_player = entity.Player()

    assert test_actor._attributes is None

    new_attributes = actor_attributes.ActorAttributes(0, 100, 20,4)
    test_actor._attributes = new_attributes
    test_player._attributes = new_attributes

    assert test_actor.attributes.current_defense == 0, "0 defense should equal 0"
    assert test_actor.attributes.current_hitpoints == 100, "100 hitpoints should equal 100"
    assert test_actor.attributes.current_strength == 20, "20 strength should equal 20"
    assert test_actor.attributes.current_speed == 4, "4 speed should equal 4"

    assert test_enemy.attributes.current_defense == 10, "10 defense should equal 10"
    assert test_enemy.attributes.current_hitpoints == 100, "100 hitpoints should equal 100"
    assert test_enemy.attributes.current_strength == 10, "0 strength should equal 0"
    assert test_enemy.attributes.current_speed == 4, "4 speed should equal 4"

    assert test_player.attributes.current_defense == 0, "0 defense should equal 0"
    assert test_player.attributes.current_hitpoints == 100, "100 hitpoints should equal 100"
    assert test_player.attributes.current_strength == 20, "20 strength should equal 20 -test_player"
    assert test_player.attributes.current_speed == 4, "4 speed should equal 4"


def test_actor_status_effects():
    """Test that an Actor's status effects are properly returned"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    assert test_actor.status_effects == []

    test_heal = status_effect.StatusEffect(Potion.PotionType.HEALING.value, heal, 240, 60, 5, False)

    test_actor.add_status_effect(test_heal)
    assert test_actor.status_effects == [test_heal]


def test_actor_is_dead():
    """Test that a newly created Actor is not dead"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    assert test_actor.is_dead() is False


def test_actor_get_coords():
    """Test that Actor's sprite coordinates are correct"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)

    assert test_actor.coords == (64, 64)


def test_actor_coords():
    """Test getting and setting Actor's coords"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    assert test_actor.coords == (64, 64)

    test_actor.coords = (128, 128)
    assert test_actor.coords == (128, 128)


def test_actor_take_damage():
    """Test that take_damage doesn't raise an exception when an actor doesn't have attributes"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    test_actor.take_damage(100)
    assert test_actor.attributes is None


def test_actor_damage_timer():
    """Test that an actor's damage timer can be retrieved and changed"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    assert test_actor._damage_timer == 0

    test_actor._damage_timer = 30
    assert test_actor._damage_timer == 30

    for _ in range(30):
        test_actor.update_damage_timer()

    assert test_actor._damage_timer == 0


def test_player_projectile():
    """Test that a Player can create a Projectile"""
    test_actor = entity.Player()
    test_actor.set_weapon(
        Weapon("", 0, 0)
    )

    direction = (0, 0)
    projectile = test_actor.generate_attack(direction, 0)

    assert test_actor.shot_timer == 15
    assert projectile.coords == test_actor.coords
    assert projectile.speed == direction


def test_player_is_dead():
    """Test that the player can be killed.
    Since players have 0 defense, an attack with 100 base damage does 100 actual damage
    """
    test_actor = entity.Player()
    assert test_actor.is_dead() is False
    assert test_actor.attributes.current_hitpoints == 100
    test_actor.take_damage(100, False)
    assert test_actor.attributes.current_hitpoints == 0
    assert test_actor.is_dead() is True


def test_player_coords():
    """Test getting and setting Player's coords"""
    test_actor = entity.Player()
    assert test_actor.coords == (64, 64)

    test_actor.coords = (128, 128)
    assert test_actor.coords == (128, 128)


def test_player_shot_timer():
    """Test setting and getting Player's shot timer"""
    test_actor = entity.Player()
    test_actor.shot_timer = 30
    assert test_actor.shot_timer == 30

    test_actor.shot_timer -= 30
    assert test_actor.can_shoot() is True


def test_player_status_effects_heal_poison():
    """Test getting, setting and updating player's status effects"""
    test_actor = entity.Player()
    assert test_actor.status_effects == []

    time = 10
    pulse = 1
    potency = 5

    test_poison = status_effect.StatusEffect(Potion.PotionType.POISON.value, poison, time, pulse, potency, False)
    test_heal = status_effect.StatusEffect(Potion.PotionType.HEALING.value, heal, time, pulse, potency, False)

    effects = [test_poison]
    test_actor._status_effects = effects
    test_actor.add_status_effect(test_heal)
    assert test_actor.status_effects == [test_poison, test_heal]

    for _ in range(time + 1):
        test_actor.update_effects(False)
        test_actor._damage_timer = 0

    assert test_actor.status_effects == []
    assert test_actor.attributes.current_hitpoints == test_actor.attributes.base_hitpoints


def test_player_use_item():
    """Test using an item"""
    test_actor = entity.Player()
    potion_factory = PotionFactory()
    assert test_actor.status_effects == []

    test_poison = potion_factory.get_potion(Potion.PotionType.POISON, 5)
    test_heal = potion_factory.get_potion(Potion.PotionType.HEALING, 5)

    test_actor.inventory.add(test_heal)
    test_actor.inventory.add(test_poison)
    assert test_actor.inventory.get_hotbar() == [[test_heal], [test_poison], [], [], []]

    test_actor.use_item(1)
    assert test_actor.inventory.get_hotbar() == [[test_heal], [], [], [], []]

    test_actor.use_item(1)
    assert test_actor.inventory.get_hotbar() == [[test_heal], [], [], [], []]

    assert test_actor.status_effects == [test_poison.get_effect()]


def test_player_take_damage():
    """Test that Player can take damage"""
    test_actor = entity.Player()
    assert test_actor.attributes.current_hitpoints == 100
    test_actor.take_damage(5, False)
    assert test_actor.attributes.current_hitpoints == 95


def test_actor_update_position():
    """Test the Actor's sprite coordinates can be updated'"""
    test_actor = entity.Actor(entity.EntityType.PLAYER)
    assert test_actor.coords == (64, 64)

    test_actor.update_position((32, 32))
    assert test_actor.coords == (96, 96)

    test_player = entity.Player()
    assert test_player.coords == (64, 64)

    test_player.update_position((32, 32))
    assert test_player.coords == (96, 96)

    test_enemy = entity.Player()
    assert test_enemy.coords == (64, 64)

    test_enemy.update_position((32, 32))
    assert test_enemy.coords == (96, 96)


def test_enemy_damage_timer():
    """Test that an enemy's damage timer can be retrieved and changed"""
    test_enemy = entity.Enemy()
    assert test_enemy._damage_timer == 0

    test_enemy._damage_timer = 30
    assert test_enemy._damage_timer == 30


def test_enemy_is_dead():
    """Test that enemies can be killed.
    Since enemies have 10 defense, an attack with 110 base damage does 100 actual damage
    """
    test_actor = entity.Enemy()
    assert test_actor.is_dead() is False
    assert test_actor.attributes.current_hitpoints == 100
    test_actor.take_damage(110, False)
    assert test_actor.attributes.current_hitpoints == 0
    assert test_actor.is_dead() is True


def test_enemy_get_coords():
    """Test that Enemy's sprite coordinates are correct'"""
    test_actor = entity.Enemy()

    assert test_actor.coords == (64, 64)


def test_enemy_set_coords():
    """Test that Enemy's sprite coordinates can be changed'"""
    test_actor = entity.Enemy()
    assert test_actor.coords == (64, 64)

    test_actor.coords = (128, 128)
    assert test_actor.coords == (128, 128)


def test_enemy_take_damage():
    """Test that Enemy can take damage"""
    test_actor = entity.Enemy()
    assert test_actor.attributes.current_hitpoints == 100
    test_actor.take_damage(5, False)
    assert test_actor.attributes.current_hitpoints == 99


def test_enemy_update_position():
    """Test that Enemy's sprite coordinates can be updated'"""
    test_actor = entity.Enemy()
    assert test_actor.coords == (64, 64)

    test_actor.update_position((32, 32))
    assert test_actor.coords == (96, 96)


def test_projectile_update_position():
    """Test that projectile can be moved and its range updated"""
    proj = entity.Projectile((0, 0), 50, 0)
    assert proj.coords == (0, 0)
    assert proj._range == 10 * 32
    assert proj.is_out_of_range() is False

    proj.update_position((4, 3))
    assert proj.coords == (4, 3)
    assert proj._range == (10 * 32) - 5
    assert proj.is_out_of_range() is False

    proj.update_position((223, 223))
    assert proj._range == 0
    assert proj.is_out_of_range() is True
