# ContestTwitterMN
Tweet a gnome every few hours and show upcoming programming contests from www.hackerrank.com/calendar/feed.rss

## Development:

### Install third-party libraries
```sh
pip install -r requirements.txt -t lib/
```

### Local settings
```sh
mv ContestTweets/local.settings.py ContestTweets/local_settings.py
```
Configure your settings in `local_settings.py`.


### Run local server
```sh
dev_appserver.py .
```

### Run tests
```sh
manage.py test
```

### Upload

```sh
appcfg.py -A contestmn update .
```
