# Base Class
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self):
        print("Receiving a call...")

    def take_a_picture(self):
        print(f"Taking picture with {self.rear_camera} rear camera")

    def phone_info(self):
        print("\nPhone Specifications:")
        print("Screen Type:", self.screen_type)
        print("Network Type:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)

# Child Class: Apple
class Apple(MobilePhone):
    def __init__(self, model, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim,
                         front_camera, rear_camera, ram, storage)
        self.brand = "Apple"
        self.model = model

    def phone_info(self):
        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        super().phone_info()

# Child Class: Samsung
class Samsung(MobilePhone):
    def __init__(self, model, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim,
                         front_camera, rear_camera, ram, storage)
        self.brand = "Samsung"
        self.model = model

    def phone_info(self):
        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        super().phone_info()

# Creating Apple Objects
iphone1 = Apple("iPhone 13", "Touch Screen", "5G", False,
                "12MP", "12MP", "4GB", "128GB")

iphone2 = Apple("iPhone SE", "Touch Screen", "4G", False,
                "7MP", "12MP", "3GB", "64GB")

# Creating Samsung Objects
samsung1 = Samsung("Galaxy S21", "Touch Screen", "5G", True,
                    "16MP", "48MP", "8GB", "256GB")

samsung2 = Samsung("Galaxy M12", "Touch Screen", "4G", True,
                    "8MP", "48MP", "4GB", "128GB")

# Using Objects
iphone1.phone_info()
iphone1.make_call("9876543210")
iphone1.take_a_picture()

samsung1.phone_info()
samsung1.receive_call()
samsung1.take_a_picture()
