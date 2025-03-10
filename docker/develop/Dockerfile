FROM debian:stable
MAINTAINER gm@gm.lv

# Avoid interactive cli blockers
ENV DEBIAN_FRONTEND noninteractive

# Install basic stuff
RUN apt-get update -yq \
    && apt-get install -yq apt-utils

RUN apt-get install -y --no-install-recommends \
    apt-transport-https lsb-release ca-certificates gnupg \
    locales less nano curl wget zip unzip tree \
    git openssh-client

# Update locales
RUN echo "Europe/Riga" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# lv_LV.UTF-8 UTF-8/lv_LV.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

# Install python and service runner
RUN apt-get install -y --no-install-recommends \
    python3 python3-venv python3-pip \
    supervisor

# Create virtualenv
RUN python3 -m venv /srv/venv

# Activate virtual environment
ENV PATH="/srv/venv/bin:$PATH"

# Install services python dependecies
COPY ./data/requirements.txt  /root/requirements.txt
RUN pip3 install -r /root/requirements.txt && rm /root/requirements.txt

# Supervisord configuration
COPY ./conf/supervisord.dev.conf  /etc/supervisor/conf.d/dev.conf
COPY ./post-install.bash  /root/post-install.bash

# Set work directory and start php webserver
WORKDIR /srv/project/src/
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]

EXPOSE 8000
