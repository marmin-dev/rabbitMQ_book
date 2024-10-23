import rabbitpy

# 연결할 URL 지정하기
url = 'amqp://guest:guest@localhost:5672/%2F'

# 위 URL 을 사용하여 RabbitMQ 에 연결하기
connection = rabbitpy.Connection(url)
# 커넥션에서 새로운 채널 열기
channel = connection.channel()

# 채널을 인자로 전달해서 새로운 익스체인지 객체 생성
exchange = rabbitpy.Exchange(channel, 'chapter2-example')
exchange.declare()

# 채널을 전달해 새로운 Queue 객체 생성하기
queue = rabbitpy.Queue(channel, 'example')

# RabbitMQ 서버에 큐 선언하기
print(queue.declare())

print(queue.bind(exchange, 'example-routing-key'))

for message_number in range(0, 10):
    Message = rabbitpy.Message(
        channel,
        f'Test Message {message_number} #%i' % message_number,
        {'content_type' : 'text/plain'},
        opinionated=True
    )
    Message.publish(exchange, 'example-routing-key')
