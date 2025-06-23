# Product
class Pizza:
    def __init__(self):
        self.ingredients = []

    def show(self):
        print("Pizza with:", ", ".join(self.ingredients))

# Builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.ingredients.append("cheese")
        return self

    def add_pepperoni(self):
        self.pizza.ingredients.append("pepperoni")
        return self

    def add_olives(self):
        self.pizza.ingredients.append("olives")
        return self

    def build(self):
        return self.pizza

# Client
builder = PizzaBuilder()
pizza = builder.add_cheese().add_olives().build()
pizza.show()
