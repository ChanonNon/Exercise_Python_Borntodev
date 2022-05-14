class Cutomer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print(f"Added product to {self.name} {self.lastname}'s cart")
    
customer1 = Cutomer()
customer1.name = "Chanon"
customer1.lastname = "K"
customer1.addCart()

customer2 = Cutomer()
customer2.name = "Kittikorn"
customer2.lastname = "P"
customer2.addCart()

customer3 = Cutomer()
customer3.name = "James"
customer3.lastname = "M"
customer3.addCart()

customer4 = Cutomer()
customer4.name = "Robert"
customer4.lastname = "P"
customer4.addCart()