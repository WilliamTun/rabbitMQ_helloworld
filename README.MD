# Instructions

### Set up rabbitMQ 

#### First time set up
```
docker pull rabbitmq:3-management
docker run -d -p 15672:15672 -p 5672:5672 --name rabbit-test-for-medium rabbitmq:3-management
```
You can see the rabbitMQ server UI on local machine by going to http://localhost:15672 
and login as username "guest" and password "guest"

#### Set up rabbitMQ upon return
if the docker container is already in local sytstem, open docker UI, go to images on the left pane,
then click "run" on rabbitmq image. Then as before call:
```
docker pull rabbitmq:3-management
docker run -d -p 15672:15672 -p 5672:5672 --name rabbit-test-for-medium rabbitmq:3-management
```

### Calling the sender reciever scripts

1. install pika library into the environment
2. edit the mypath variable in send.py to the directory you wish to constantly monitor for new files
3. run the recieve.py script
4. open a new terminal, and run the send.py script
5. when a new file is added to the directory of interest, a "hello world" message is sent to the reciever, that in turn calls echo "hello world"


### Resources:
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
https://www.rabbitmq.com/tutorials/tutorial-two-python.html
https://www.rabbitmq.com/tutorials/tutorial-three-python.html
https://betterprogramming.pub/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
https://www.cloudamqp.com/blog/part2-3-rabbitmq-for-beginners_example-and-sample-code-python.html
