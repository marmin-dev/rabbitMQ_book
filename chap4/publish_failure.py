import datetime
import rabbitpy

# url = 'amqp://guest:guest@localhost:5672/%2F'

# 기본 url 로 접속 : 상단이 기본 url

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        body = 'server.cpu.utilization 25.5 1350884514' # => 본문
        message = rabbitpy.Message( # => 전달할 메시지 본문
            channel,
            body,
            {
                'content_type':'text/plain',
                'timestamp': datetime.datetime.now(),
                'message_type':'graphite metric'
            }
        )
        message.publish(
            'chapter2-example',
            'server-metrics',
            mandatory=True # => mandatory 플래그를 설정하고 메시지를 발행한다.
        )
