from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    author=models.CharField(max_length=100) #작성자를 직접 입력해줘야함.
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

