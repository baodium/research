import json
import re
from googleapiclient.discovery import build

# normalize date
API_KEY= 'AIzaSyCdOGjynFqrd5A-gkKKeYjqs0UIMP7FGjc' #'AIzaSyBU90NCoIdkvmBkjDqjF6wj3nBtoE_6xfA' # # # ## # # #

service = build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

# read json file
with open('toxicVideo.json', encoding='utf-8-sig') as f:
    data = json.load(f)

output = []

for x in data:
    comment = {}
    try:
        comment['id'] = x['id']
        comment['comment_id'] = x['comment_id']
        comment['video_id'] = x['video_id']
        comment['commenter_name'] = x['commenter_name']
        comment['commenter_id'] = x['commenter_id']
        comment['comment_displayed'] = x['comment_displayed']
        comment['comment_original'] = x['comment_original']
        comment['likes'] = x['likes']
        comment['published_date'] = x['published_date']
        comment['updated_date'] = x['updated_date']
        comment['total_replies'] = x['total_replies']
        comment['replyto'] = x['replyto']
    except:
        comment['id'] = ''
        comment['comment_id'] = ''
        comment['video_id'] = ''
        comment['commenter_name'] = ''
        comment['commenter_id'] = ''
        comment['comment_displayed'] = ''
        comment['comment_original'] = ''
        comment['likes'] = ''
        comment['published_date'] = ''
        comment['updated_date'] = ''
        comment['total_replies'] = ''
        comment['replyto'] = ''
    
    try:
        analyze_request = {
                    'comment': { 'text': comment['comment_displayed'] },
                    'requestedAttributes': {'TOXICITY': {}}
                }  
        probability = service.comments().analyze(body=analyze_request).execute()
        comment['comment_toxicity'] = probability['attributeScores']['TOXICITY']['summaryScore']['value']

    except:
         comment['comment_toxicity']  = 0.0

    output.append(comment)
    #output_sorted = sorted(output, key=lambda k: k['comment_toxicity'])

    # # print(output_sorted)

# write json file
with open('Result.json', 'w+') as outfile:
    json.dump(output, outfile)