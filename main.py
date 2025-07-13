import datetime
import urllib.request as req
import re
import random


def search(expression):
    html=req.urlopen("https://www.youtube.com/results?search_query="+expression.replace(" ", "+"))
    ids=re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return ids



CLIENT_SECRET_FILE = '../videoChanger/credentitals.json'
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
client_secrets_file = "../videoChanger/credentitals.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_local_server()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def postComment(videoId):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    comment=random.choice(comments)


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

comments=["There is no free energy !!! #electroboom #debunkerBot",
          "#electroboom THERE IS NO FREE ENERGY !!! #debunkerBot",
          "That's why we always have nuclear power plants in 2024 ! 😂 #electroboom #debunkerBot",
          "Free energy ? Please be polite, don't tell bad words. #electroboom #debunkerBot",
          "The hardest part of free energy videos is to find where to hide the batteries #debunkerBot"]
comments=["First, get free internet on your phone. Then, open a company to sale it and be rich ! Oh no, I forgot, there is no free internet ! #debunkerBot",
          "That's really interesting ! I always wanted free internet to watch dumb and useless videos on my phone ! #debunkerBot",
          "Use your free internet with care, it could be fake ! #debunkerBot"]


print("Ready to debunk !!!")
videos=['0lRTIOyH0nE', 'Ql5hRkv-m7A', 'odvshmwPXmk', '39maxnc-OZA', 'TG2jeuDTm2s', 'SGtpjEcQGvc', '54Ya959OOjM', 'HamRpW6EY9w', 'xhj20UflMQ0', 'QWfUQSUqRN8', 'sdKGxkRdDa4', 'isFaAA9dT_w', 'GzugEID1mGM', 'w1w37btgx-M', '2SDWKuxP2fM', 'tfLKU1dvqH8', 'hpDwTtE2OGo', 'vSUjv_qAn_Y', '5hU_x20IY80', 'ZF8prOHgxZg', 'f0GnB0kYli0', 'zLYmye-BvP4', 'vf6sghP9VPc', 'hJ2sFYFESE0', 'OOTv_YM-R8Y', 'tg3bcIuBSiA', 'pyNqzq71x6Q', 'azaBuxtuZgA', 'GBizDlpesi0', 'U0YtcNVn2L4', 'xBLlk6xd58E', 'YafUOdl59jU', 'DsMl3e9WdzA', 'TJXm8THHksw', 'HA-ydM93ejk', 'Zze8doj28cI', 'RVQ2NShGopU', 'tdADWnkZPng', 'buKA0jesMd8', '04OWaIYTskc', '2M3jeVPzc88', 'Z06UE4HVtZ0', 'ylHtVpYyvO8', 'bnlPR8Pn7-A', 'CsJlt2jY-9M', 'IO9ihx-N1LA', 'LrhS-pIHZL4', '-c5WLnggp3I', 'BSdSDfOWbNs', '228pPP62zJM', 'YKfFt9aS9dc', 'HGCqTGyefKc', 't0Je_GFm6mQ', 'agOY3F55bqM', 'Eu_kyNaAaOQ', 'vQBdSm8kF1c', 'ePH6vkqAeB4', 'VuqiiOj_Pj8', 'IoSLGuo2b_A', 'qVpv3WNbm-k', '-yU9jM81z_w', '5Rl1ozW31Lk', 'Y8isKhWEDxE', '9rRfh4kWcQ0', 'R-7xQ4I8c60', 'KpKpNdQYLCI', 'DZZ7BBYWHwQ', 'L28bacWmQpg', '--ZiSeo_G_M', '0e47W5mzcyU', 'S4GhyLAVcTw', 'tkYdHQwiPNM', 'zv2rzIcEJFY', 'eaXVBa7hno8', '4vKOLg_c3LQ', 'gBipk8CYOGM', '4d-139bhhjQ', 'gmUAcKyab_Q', 'I6oNIwmzg1E', 'ZwEwfpSf8Ho', 'SNJ_PIBWDxY', '_-RUQXD3rvQ', 'V6UXqS8U7is', 'eF39d5in6Kc', 'gWeTRTvOl9A', 'D_rTacQdQho', '9VcMSHJqj_M', 'fk_XNoxkmYA', 'CYXZVQiUNlg', 'V6tH3a9PyQ4', '7Jp_-HXaDgQ', 'jvZBRHiLKiE', 'pNEax6qW_iw', 'NPfATzKSYP0', 'qCQLqKEEECA', 'Oyc9c1q0RRU', 'QRH8ksmRCuU', 'ljxiSc9LF3c', 'Qzk1VPJNg6Y', 'ShOdi05VjXE', 'PCq983v-e4k', 'IOvdp_04KRQ', 'vSaE1Vrk12I', '92nsAaMvQcs', 'FFTju7B4q1Q', 'DPgB_GsYAYg', '8cl9oUh98y0', 'nVLflX3zyK0', '_mzpdZ9FT2M', 'qCjOt8foehQ', 'y96MaLJ8Z5k', 'qnBjNoK1TVQ', 'R9Nb-o-okf4', 'PKwyKqPaxoA', 'w5WYHZHll_s', 'iBFzAHicL2U', 'AE273E167rE', '2Oz2_3sFajQ', 'sT-WcjR4L3g', 'LCfHMjhArKA', 'bcbCK8EX2J4', 'hHpKdeIB4fQ', 'on1Ua2-uYWQ', '-J4knMYf_nE', 'wlCKF1HqbFg', 'BMk_mVC_z0U', 'kYeAEXepUb4', 'GEICT_6BhWE', '9_VMpGZWOBc', 'EPjSO2u_PA0', '8cEOz6hsgDM', 'eR1SR0Usd_4', '3OCcY5u4nMo', 'f0-amM95b-s', 'JLS83-Ly_7U', 'MUG5bppMFtg', '9W1ESRkAHZA', 'IstNvqbJZbU', 'vtGqhplx7-A', 'kKGCePREu5A', 'KgxqcX2G5qI', 'NNt31CF_cd4', '7LoLYFCm-sc', 'xjXCJe8LwC0', 'am_Jhr_qWzA', 'MLoVoYJWmzE', 'XRpfCwPxVoA', '6psqtrhpfPo', '9rtQzrvNXzE', 'p_r-1gNzTTI', 'yy100w844Zw', 'LpV2mjCWm0g', 'hvnUkY6mLtA', 'hq29qbMd6wk', 'M9x8VxAY2sQ', 'BhCRUHQ3p3Y', 'Ub7PWaZAw_Y', '9_wVAp8xm44', '3LdtELKZ_Ys', 'CeoDXwZkUGY', 'GEjWcVZALms']
debunked=len(videos)
for video in search("free internet"):
    if video in videos:
        continue
    postComment(video)
    print(video)
    debunked+=1
    print(debunked, "debunked videos")
    videos.append(video)
    print(videos)