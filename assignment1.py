class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # Encapsulated variable

    def turn_on(self):
        print(f"{self.model} is now ON!")

    def turn_off(self):
        print(f"{self.model} is now OFF!")

    def charge(self):
        self.__battery_level = 100
        print(f"{self.model} is fully charged!")

    def check_battery(self):
        print(f"Battery level of {self.model}: {self.__battery_level}%")

class SmartphoneWithCamera(Smartphone):  # Inheritance from Smartphone
    def __init__(self, brand, model, battery_level, camera_quality):
        super().__init__(brand, model, battery_level)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera quality!")

iphone = Smartphone("Apple", "iPhone 13", 80)
iphone.turn_on()
iphone.check_battery()
iphone.charge()

samsung = SmartphoneWithCamera("Samsung", "Galaxy S21", 60, "108MP")
samsung.turn_on()
samsung.take_photo()
