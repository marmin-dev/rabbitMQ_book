import rabbitpy


url = 'amqp://guest:guest@localhost:5672/%2F'
# RabbitMQ에 연결하는 새 Connection 객체를 만든다
connection = rabbitpy.Connection(url)
# 통신할 채널을 연다
channel = connection.channel()
# 메시지를 가져올 새 queue 객체를 만든다
queue = rabbitpy.Queue(channel, 'example')

# 메시지가 없을 때 까지 소비
while len(queue) > 0:
    message = queue.get()
    print('Message:')
    print(f'ID : {message.properties["message_id"]}')
    print(f'Time : {message.properties["timestamp"].isoformat()}')
    print(f'Body : {message.body}')
    message.ack()

