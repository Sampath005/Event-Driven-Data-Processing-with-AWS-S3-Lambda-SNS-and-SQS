import json
import boto3
import pandas
import io
import os

def lambda_handler(event, context):
    print('event', event)
    # Extract information from the S3 event
    s3_event = json.loads(event['Records'][0]['body'])['Message']
    print('s3_client', s3_event)

    # Parse the S3 event JSON string
    s3_event = json.loads(s3_event)
    key = s3_event['detail']['object']['key']
    source_bucket = s3_event['detail']['bucket']['name']

    s3_client = boto3.client('s3', region_name=os.environ.get('REGION'))
    # store the region in env

    try:
        get_file = s3_client.get_object(Bucket=source_bucket, Key=key)

        # Read the file contents
        data = get_file['Body'].read()

        # Convert the data to a Pandas DataFrame
        df = pandas.read_csv(io.BytesIO(data))

        # Convert the DataFrame to a JSON string
        df_json_string = df.to_json(orient='records')

        # Extract the filename from the input key
        input_filename = key.split("/")[-1]

        # Define the output filename
        output_filename = f'converted_{input_filename}.json'

        # Upload the JSON string to S3
        s3_client.put_object(Bucket='files-dp-target-bucket', Key=output_filename, Body=df_json_string.encode('utf-8'))

        print(f"File converted from CSV to JSON and uploaded to S3 as {output_filename}")

    except Exception as e:
        print(f"An error occurred during uploading: {e}")

