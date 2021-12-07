""" To be imported to extraction scripts to push data to S3. """

import os
import shutil
import tempfile
import boto3
import json
import logging
import csv

def load_object_to_s3(data, local_file_name, output_filename, s3_bucket, 
                    aws_server_public_key=None, aws_server_secret_key=None):
    """ This saves a json, list of json, or CSV object
    locally to a temporary file and then uploads it to the S3 bucket"""

    temp_dir = tempfile.TemporaryDirectory()
    input_filename = os.path.join(temp_dir.name, local_file_name)
    ## allow for it to be csv
    with open(input_filename, 'w') as f:
        if isinstance(data, dict) or isinstance(data, list):
            json.dump(data, f)
        else:
            f.writelines(data)

    if aws_server_public_key is not None:
        session = create_session(aws_server_public_key, aws_server_secret_key)
        s3_storage = session.resource("s3")
    else:
        s3_storage = boto3.resource("s3")

    s3_storage.meta.client.upload_file(input_filename, s3_bucket, output_filename)
    # remove temp directory if done
    if os._exists(temp_dir.name):
        shutil.rmtree(temp_dir.name)

def create_session(aws_server_public_key, aws_server_secret_key):
    """ If AWS credentials are passed, create a session with them """

    return boto3.Session(
        aws_access_key_id=aws_server_public_key,
        aws_secret_access_key=aws_server_secret_key,
    )

def find_existing_data(prefix, s3_bucket, aws_server_public_key=None, aws_server_secret_key=None):
    """ Given a key within an S3 buckets, reads through all files and returns content"""
    
    if aws_server_public_key is not None:
        session = create_session(aws_server_public_key, aws_server_secret_key)
        s3_storage = session.resource("s3")
    else:
        s3_storage = boto3.resource("s3")

    my_bucket = s3_storage.Bucket(s3_bucket)
    json_row_objects = []

    for object_summary in my_bucket.objects.filter(Prefix=prefix):
        content_object = s3_storage.Object(s3_bucket, object_summary.key)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        if content_object.key.endswith('.json'):
            for line in file_content.splitlines():
                for json_line in json.loads(line):
                    json_row_objects.append(json_line)
        elif content_object.key.endswith('.csv'):
            for row in csv.DictReader(file_content.splitlines(True)):
                json_row_objects.append({k.lower().strip(): v.strip() for k, v in row.items()})
        else:
            logging.info("Found file of invalid type, not processing for most recent date")
    return json_row_objects