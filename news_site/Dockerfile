# The image you are going to inherit your Dockerfile from
FROM python:3.10.8
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /django_news_site
# Set the /django_news_site directory as the working directory
WORKDIR /django_news_site
# Copies from your local machine's current directory to the django_news_site folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt
# Postgres integrate configurations
# RUN pip install --upgrade postgresql-client jpeg-dev
# RUN pip install --upgrade --virtual .tmp-build-deps \
#       gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
# Create a user that can run your container
# RUN adduser user
# USER user