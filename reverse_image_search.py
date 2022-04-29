# google_search_results : only 1 library!! library gaggoole

from serpapi import GoogleSearch
params = {
    "engine": "google_reverse_image",
    "image_url": "https://jongsul.s3.amazonaws.com/samplepng8.jpg",                  #image url !!!!!!!!!!!1
    "api_key": ""
    }

#get API response
search = GoogleSearch(params)
results = search.get_dict()
  #print(results)
image_results = results['image_results']
image_results2 = results['inline_images']

#1st link: image results_imagelink
#2nd link: inline image_link
#3rd link: inline image_source

print('\n')
i=1
for image in image_results:
    print('imagelink',i,':',image.get('link'),'\n')
    i=i+1
print('n')

i=1
for image in image_results2:
    print('link',i,':',image.get('link'),'\n')
    i=i+1
    print('n')
i=1
for image in image_results2:
    print('source',i,':',image.get('source'),'\n')
    i=i+1









