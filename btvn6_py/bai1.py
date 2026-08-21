from abc import ABC, abstractmethod

class HomeAppliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def operate(self):
        pass


class KitchenAppliance(HomeAppliance):

    def turn_on(self):
        print(f"[{self.__class__.__name__}] Da cam dien va bat cong tac.")

    @abstractmethod
    def operate(self):
        pass


class RiceCooker(KitchenAppliance):

    def operate(self):
        print("[RiceCooker] Hoat dong: Dang nau chin gao...")


class Microwave(KitchenAppliance):

    def operate(self):
        print("[Microwave] Hoat dong: Dang ham nong thuc an...")


try:
    device = KitchenAppliance()
except TypeError as e:
    print("Loi:", e)

print("-" * 40)

devices = [RiceCooker(), Microwave()]

for device in devices:
    device.turn_on()
    device.operate()