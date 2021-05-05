## google_trends

Simple Google Trends API


### Install

```
pip install -U google_trends
```

### Usage:
```python
from google_trends import gtrends

gtrends(date=None, country='US', language='en-US', timezone='-180')
    '''
    date = date of interest, allowable interval: today - 30 days ago;
    country = two letter country abbreviation;
    timezone = timezone Offset, GMT-7 == -7*60 = '-420',
                                GMT-8 == -8*60 = '-480';
    language = language.
    '''
 
 
gtrends()
#realtime trends

gtrends(YYYYMMDD)
#trends on a given date, interval: today - 30 days ago.
```
