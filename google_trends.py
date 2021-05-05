import json
import requests

__version__ = 0.2

def _get_json(date, country, language, timezone): # timezone '-420'(GMT-7 == -7*60)
    # get json from google trends    
    params = {
        'hl': language,
        'tz': timezone,
        'ed': date,
        'geo': country,
        }
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    r = requests.get("https://trends.google.com/trends/api/dailytrends", headers=headers, params=params)
    i = r.text.index('{')
    r = r.text[i:]
    r = json.loads(r)    
    return r

def gtrends(date=None, country='US', language='en-US', timezone='-180'): # timezone '-420'(GMT-7 == -7*60)
    # date =  YYYYMMDD, else realtime trends (max 30 days ago).
    j = _get_json(date=date, country=country, language=language, timezone=timezone)
    r = j['default']['trendingSearchesDays'][0]
    data = r['trendingSearches']
    res = []
    for r in data:
        t = r['title']['query']
        res.append(t)  
    return res
