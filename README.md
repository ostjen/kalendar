# kalendar
A simple command line google calendar tool

### Requirements 

1. create a virtualenv

```
virtualenv .venv --python=`which python3`
```

2. activate it
```
source .venv/bin/activate
```

3. install requirements
```
pip install -r requirements/base.txt
```

### Setup

* enable your google calendar api [here](https://developers.google.com/calendar/quickstart/python) and paste the credentials.json in the repo root folder

* authorize kalendar
  ```
  ./kalendar setup
  ```

## Actions

### List

list upcoming calendar events


optional arguments:
  -h, --help  show this help message and exit
  -c C        calendar name(default calendar located in config/settings.py)


```
./kalendar list
```

```
{ 'end': '2020-09-24 -> 12:00',
  'start': '2020-09-24 -> 11:00',
  'summary': 'test event 1'}


{ 'end': '2020-09-25 -> 13:00',
  'start': '2020-09-25 -> 12:00',
  'summary': 'test event 2'}


{ 'end': '2020-09-26 -> 16:30',
  'start': '2020-09-26 -> 15:30',
  'summary': 'test event 3'}

```

### Find

Find event by name

```
./kalendar  find -n "test event 2"
```

optional arguments:
  -h, --help  show this help message and exit

required arguments:
  -n N        event name


```
{ 'end': '2020-09-25 -> 13:00',
  'start': '2020-09-25 -> 12:00',
  'summary': 'test event 2'}
```


### Create

Create event

optional arguments:
  -h, --help  show this help message and exit
  -n N        event name / summary
  -d D        description
  -c C        calendar(default calendar located in config/settings.py)

required arguments:
  -s S        start time
  -e E        end time
  
```
./kalendar create -n "foo" -d "event-description" -s "24/09/2020-10:30" -e "24/09/2020-16:00"
```
```
created event foo

```



