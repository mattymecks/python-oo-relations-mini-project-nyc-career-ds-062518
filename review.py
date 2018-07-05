class Review:

    _all = []

    def __init__(self, reviewer, recipe, rating, comment = None):
        self._reviewer = reviewer
        self._recipe = recipe
        self._rating = rating
        self._comment = comment
        Review._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all


    #DECORATORS

    #decorators for _reviewer

    @property
    def reviewer(self):
       return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
       self._reviewer = reviewer

    #decorators for _rating

    @property
    def rating(self):
       return self._rating

    @rating.setter
    def rating(self, rating):
       self._rating = rating


    #decorators for _comment

    @property
    def comment(self):
       return self._comment

    @comment.setter
    def comment(self, comment):
       self._comment = comment


    #decorators for _recipe

    @property
    def recipe(self):
       return self._recipe

    @recipe.setter
    def recipe(self, recipe):
       self._recipe = recipe
