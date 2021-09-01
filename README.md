[![Python >= 3.6](https://img.shields.io/badge/python->=3.6-red.svg)](https://www.python.org/downloads/) [![](https://badgen.net/github/release/deedy5/google_trends)](https://github.com/deedy5/google_trends/releases) [![](https://badge.fury.io/py/google-trends.svg)](https://pypi.org/project/google_trends)
## google_trends

Simple Google Trends API


### Install

```python3
pip install -U google_trends
```

### Usage:
*Warning: gtrends renamed to daily_trends*
```python3
from google_trends import daily_trends, realtime_trends
```
**1. Google daily search trends**
```python3
daily_trends(date=None, country='US', language='en-US', timezone='-180')
    ''' Google daily search trends
    
    date = YYYYMMDD (example: 20210810) - trends on a given date, interval: today - 30 days ago;
    country = 'US', 'RU', etc.;
    language = 'en-US', 'ru-RU', etc.;
    timezone = timezone offset, example: GMT-7 == -7*60 = '-420'.
    '''

# trends today
today_trends = daily_trends(country='GB')
print(today_trends)

#trends on a given date, interval: today - 30 days ago.
date_trends = daily_trends(20210810)
print(date_trends)
```
---
**2. Google realtime search trends**
```python3
realtime_trends(country='US', category='all', language='en-US', num_results=20, timezone='-180')
    ''' Google realtime search trends

    country = 'US', 'RU', etc.;
    category = 'all' (all), 'b' (business), 'e' (entertainment), 
               'm' (health), 's' (sports), 't' (sci/tech), 'h' (top stories);
    language = 'en-US', 'ru-RU', etc.;
    num_results = how many results to return, max num_results = 64;
    timezone = timezone offset, example: GMT-7 == -7*60 = '-420'.
    '''
 
real_trends = realtime_trends(country='DE', category='t', language='en-UK', num_results=2)
print(real_trends)

[
{
'title': 'Sony, Funimation, PlayStation Network, Anime, Aniplex', 
'entity_names': ['Sony', 'Funimation', 'PlayStation Network', 'Anime', 'Aniplex'], 
'article_urls': ['https://www.gamepro.de/artikel/sony-crunchyroll-ps-plus-premium-abo,3372448.html', 'https://www.play3.de/2021/08/11/playstation-plus-premium-variante-mit-crunchyroll/', 'https://www.pcgames.de/PlayStation-Plus-Thema-260472/News/geruechte-um-premium-abo-mit-anime-inhalten-1377545/', 'https://stadt-bremerhaven.de/crunchyroll-uebernahme-durch-sony-abgeschlossen/', 'https://playfront.de/playstation-plus-premium-arbeitet-sony-an-einem-neuen-abo/', 'https://www.netzwelt.de/news/192097-milliardendeal-sony-uebernimmt-crunchyroll-bald-nur-noch-ultimativer-anime-streamingdienst.html', 'https://www.pattotv.de/animenews/sonys-funimation-global-group-schliesst-uebernahme-von-crunchyroll-ab/', 'https://shonakid.de/milliardendeal-sony-schliesst-ubernahme-von-crunchyroll-ab-und-jetzt-63014/', 'https://www.playcentral.de/anime-anbieter-crunchyroll-funimation-fusionieren/', 'https://game7.de/playstation-network/news/premium-version-plus-geplant-kkm/']
}, 
{
'title': 'Diablo II, Blizzard Entertainment, Xbox One', 
'entity_names': ['Diablo II', 'Blizzard Entertainment', 'Xbox One'], 
'article_urls': ['https://www.giga.de/news/diablo-2-resurrected-blizzard-laesst-euch-kostenlos-reinschnuppern-so-gehts/', 'https://www.heise.de/news/Diablo-2-Resurrected-Offene-Beta-beginnt-am-20-August-6160795.html', 'https://www.tz.de/leben/games/diablo-resurrected-2-beta-starttermin-fuer-early-access-steht-fest-blizzard-games-zr-90914078.html', 'https://www.golem.de/news/resurrected-alte-savegames-muessen-bei-beta-von-diablo-2-noch-warten-2108-158820.html', 'https://www.netzwelt.de/news/192079-diablo-2-resurrected-blizzard-kuendigt-beta-start-pc-konsolen.html', 'https://www.gamepro.de/artikel/diablo-2-resurrected-starttermin-beta-offiziell,3372455.html', 'https://www.spieletipps.de/n_49329/', 'https://winfuture.de/news,124553.html', 'https://www.eurogamer.de/articles/2021-08-11-diablo-2-resurrected-offizielle-startzeiten-der-beta-bestaetigt', 'https://www.pcgameshardware.de/Diablo-2-Resurrected-Spiel-73212/News/Open-Beta-Starttermin-bekannt-gegeben-1377542/']
}
]
```
