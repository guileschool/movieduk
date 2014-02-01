from django.db import models
from core.models import *

class CustomUserManager(models.Manager):
  def create_user(self, username, email=None):
    print "==============DUKUSERCREATE"
    return self.model._default_manager.create(username=username, first_name='')

class DukUser(models.Model):
  print "==============DUKUSERCREATE"
  #social_auth requirements
  username = models.CharField(max_length=30)
  first_name = models.CharField(max_length=10, blank=True, null=True)
  last_name = models.CharField(max_length=10, blank=True, null=True)
  password = models.CharField(max_length=30)

  email = models.EmailField(blank=True, null=True)
  last_login = models.DateTimeField(blank=True, null=True)
  is_active = models.BooleanField(default=True)

  friends = models.ManyToManyField('self', blank = True, null = True, symmetrical=False)

  gender = models.CharField(max_length=10, blank=True)
  locale = models.CharField(max_length=10, blank=True)

  objects = CustomUserManager()

  own_movielist = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'own_movielist')
  liked_movielist = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'liked_movielist')
  hated_movielist = models.ManyToManyField(MovieList, blank=True, null=True, related_name = 'hated_movielist')

  watched_movie = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'watched_movie')
  liked_movie = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'liked_movie')
  hated_movie = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'hated_movie')
  watchlist_movie  = models.ManyToManyField(Movie, blank=True, null=True, related_name = 'watchlist_movie')

  def __unicode__(self):
    return self.username

  def is_authenticated(self):
    return True

  def facebook_extra_values(sender, user,response, details, **kwargs):     
    profile = user.get_profile()
    current_user = user 
    profile, new = UserProfile.objects.get_or_create(user=current_user)

    profile.gender = response.get('gender')
    profile.locale = response.get('locale')
    profile.save()
    return True
