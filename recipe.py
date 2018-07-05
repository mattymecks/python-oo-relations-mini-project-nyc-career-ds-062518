from review import Review

class Recipe:

    _all = []

    def __init__(self, name):
        self._name = name
        Recipe._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return Recipe._all

    # @classmethod
    # def reviews_by_recipe(cls):
    #     reviews_by_recipe = {}
    #     for recipe in cls.all():
    #         reviews_by_recipe[recipe] = recipe.reviews()
    #     return reviews_by_recipe
    #
    # @classmethod
    # def recipe_by_rating(cls):
    #     recipe_rating_dict = {}
    #     for recipe in cls.all():
    #         recipe_rating_dict[recipe] = recipe.ratings()
    #
    #     print(cls.all())


        # recipe_rating_avgs = {}
        # for recipe, ratings in recipe_rating_dict.items():
        #     #fix with a test for 0 list
        #     rating_avg = sum(ratings)/len(ratings)
        #     recipe_rating_avgs[recipe] = rating_avg
        #
        # recipe_rating_list = []
        # for recipe, rating in recipe_rating_avgs.items():
        #     recipe_rating_list.append(rating, recipe)
        #
        # return recipe_rating_list


    #this gives me a dict of k,v of recipe, [reviews]

    @classmethod
    def top_three(cls):
        recipes = cls.all()
        filtered_recipes = list(filter(lambda recipe: len(recipe.ratings()) >= 1, recipes))
        sorted_recipes = sorted(filtered_recipes, key=lambda recipe: recipe.average_rating(), reverse = True)
        return sorted_recipes[:3]

        #for each recipe, pull out all of its ratings into a list
        #match review and rating
        #sort by review
        #append each of the top recipes to a list
        #return list
    @classmethod
    def bottom_three(cls):
        recipes = cls.all()
        filtered_recipes = list(filter(lambda recipe: len(recipe.ratings()) >= 1, recipes))
        sorted_recipes = sorted(filtered_recipes, key=lambda recipe: recipe.average_rating())
        return sorted_recipes[:3]

    #INSTANCEMETHODS

    def reviews(self):
        return [review for review in Review.all() if review.recipe == self]

    def ratings(self):
        return [review.rating for review in self.reviews()]

    def average_rating(self):
        ratings = self.ratings()
        for rating in ratings:
            if len(ratings) == 0:
                return "Recipe has no ratings"
                break
            else:
                number_ratings = len(ratings)
        sum_ratings = sum(ratings)
        return sum_ratings/number_ratings

    def top_five_reviews(self):
        reviews = self.reviews()
        sorted_reviews = sorted(reviews, key=lambda review: review.rating, reverse = True)
        return sorted_reviews[:5]

# there's a lot of bad code here, attempts to do what's going on here
    #

    #
    # recipe_rating_avg_local = Recipe.recipe_by_ratings()
    # recipes_at_party = {}
    # for recipe in recipe_rating_avg_local.keys():
    #     if recipe in self.recipes():
    #         recipes_at_party.append(recipe, recipe_rating_avg_local[recipe])
#shit, this doesn't work because we don't have ratings yet. We need to pull out the ratings
            #returns a list with the five review instances with the highest rating for the given recipe

        #if this doesn't work, build them into k,v pairs in a dictionary instead
        #then cycle through them using d.items()


    #DECORATORS

    #decorators for _name

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self, name):
       self._name = name

    @classmethod
    def test_function(cls):
        all_recipes = cls.all()
        print(all_recipes)
        filtered_recipes = list(filter(lambda recipe: len(recipe.ratings()) >= 1, all_recipes))
        print(filtered_recipes)
