# README #

A quick py script to download data from dukascopy using findatapy and upload to mongodb


## docker ##

### building ###

docker build -t findatapy .


### running mongo ###

docker run -v c:\projects\pr\python\mongo_data:/data/ -p 27017:27017 mongo


### running ###

docker run -it -v c:\projects\pr\python:/app findatapy python src/get.py
