from .RandomStrings import GenerateRandomString
from users.models import User




class UserSlugManager():
    def generateUserSlug(self):
        slug = GenerateRandomString.randomStringGenerator(90)
        try:
            User.object.get(slug=slug)
            self.generateUserSlug()
        except Exception as e:
            return slug
