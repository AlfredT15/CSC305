from common.potion import PotionFactory, Potion, strength, heal, poison, defense
from common.entity import Player


def test_strength():
    """Test that strength potion is being applied correctly"""
    test_player = Player()
    potion_factory = PotionFactory()
    assert test_player.attributes.current_strength == 50
    test_player.inventory.add(potion_factory.get_potion(Potion.PotionType.STRENGTH, 10))
    test_player.use_item(0) # Adds item's effect to effect list
    while test_player.status_effects[0].time > 1:
        # Potion is currently active
        test_player.update_effects(False) # Applies effects currenly in list
        assert test_player.attributes.current_strength == 60
    test_player.update_effects(False) # Removes effect from list as now time has elapsed
    # Potion is currently inactive
    # Potion effect should be removed
    assert test_player.attributes.current_strength == 50

def test_healing():
    """Test that healing potion is being applied correctly"""
    test_player = Player()
    potion_factory = PotionFactory()
    test_player.attributes.current_hitpoints = 50
    assert test_player.attributes.current_hitpoints == 50
    test_player.inventory.add(potion_factory.get_potion(Potion.PotionType.HEALING, 5))
    test_player.use_item(0) # Adds item's effect to effect list
    current_heath = test_player.attributes.current_hitpoints
    while test_player.status_effects[0].time > 1:
        # Potion is currently active
        if test_player.status_effects[0].is_time():
            current_heath += 5
        test_player.update_effects(False) # Applies effects currenly in list
        assert test_player.attributes.current_hitpoints == current_heath
    test_player.update_effects(False) # Removes effect from list as now time has elapsed
    # Potion is currently inactive
    # Potion effect should still be present
    assert test_player.attributes.current_hitpoints == current_heath

def test_poison():
    """Test that poison potion is being applied correctly"""
    test_player = Player()
    potion_factory = PotionFactory()
    assert test_player.attributes.current_hitpoints == 100
    test_player.inventory.add(potion_factory.get_potion(Potion.PotionType.POISON, 5))
    test_player.use_item(0) # Adds item's effect to effect list
    current_heath = test_player.attributes.current_hitpoints
    while test_player.status_effects[0].time > 1:
        # Potion is currently active
        if test_player.status_effects[0].is_time():
            current_heath -= 5
        test_player.update_effects(False) # Applies effects currenly in list
        test_player.update_damage_timer()
        assert test_player.attributes.current_hitpoints == current_heath
    test_player.update_effects(False) # Removes effect from list as now time has elapsed
    # Potion is currently inactive
    # Potion effect should still be present
    assert test_player.attributes.current_hitpoints == current_heath

def test_defense():
    """Test that defense potion is being applied correctly"""
    test_player = Player()
    potion_factory = PotionFactory()
    assert test_player.attributes.current_defense == 0
    test_player.inventory.add(potion_factory.get_potion(Potion.PotionType.DEFENSE, 10))
    test_player.use_item(0) # Adds item's effect to effect list
    while test_player.status_effects[0].time > 1:
        # Potion is currently active
        test_player.update_effects(False) # Applies effects currenly in list
        assert test_player.attributes.current_defense == 10
    test_player.update_effects(False) # Removes effect from list as now time has elapsed
    # Potion is currently inactive
    # Potion effect should be removed
    assert test_player.attributes.current_defense == 0

def test_create_potion():
    """Test that a potion is being created correctly"""
    potion_factory = PotionFactory()
    potency = 10
    control_potion = Potion(Potion.PotionType.STRENGTH.value, strength, 240, 240, potency, True, 1)
    assert control_potion == potion_factory.get_potion(Potion.PotionType.STRENGTH, potency)

def test_heal_method():
    """Test that the heal method is operating correctly"""
    test_player = Player()
    test_player.attributes.current_hitpoints = 50
    assert test_player.attributes.current_hitpoints == 50
    heal(test_player, 10, False)
    assert test_player.attributes.current_hitpoints == 60

def test_poison_method():
    """Test that the poison method is operating correctly"""
    test_player = Player()
    assert test_player.attributes.current_hitpoints == 100
    poison(test_player, 10, False)
    assert test_player.attributes.current_hitpoints == 90

def test_strength_method():
    """Test that the strength method is operating correctly"""
    test_player = Player()
    assert test_player.attributes.current_strength == 50
    strength(test_player, 10, False)
    assert test_player.attributes.current_strength == 60

def test_defense_method():
    """Test that the defense method is operating correctly"""
    test_player = Player()
    test_player.attributes.current_hitpoints = 50
    assert test_player.attributes.current_defense == 0
    defense(test_player, 10, False)
    assert test_player.attributes.current_defense == 10