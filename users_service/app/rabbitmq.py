import aio_pika
from settings import settings
import asyncio

async def start_consumer(loop):
    try:
        conn = await aio_pika.connect_robust(
            settings.amqp_url, 
            loop=loop,
            timeout=5  # Таймаут подключения
        )
        ch = await conn.channel()
        q = await ch.declare_queue("medicine_added", durable=True)
        
        async def consume(msg: aio_pika.IncomingMessage):
            async with msg.process():
                payload = msg.body.decode()
                print(f"[USERS] Получено: {payload}")
                # Можно логировать в файл вместо БД
                
        await q.consume(consume)
        print("RabbitMQ consumer запущен")
        return conn
    except Exception as e:
        print(f"Не удалось подключиться к RabbitMQ: {e}")
        return None