# big-data-processing-hw7
Seventh Homework for the UCU Big Data Processing course.

Results are stored in results.pdf and also in Screenshots folder 

## Usage:
```
bash run-cluster.sh
bash create-topic.sh
bash kafka_write/build-run.sh
bash kafka_read/build-run.sh
bash shutdown-cluster.sh
```
## NOTE: 
In the Dockerfile in kafka_read directory change mounted volume to your own directory to which you wish to save the created files.
Also make sure that you have twcs.csv file in kafka_write directory.
