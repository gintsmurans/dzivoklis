#!/bin/bash

if [ "$1" = "install" ]; then

    # Down docker
    docker-compose down --remove-orphans
    docker-compose rm

    # This is required for node_modules caching
    cp src/requirements.txt docker/develop/data/

    # Build up
    docker-compose up --build --force-recreate --detach

    # After build we don't need this anymore
    rm docker/develop/data/requirements.txt

    # Run post install comands
    docker-compose exec develop /root/post-install.bash

elif [ "$1" = "start" ]; then

    docker-compose start

elif [ "$1" = "stop" ]; then

    docker-compose stop

elif [ "$1" = "uninstall" ]; then

    docker-compose down -v --rmi all --remove-orphans

elif [ "$1" = "deploy" ]; then

    if [[ ! -f docker/deploy/data/id_rsa ]] ; then
        echo 'Cant find `docker/deploy/data/id_rsa`, aborting...'
        exit
    fi

    # Build up
    # docker-compose -f docker-compose.deploy.yml up --build --force-recreate

else

    echo "No command presented: install|start|stop|uninstall|deploy"

fi
