# bulk-mixcloud-download (deprecated)
using selenium to bulk download all mixes from a mixcloud user via http://www.mixcloud-downloader.com/ hyperfast.

## requirements

install chomium webdriver and make sure the path to the executable is correct (see code)

example:

```chromedriver_path = "/usr/lib/chromium-browser/chromedriver"```

```pip install selenium```

change the url of the playlist, stream, search, ... you want to use in the code

```python3 mxdl.py```

## note
uses http://www.mixcloud-downloader.com/ which detects it's a bot after a while. 
