# Rabbit MQ Python

Experimenting messaging queue with RabbitMQ

1. init virtual environment
```shell
make s
```

2. install all dependencies
```shell
make i 
```

3. [Optional] insatall all dependencies
```shell
make u
```

4. init pre-commit configurations see [.pre-commit-config.yaml](.pre-commit-config.yaml)
```shell
make pc
```

5. init the rabbitMQ container
```shell
make rmq
```

## rabbitMQ commands
1. [List queues and messages] inside the rabbitmq container:
```shell
rabbitmqctl list_queues
```