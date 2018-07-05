

class Course:

    _all = []

    def __init__(self, dinner_party, recipe):
        self._dinner_party = dinner_party
        self._recipe = recipe
        Course._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all

    #DECORATORS

    #decorators for _dinner_party

    @property
    def dinner_party(self):
       return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinner_party):
       self._dinner_party = dinner_party

    #decorators for _recipe

    @property
    def recipe(self):
       return self._recipe

    @recipe.setter
    def recipe(self, recipe):
       self._recipe = recipe
