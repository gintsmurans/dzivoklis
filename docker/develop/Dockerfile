FROM debian:stable
MAINTAINER gm@gm.lv

# Avoid interactive cli blockers
ENV DEBIAN_FRONTEND noninteractive

# Install basic stuff
RUN apt-get update -yq \
    && apt-get install -yq apt-utils

RUN apt-get install -yq apt-transport-https lsb-release ca-certificates \
        wget curl unzip git supervisor sudo build-essential locales

# Update locales
RUN echo "Europe/Riga" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# lv_LV.UTF-8 UTF-8/lv_LV.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

# Install python
RUN apt-get -yq install python3 python3-pip

# Install services python dependecies
COPY ./requirements.txt  /root/requirements.txt
RUN pip3 install -r /root/requirements.txt && rm /root/requirements.txt

# Supervisord configuration
ADD ./supervisord.web.conf  /etc/supervisor/conf.d/web.conf
ADD ./supervisord.services.conf  /etc/supervisor/conf.d/services.conf
ADD ./post-install.bash  /root/post-install.bash

# Fix www-data home directory
RUN mkdir -p /var/www/ \
    && chown www-data:www-data /var/www/ \
    && mkdir -p /srv/sites/web/ \
    && chown www-data:www-data /srv/sites/web/

# Set work directory and start php webserver
WORKDIR /srv/sites/web/
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]

EXPOSE 9100
EXPOSE 4100
