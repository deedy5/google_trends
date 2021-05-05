## google_trends

Simple Google Trends API

### Usage:
```python
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

gtrends(date=YYYYMMDD)
#trends on a given date, interval: today - 30 days ago.
```
### Example

realtime trends
```python
r = gtrends()
print(r)
```

trends on dates
```python
dates = [20210502, 20210501, 20210430, 20210429]
for date in dates:
    print(date)
    print(gtrends(date=date))
```
