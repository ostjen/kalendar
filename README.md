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

```
./kalendar list
```

