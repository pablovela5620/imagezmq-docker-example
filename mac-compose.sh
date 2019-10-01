IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
xhost + $IP
DOCKER_MACHINE=webcam
docker-machine start webcam
eval $(docker-machine env webcam)
vboxmanage controlvm "webcam" webcam attach .1
echo "If you get error, change IP in compose to $IP"
docker-compose build;
docker-compose up