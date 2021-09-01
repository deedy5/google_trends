import json
import requests

__version__ = 0.9

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
               if specific categories do not work, leave category='all' or 'h';
    language = 'en-US', 'ru-RU', etc.;
    num_results = how many results to return, max num_results = 64;
    timezone = timezone offset, example: GMT-7 == -7*60 = '-420'.
    '''
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
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
    r = requests.get('https://trends.google.com/trends/api/realtimetrends', headers=headers, params=params)
    i = r.text.index('{')
    r = r.text[i:]
    r = json.loads(r)
    
    trending_story_ids = r["trendingStoryIds"]
    res = []
    for i in range(min(num_results, 64)):
        t = _get_realtime_trend(trending_story_ids[i], language=language, timezone=timezone)
        res.append(t)
    return res

def _get_realtime_trend(trending_story_id, language='en-US', timezone='-180'):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    params = {
        'hl': language,
        'tz': timezone,
        }
    r = requests.get(f'https://trends.google.com/trends/api/stories/{trending_story_id}', headers=headers, params=params)
    i = r.text.index('{')
    r = r.text[i:]
    r = json.loads(r)
    try:
        t = {
            "title": r["title"],
            "entity_names": r["entityNames"],
            "article_urls": [x["url"] for x in r["widgets"][0]["articles"]],
            }
        return t
    except:
        return
