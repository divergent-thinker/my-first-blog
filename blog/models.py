from django.db import models
from django.utils import timezone

#class Post(models.Model): - this line defines our model (it is an object).
class Post(models.Model):
	#class is a special keyword that indicates that we are defining an object.
# Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespaces). Always start a class name with an uppercase letter.
#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.


#Now we define the properties we were talking about: 
#title, text, created_date, published_date and author. 
#To do that we need to define a type of each field (Is it text? 
#A number? A date? A relation to another object, i.e. a User?).

    author = models.ForeignKey('auth.User')
#models.ForeignKey - this is a link to another model.

    title = models.CharField(max_length=200)
#models.CharField - this is how you define text with a limited number of characters.

    text = models.TextField()
 #models.TextField - this is for long text without a limit. 
 #Sounds ideal for blog post content, right?

    created_date = models.DateTimeField(
            default=timezone.now)
  #models.DateTimeField - this is a date and time.

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
#What about def publish(self):? It is exactly the publish method 
#we were talking about before. def means that this is a 
#function/method and publish is the name of the method. 
#You can change the name of the method, if you want. 
#The naming rule is that we use lowercase and underscores 
#instead of whitespaces. For example, a method that calculates 
#average price could be called calculate_average_price.

    def __str__(self):
        return self.title
#Methods often return something. 
#There is an example of that in the __str__ method. 
#In this scenario, when we call __str__() we will get a text 
#(string) with a Post title.



