#!/bin/bash
mycont=portrety_dev
myimage=${mycont}_image
docker stop $mycont && docker rm $mycont

docker build . -t $myimage && docker run --name $mycont -d $myimage tail -f /dev/null
