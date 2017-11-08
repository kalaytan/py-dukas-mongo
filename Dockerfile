FROM python:3.5

WORKDIR /app

# install dependencies
RUN pip install git+https://github.com/cuemacro/findatapy.git

#install pymongo
RUN pip install pymongo