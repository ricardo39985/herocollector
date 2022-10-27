from django.shortcuts import render, redirect
from .models import Hero, Photo
import os
import uuid
import boto3

# Create your views here.


def home(request):
    # request.user.hero_set.all().first().photo_set.all().first()

    if request.user.is_authenticated:
        return redirect('heroes')
    return render(request, 'home.html')


def heroes(request):
    return render(request, 'heroes.html')


def create_hero(request):
    print(request.FILES)
    if request.method == "POST":
        hero = Hero.objects.create(
            name=request.POST['name'], description=request.POST['description'], user_id=request.user.id)
        photo_file = request.FILES.get('photo-file',None)
        print(photo_file.size)
        if photo_file:
            s3 = boto3.client('s3')
            # need a unique "key" for S3 instead of using
            # the filename that was sent by the user
            key = uuid.uuid4().hex[:6] + \
                photo_file.name[photo_file.name.rfind('.'):]
            print(key)
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                Photo.objects.create(url=url, hero_id=hero.id)
                print(Photo.objects.all())
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
    return redirect('heroes')
