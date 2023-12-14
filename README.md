# Event-Driven Data Processing with AWS S3, Event Bridge, Lambda, SNS, and SQS

This project demonstrates an event-driven data processing pipeline using AWS services to transform files when uploaded to an S3 bucket. The pipeline includes AWS S3, Lambda, SNS, and SQS.

## Project Overview

The objective of this project is to automatically transform files when they are uploaded to a designated S3 bucket. The transformation is handled by an AWS Lambda function. The transformed files are then stored in another S3 bucket.

## Architecture

![Architeture](https://github.com/Sampath005/Event-Driven-Data-Processing-with-AWS-S3-Lambda-SNS-and-SQS/assets/97429122/ec2eef5b-baf0-445d-bb48-fc9e17521735)

## Setup

1. **Create AWS Resources:**
   - Create source S3 bucket with bucket policy.
   - create target s3 bucket 
   - Create Event Bridge rule
   - create an SNS topic for notifications.
   - create an SQS queue for asynchronous processing with access policy.
   - Create a Lambda function with the appropriate IAM role.
   
2. **Configure - [Source s3](https://github.com/Sampath005/Event-Driven-Data-Processing-with-AWS-S3-Lambda-SNS-and-SQS/blob/main/Configure%20s3.md) :**
   - Create required bucket policy
   - Turn on Event bridge to trigger.
   
3. **Configure - [SQS Queue](https://github.com/Sampath005/Event-Driven-Data-Processing-with-AWS-S3-Lambda-SNS-and-SQS/blob/main/Configure%20SQS.md):**
   - create an SQS queue and configure the Lambda function to send messages to it.

4. **Configure - [Lambda Function](https://github.com/Sampath005/Event-Driven-Data-Processing-with-AWS-S3-Lambda-SNS-and-SQS/blob/main/Configure%20Lambda.md):**
   - Set up the Lambda function environment variables with the appropriate values.
   - Add the layer for the dependency
   - configure trigger as SQS
   - Make sure you have enough permission to put the object on the target bucket
   - Adjust the Lambda function code to suit your transformation logic.


## Lambda Function Code

See the provided[ lambda_function.py](https://github.com/Sampath005/Event-Driven-Data-Processing-with-AWS-S3-Lambda-SNS-and-SQS/blob/main/lambda_function.py) for a sample Lambda function code. Customize the code according to your transformation logic.

## Testing

1. **Upload a File:**
   - Upload a file to the source S3 bucket.

2. **Monitor Transformation:**
   - Monitor the Lambda function logs in the AWS CloudWatch console.
   - Check the destination S3 bucket for the transformed file.

## Notes

- Ensure that the Lambda function has the necessary IAM permissions to read from the source S3 bucket and write to the destination S3 bucket.

- Replace placeholder values in the code and configuration with your actual AWS resource details.

## License

This project is licensed under the [MIT License](LICENSE).

## Author
   - Sampath. V

