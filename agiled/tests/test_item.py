from common.weapon import Weapon
from common.entity import Projectile

def test_weapon_constructor():
    weapon = Weapon(
        title="Sample Weapon",
        speed=10,
        damage = 50
    )
    # Get the projectile
    weapon_proj = weapon.generate_projectile((1,1), 1, 0)

    # Create a hopefully identical projectile
    proj = Projectile((10, 10), 50, 0)

    assert proj.get_damage() == weapon_proj.get_damage()
    assert proj.get_speed() == weapon_proj.get_speed()
    assert proj.get_coords() == weapon_proj.get_coords()