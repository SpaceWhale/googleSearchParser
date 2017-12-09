# googleSearchParser
crawl a google search dump and print searches chronologically.

# How To
* Sign into your google account and download a zip of [your search history](https://takeout.google.com/settings/takeout/downloads)
![alt text](https://github.com/SpaceWhale/googleSearchParser/blob/master/images/001.png "search takeout")
* Clone the repository and unzip the search history file inside of the project folder.
```
mkdir ~/code/
git clone https://github.com/SpaceWhale/googleSearchParser.git ~/code/googleSearchParser
unzip ~/Downloads/takeout*.zip -d ~/code/googleSearchParser/
```

* Install the requirements
```
pip install -r ~/code/googleSearchParser/requirements.txt
```

* run the application
```
python ~/code/googleSearchParser/googleSearchParser.py
```
