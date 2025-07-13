import datetime
import urllib.request as req
import re
import random


def search(expression):
    html=req.urlopen("https://www.youtube.com/results?search_query="+expression.replace(" ", "+"))
    ids=re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return ids



CLIENT_SECRET_FILE = 'credentitals.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "credentitals.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_local_server()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def postComment(videoId, cmts_list):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    comment=random.choice(cmts_list)


    request = youtube.commentThreads().insert(
        part="snippet",
        body={
          "snippet": {
            "videoId": videoId,
            "topLevelComment": {
              "snippet": {
                "textOriginal": comment
              }
            }
          }
        }
    )
    response = request.execute()
    print(comment, videoId)

comments_energy=["There is no free energy !!! #electroboom #debunkerBot",
          "#electroboom THERE IS NO FREE ENERGY !!! #debunkerBot",
          "That's why we always have nuclear power plants in 2024 ! 😂 #electroboom #debunkerBot",
          "Free energy ? Please be polite, don't tell bad words. #electroboom #debunkerBot",
          "The hardest part of free energy videos is to find where to hide the batteries #debunkerBot"]
comments_internet=["First, get free internet on your phone. Then, open a company to sale it and be rich ! Oh no, I forgot, there is no free internet ! #debunkerBot",
          "That's really interesting ! I always wanted free internet to watch dumb and useless videos like this on my phone ! #debunkerBot",
          "Use your free internet with care, it could be fake ! #debunkerBot"]


print("Ready to debunk !!!")
videos=[]
debunked=len(videos)
for video in search("free internet"):
    if video in videos:
        continue
    postComment(video, comments_internet)
    print(video)
    debunked+=1
    print(debunked, "debunked videos")
    videos.append(video)
    print(videos)
