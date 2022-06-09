docker build --network=host -t hw7-write .
docker run --name kafka-producer --network kafka-network --rm hw7-write

