import json
import logging
import time
import boto3
import botocore
from botocore.exceptions import ClientError
from loguru import logger
from utils import search_download_youtube_video


def process_msg(msg):
    v_name = search_download_youtube_video(msg)
    v_name = ''.join(v_name)
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(v_name, 'dady-kosta-s3', v_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True




    # TODO upload the downloaded video to your S3 bucket


def main():
    while True:
        try:
            messages = queue.receive_messages(
                MessageAttributeNames=['All'],
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )
            for msg in messages:
                logger.info(f'processing message {msg}')
                process_msg(msg.body)

                # delete message from the queue after is was handled
                response = queue.delete_messages(Entries=[{
                    'Id': msg.message_id,
                    'ReceiptHandle': msg.receipt_handle
                }])
                if 'Successful' in response:
                    logger.info(f'msg {msg} has been handled successfully')

        except botocore.exceptions.ClientError as err:
            logger.exception(f"Couldn't receive messages {err}")
            time.sleep(10)


if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)

    sqs = boto3.resource('sqs', region_name=config.get('aws_region'))
    queue = sqs.get_queue_by_name(QueueName=config.get('bot_to_worker_queue_name'))

    main()
