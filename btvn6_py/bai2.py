class Weapon:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def reload(self, amount=None):
        if amount is None:
            self.ammo = 30
            print(f"{self.name} nap day (khong tham so) -> Dan: {self.ammo}")
        else:
            self.ammo += amount
            print(f"{self.name} nap {amount} vien -> Dan: {self.ammo}")

    def shoot(self):
        pass


class Vandal(Weapon):
    def __init__(self):
        super().__init__("Vandal", 30)

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"[Vandal] Dung! - Dan con: {self.ammo}")
        else:
            print("[Vandal] Het dan!")


class Operator(Weapon):
    def __init__(self):
        super().__init__("Operator", 5)

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"[Operator] DOANG! - Dan con: {self.ammo}")
        else:
            print("[Operator] Het dan!")


class JettSkill:
    def __init__(self):
        self.knives = 5

    def shoot(self):
        if self.knives > 0:
            self.knives -= 1
            print(f"[JettSkill] Phong dao! - Dao con: {self.knives}")
        else:
            print("[JettSkill] Het dao!")


def perform_attack(entity, times):
    for _ in range(times):
        entity.shoot()


weapons = [Vandal(), Operator(), JettSkill()]

for weapon in weapons:
    perform_attack(weapon, 2)

print("---")

vandal = weapons[0]
vandal.reload(10)
vandal.reload()