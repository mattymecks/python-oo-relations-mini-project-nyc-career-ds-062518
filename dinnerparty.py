from invite import Invite
from course import Course
from review import Review

class DinnerParty:

    _all = []

    def __init__(self, name):
        self._name = name
        DinnerParty._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all

    #INSTANCEMETHODS

    def invites(self):
        return [invite for invite in Invite.all() if self == invite.dinner_party]

    def guests(self):
        return [invite.guest for invite in self.invites()]

    def number_of_attendees(self):
        return len([invite.guest for invite in self.invites() if invite.rsvp_status == True])

    def courses(self):
        return [course for course in Course.all() if self == course.dinner_party]

    def recipes(self):
        return [course.recipe for course in self.courses()]

    def recipe_count(self):
        return len(self.recipes())

    def reviews(self):
        recipes = self.recipes()
        reviews = []
        for recipe in recipes:
            for review in Review.all():
                if recipe == review.recipe:
                    reviews.append(review)
        return reviews

        # reviews = [recipe.reviews(for review in recipes]
        # return [review for review in Review.all == review.recipe]

        #a list of reviews for the recipes of a given dinner party
        #going to need to pull all reviews, for each recipe, using a bunch of recipe object


    def highest_rated_recipe(self):
        all_reviews = self.reviews()
        sorted_reviews = sorted(all_reviews, key=lambda review: review.rating, reverse = True)
        return sorted_reviews[0].recipe



        recipe_rating_avg_local = Recipe.recipe_by_rating()
        recipes_at_party = {}
        for recipe in recipe_rating_avg_local.keys():
            if recipe in self.recipes():
                recipes_at_party.append(recipe, recipe_rating_avg_local[recipe])


#recipe with max rating

        #use self.recipes()

         #returns the highest rated recipe for the given dinner party
         #want to use the above function to create a data structure of recipe: [reivews]
         #then average each review?
         #Note: there's possible some functions within recipe that we could use?

    #DECORATORS

    #decorators for _name

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self, name):
       self._name = name
