import json
import requests

__version__ = '1.0'

def gtrends(*args, **kwargs):
    print("Function 'gtrends' is deprecated: renamed to 'daily_trends'")
    return daily_trends(*args, **kwargs)

def daily_trends(date=None, country='US', language='en-US', timezone='-180'):
    ''' Google daily search trends
    date = YYYYMMDD, example: 20210810, trends on a given date, interval: today - 30 days ago;
    country = 'US', 'RU', etc.;
    language = 'en-US', 'ru-RU', etc.;
    timezone = timezone offset, example: GMT-7 == -7*60 = '-420'.
    '''    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    params = {
        'hl': language,
        'tz': timezone,
        'ed': date,
        'geo': country,
        }    
    r = requests.get("https://trends.google.com/trends/api/dailytrends", headers=headers, params=params)
    i = r.text.index('{')
    r = r.text[i:]
    r = json.loads(r)    
    r = r['default']['trendingSearchesDays'][0]
    data = r['trendingSearches']
    res = []
    for element in data:
        t = element['title']['query']
        res.append(t)  
    return res

def realtime_trends(country='US', category='all', language='en-US', num_results=20, timezone='-180'):
    ''' Google realtime search trends    
    country = 'US', 'RU', etc.;
    category = 'all' (all), 'b' (business), 'e' (entertainment), 
               'm' (health), 's' (sports), 't' (sci/tech), 'h' (top stories);
    language = 'en-US', 'ru-RU', etc.;
    num_results = how many results to return, max num_results = 200;
    timezone = timezone offset, example: GMT-7 == -7*60 = '-420'.
    '''
    with requests.Session() as s:
        s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"})
        params = {
            'hl': language,
            'tz': timezone,
            'cat': category,
            'fi': '0',
            'fs': '0',
            'geo': country,
            'ri': '300',
            'rs': f'{num_results}',
            'sort': '0',
            }
        # request json with real time trends
        r = s.get('https://trends.google.com/trends/api/realtimetrends', params=params)
        # fix the json and load it as a dictionary
        i = r.text.index('{')
        r = r.text[i:]
        r = json.loads(r)
        # extract information from json
        data = r["storySummaries"]["trendingStories"]
        res, ids_cache = [], set()
        for element in data:
            res.append({"title": element["title"],
                        "entity_names": element["entityNames"],
                        "article_urls": [x["url"] for x in element["articles"]],})
            ids_cache.add(element["id"])

        # if not enough results, request additional jsons by trending_story_ids
        trending_story_ids = r["trendingStoryIds"]
        while len(res) < num_results:
            id_list = []
            for trending_story_id in trending_story_ids:
                if trending_story_id not in ids_cache:
                    id_list.append(trending_story_id)
                if len(id_list) == 20:
                    break
            if not id_list:
                break
            ids_cache.update(id_list)
            params = {
                'hl': language,
                'tz': timezone,
                'cat': category,
                'id': id_list,
                }
            r = s.get('https://trends.google.com/trends/api/stories/summary', params=params)
            i = r.text.index('{')
            r = r.text[i:]
            r = json.loads(r)
            data = r["trendingStories"]
            for element in data:
                res.append({"title": element["title"],
                            "entity_names": element["entityNames"],
                            "article_urls": [x["url"] for x in element["articles"]],})
                ids_cache.add(element["id"])

        ''' ----- Another way, if not enough results -----
        # request additional jsons per each trending_story_id
        trending_story_ids = r["trendingStoryIds"]
        i = 0
        while len(res) < num_results and len(res) < len(trending_story_ids):
            if trending_story_ids[i] not in ids_cache:
                r = s.get(f'https://trends.google.com/trends/api/stories/{trending_story_ids[i]}?hl={language}&tz={timezone}')
                i = r.text.index('{')
                r = r.text[i:]
                r = json.loads(r)
                res.append({"title": r["title"],
                            "entity_names": r["entityNames"],
                            "article_urls": [x["url"] for x in r["widgets"][0]["articles"]],})
            i += 1
        '''
    return res
