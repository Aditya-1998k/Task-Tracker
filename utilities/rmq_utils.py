import os
import pika
import json

from utilities.logging_config import get_logger

logger = get_logger(__name__)


def create_connection():
    credentials = pika.PlainCredentials(
        os.getenv("RABBITMQ_USER", "guest"),
        os.getenv("RABBITMQ_PASS", "guest")
    )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
            port=int(os.getenv("RABBITMQ_PORT", 5672)),
            credentials=credentials
        )
    )
    return connection


def publish_to_rabbimq(queue, payload):
    """Safely publish a message to RabbitMQ."""
    try:
        connection = create_connection()
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)

        if not isinstance(payload, (str, bytes)):
            payload = json.dumps(payload)

        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=payload,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        logger.info(f"Message published to queue: {queue}")
    except Exception as e:
        logger.exception(f"RabbitMQ publish failed: {e}")
    finally:
        try:
            connection.close()
        except Exception:
            pass

