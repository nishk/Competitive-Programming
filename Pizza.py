class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        print cls(['Basil', 'Tomatoes'])

    # def __repr__(self):
    #     print Pizza({self.ingredients})


P1 = Pizza(['Cheese', 'Chicken'])
P2 = Pizza(['Pineapple'])
P2.margherita()
