from django.db import models
from django.core.urlresolvers import reverse
 

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_name = models.CharField(blank = True,max_length=100)
    image_field = models.BooleanField(default=False)
    code_post = models.BooleanField(default=False)
    section1 = models.TextField()      
    code1 = models.TextField(blank = True)
    section2 = models.TextField(blank = True)
    code2 = models.TextField(blank = True)
    section3 =  models.TextField(blank = True)
    code3 =  models.TextField(blank = True)
    url = models.URLField(unique=True, blank = True, max_length=255)
    url_description = models.CharField(max_length=250, blank = True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
