from invite import Invite
from review import Review

class Guest:

    _all = []

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all


    @classmethod
    def most_popular(cls):
        guests = cls.all()
        sorted_guests = sorted(guests, key=lambda guest: len(guest.invites()), reverse = True)
        return sorted_guests[0]

        # invites_per_guest =  {}
        # for name in names_composite:
        #     invites_per_guest[name] = invites_per_guest.get(name, 0) + 1
        #
        # most_invites = 0
        # most_popular = None
        # for guest, invites in invites_per_guest:
        #     if invites > most_invites:
        #         most_invites = invites
        #         most_popular = guest
        #
        # return most_popular

        #if you were being real much, you could convert this back into the corresponding
        #object, but we aren't doing that. Might be a potential weakness you could think
        #about how you'd shore up through

    @classmethod
    def toughest_critic(cls):
        all_guests = cls.all()
        sorted_guests = sorted(all_guests, key=lambda guest: guest.average_rating())
        return sorted_guests[0]
        # critics = {}
        # for guest in cls.all():
        #     critics[guest] = guest.ratings()
        #
        # avg_reviews = {}
        # for guest, reviews in critics.items():
        #     avg_review = sum(reviews)/len(reviews)
        #     avg_reivews[guest] = avg_review
        #
        # worst_review = 100
        # toughest_critic = None
        # for guest, average in avg_reivews.items():
        #     if average < worst_review:
        #         worst_review = average
        #         toughest_critic = guest
        #
        # return toughtest_critic

    @classmethod
    def most_active_critic(cls):
        guests = cls.all()
        sorted_guests = sorted(guests, key=lambda guest: len(guest.reviews()), reverse = True)
        return sorted_guests[0]
        # critics = {}
        # for guest in cls.all():
        #     critics[guest] = sum(guest.reviews())
        #
        # most_reviews = 0
        # most_active = None
        # for guest, number_reviews in critics.items():
        #     if number_reviews > most_reviews:
        #         most_reviews = number_reviews
        #         most_active = guest
        #
        # return most_active

    #INSTANCEMETHODS

    def invites(self):
        return [invite for invite in Invite.all() if invite.guest == self]

    #returns a list of all of the guest's invites

    def reviews(self):
        return [review for review in Review.all() if review.reviewer == self]

    def ratings(self):
        return [review.rating for review in self.reviews()]

#this is broken

    def number_of_invites(self):
        return len(self.invites())

    def rsvp(self, invite, rsvp_status):
        invite.rsvp_status = rsvp_status
        return invite.rsvp_status

    def review_recipe(self, recipe, rating, comment):
        new_review = Review(self, recipe, rating, comment)
        return recipe.reviews()
        # adds a guest's review with a rating and comment to a recipe. Returns the given recipe's



    def favorite_recipe(self):
        reviews = self.reviews()
        sorted_reviews = sorted(reviews, key=lambda review: review.rating, reverse = True)
        return sorted_reviews[0].recipe

    #     reviews_dict = {}
    #     for review in self.reviews():
    #          reviews_dict[review.recipe] = review.rating
    #     print(reviews_dict) #as a test for debugging. Aiming for a dict of object, rating pairs
        #if this works:
        #favorite_recipe = None
        #highest_rating = 0
        #for recipe, rating in reviews_dict:
            #if not highest_rating < rating:
                #highest_rating = rating
                #favorite_recipe = recipe
        #return favorite_recipes


        #returns the given guest's favorite recipe

        #going to need to

    #DECORATORS

    #decorators for _name

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self, name):
       self._name = name

    def average_rating(self):
        reviews = self.reviews()
        number_reviews = len(reviews)
        sum_reviews = sum([review.rating for review in self.reviews()])
        return sum_reviews/number_reviews
