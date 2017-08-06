# morph-crawler

Crawler made with Selenium to crawl Facebook to parse some data of profiles without invade the user privacy.

We use all collected information to make a data_set to predict fake profiles, possible used by pedofiles, using [Chameleon-IA](https://github.com/ChameleonProject/chameleon-AI).

## Installation ##

`$ pip install selenium`

Make sure a browser is set up with selenium. Check [official selenium documentation](http://selenium-python.readthedocs.io/index.html) if needed.

## Set Up ##

First, rename `auth_settings_example.py`  to `auth_settings.py` and setup your facebook user and password.

```
auth = dict(
    email = 'facebook@account.com',
    password = 'password',
)

```

We won't store your account and/or password. The login() function is only one to use your infos to authenticate your account and start algorithm.

Second, you need to set a [list.txt](https://github.com/ChameleonProject/morph-crawler/blob/master/crawler.py#L84) with your own links, we won't provide the scrapper algorithm to fetch all profile links at one facebook group in this version.

## Run ##

`$ python crawler.py`

## Output ##

The data_set will be created like [result.txt](https://github.com/ChameleonProject/morph-crawler/blob/master/results.csv) to input in [Chameleon-IA](https://github.com/ChameleonProject/chameleon-AI).

You can change de format or the data you want to collect, just create similar functions to the one available in this source code.
