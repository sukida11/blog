from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(null=True, blank=True, upload_to='blog/profile')
	reg_date = models.DateTimeField(default=timezone.now())
	bio = models.TextField()
	age = models.IntegerField()
	city = models.CharField(max_length=200)

	def __str__(self):
		return self.user.username


class Chanel(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=300, unique=True)
	description = models.TextField()
	reg_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.name


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	channel = models.ForeignKey(Chanel, on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	text = models.TextField()
	count_like = models.IntegerField(default=0)
	date_pub = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.title


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now())
	comment_text = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.author}: {self.comment_text[:20]}'


class CommentReply(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_to_reply = models.ForeignKey(Comment, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now())
	reply_text = models.CharField(max_length=200)

	def __str__(self):
		return f'"{self.reply_text[:15]}" от {self.author.username}'


class UserLiked(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} лайкнул "{self.post.title}"'


class Subscriber(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chanel = models.ForeignKey(Chanel, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} подписан "{self.chanel.name}"'


class UserRoot(models.Model):
	owner = models.ForeignKey(User, related_name='channel_owner',on_delete=models.CASCADE)
	worker = models.ForeignKey(User, related_name='channel_worker',on_delete=models.CASCADE)
	channel = models.ForeignKey(Chanel, on_delete=models.CASCADE)
	roots = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.worker.username} администрирует "{self.chanel.name}, как {self.roots}"'
