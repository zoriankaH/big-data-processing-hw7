docker build --network=host -t hw7-read .
docker run --name kafka-consumer --network kafka-network -v /home/zorya/Documents/BigData/HW7/kafka_read:/kafka_read --rm hw7-read

