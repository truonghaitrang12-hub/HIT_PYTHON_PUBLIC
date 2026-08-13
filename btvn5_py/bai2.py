class Character:
    def __init__(self, name, hp, level):
        self.name = name          
        self.__hp = hp            
        self._level = level       

    def get_hp(self):
        return self.__hp

    def take_damage(self, damage):
        if damage > 0:
            self.__hp -= damage

            if self.__hp < 0:
                self.__hp = 0

    def heal(self, amount):
        if amount > 0:
            self.__hp += amount

    def attack(self):
        return 0

    def show_info(self):
        print(f"Tên: {self.name}")
        print(f"HP: {self.get_hp()}")
        print(f"Level: {self._level}")



class Warrior(Character):
    def __init__(self, name, hp, level, strength):

        # Gọi __init__ của lớp cha
        super().__init__(name, hp, level)

        self.strength = strength

    def attack(self):
        damage = self._level * 5 + self.strength
        return damage

    def show_info(self):
        super().show_info()
        print(f"Strength: {self.strength}")
        print(f"Damage: {self.attack()}")
        print("-" * 40)



class Mage(Character):
    def __init__(self, name, hp, level, mana, magic_power):
        super().__init__(name, hp, level)

        self.__mana = mana      
        self.magic_power = magic_power

    def get_mana(self):
        return self.__mana

   
    def attack(self):

        if self.__mana < 10:
            return 0

        self.__mana -= 10

        damage = self._level * 3 + self.magic_power

        return damage

    def show_info(self):
        super().show_info()
        print(f"Mana: {self.get_mana()}")
        print(f"Magic Power: {self.magic_power}")
        print(f"Damage: {self.attack()}")
        print("-" * 40)



warrior1 = Warrior( "Warrior A", 150, 10, 20)

warrior2 = Warrior( "Warrior B", 180, 12, 25)

mage1 = Mage("Mage A",120,10,50,30)

mage2 = Mage("Mage B", 100,8,40,35)

characters = [warrior1,warrior2,mage1,mage2]


print("===== THÔNG TIN BAN ĐẦU =====")

for character in characters:
    print(
        character.name,
        "| HP:",
        character.get_hp()
    )

=

print("\n CHIẾN ĐẤU")

damage = warrior1.attack()
mage1.take_damage(damage)

print( warrior1.name,"tấn công",mage1.name, "gây", damage, "damage")


damage = mage1.attack()
warrior1.take_damage(damage)

print( mage1.name,"tấn công",warrior1.name,"gây",damage,"damage")



damage = warrior2.attack()
mage2.take_damage(damage)

print(warrior2.name, "tấn công",mage2.name, "gây", damage, "damage")


damage = mage2.attack()
warrior2.take_damage(damage)

print( mage2.name,"tấn công",warrior2.name,"gây",damage,"damage")



print("\nTHÔNG TIN SAU KHI CHIẾN ĐẤU ")

for character in characters:
    print( character.name,"| HP:",character.get_hp())


strongest_hp = max(characters,key=lambda character: character.get_hp())

print("\n NHÂN VẬT CÒN NHIỀU HP NHẤT ")

print(strongest_hp.name,"- HP:",strongest_hp.get_hp())


print("\n KIỂM TRA isinstance() ")

print("warrior1 có phải Warrior không?", isinstance(warrior1, Warrior))

print("mage1 có phải Mage không?",isinstance(mage1, Mage))

print("warrior1 có phải Character không?",isinstance(warrior1, Character))


print("\n KIỂM TRA issubclass()")

print("Warrior có kế thừa Character không?",issubclass(Warrior, Character))

print( "Mage có kế thừa Character không?", issubclass(Mage, Character))

print("Character có kế thừa Warrior không?",issubclass(Character, Warrior))