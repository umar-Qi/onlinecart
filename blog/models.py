from django.db import models

# Create your models here.
class blogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500)
    contenthead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500)
    contenthead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500)
    contenthead2 = models.CharField(max_length=5000, default="")
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to="mart/images", default="")

    def __str__(self):
        return self.title