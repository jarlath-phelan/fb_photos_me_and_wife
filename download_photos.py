import urllib
import ast

YOUR_ACCESS_TOKEN='goes here' # https://developers.facebook.com/tools/explorer?fql

# fb photos of me
query = "select object_id from photo_tag where subject=me()"
params = urllib.urlencode({'q': query, 'access_token': YOUR_ACCESS_TOKEN})

url = "https://graph.facebook.com/fql?" + params
photos_of_me = eval(urllib.urlopen(url).read())

# fb photos of my wife
query = "select object_id from photo_tag where subject=199701180"
params = urllib.urlencode({'q': query, 'access_token': YOUR_ACCESS_TOKEN})

url = "https://graph.facebook.com/fql?" + params
photos_of_nathalie = eval(urllib.urlopen(url).read())


# fb photos of both of us - links
photos_of_us_ids=""
for photo_of_me in photos_of_me['data']:
    for photo_of_nathalie in photos_of_nathalie['data']:
        if photo_of_me==photo_of_nathalie:
            if photos_of_us_ids=='':
                photos_of_us_ids = str(photo_of_me['object_id'])
            else:
                photos_of_us_ids = photos_of_us_ids +', ' + str(photo_of_me['object_id'])
                               
#print photos_of_us_ids
query = "select src_big from photo where object_id in (" + photos_of_us_ids + ")"
params = urllib.urlencode({'q': query, 'access_token': YOUR_ACCESS_TOKEN})

url = "https://graph.facebook.com/fql?" + params
photos_of_us_links = eval(urllib.urlopen(url).read())
#print photos_of_us_links

# fb photos of both of us - download
i=0;
for photo_of_us_links in photos_of_us_links['data']:
    #print photo_of_us_links['src_big']
    #print photo_of_us_links['src_big'].replace("\\", "")
    img=photo_of_us_links['src_big'].replace("\\", "")
    i+=1
    urllib.urlretrieve(img, r'C:\\Temp\\Facebook_Photos\\' + str(i) + '.jpg')
