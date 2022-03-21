import pandas as pd
import requests
import time


API_KEY = 'AIzaSyBRUG4lT_KIxCZURDKPEMhjSu9WAF20y2I'

df = pd.DataFrame(columns= ['video_id', 'creator', 'video_name', 'publish_date', 'views', 'likes','comments'])
# first api call
web1 = 'https://www.googleapis.com/youtube/v3/search?key='
channel_id = 'UCadoq_XKuCvUvhHsr96WBjA'
params = '&part=snippet,id&order=date&maxResults=10000'
pageToken = ''
url = (web1 + API_KEY + '&channelId=' + channel_id + params + pageToken)
response = requests.get(url).json()
time.sleep(1)
for video in response['items']:
    if video['id']['kind'] == 'youtube#video':
        video_id = video['id']['videoId']
        channel_tittle = video['snippet']['channelTitle']
        video_name = video['snippet']['title']
        video_name = str(video_name).replace('*','')
        date = video['snippet']['publishedAt']
        date = str(date).split('T')[0]
# second api call
        video_stats_url = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + '&part=statistics&key=' + API_KEY
        response_video = requests.get(video_stats_url).json()

        views = response_video['items'][0]['statistics']['viewCount']
        likes = response_video['items'][0]['statistics']['likeCount']
        comments = response_video['items'][0]['statistics']['commentCount']


# save data in pandas dataframe
        df = df.append({'video_id': video_id, 'creator': channel_tittle, 'video_name': video_name, 'publish_date': date
                   , 'views': views, 'likes': likes, 'comments': comments}, ignore_index=True)

print(df)
df.to_excel('ama governor youtube data.xlsx')







