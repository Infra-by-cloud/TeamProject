from django.db import models


class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname


class Home(models.Model):
    title = models.TextField(blank=True, null=True)
    background1 = models.ImageField(blank=True)
    background2 = models.ImageField(blank=True)
    background3 = models.ImageField(blank=True)
