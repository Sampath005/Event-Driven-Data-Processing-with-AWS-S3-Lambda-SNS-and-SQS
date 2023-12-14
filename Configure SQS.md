**SQS - Policy**

`{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "<YourQueue-Arn>",
      "Condition": {
        "ArnEquals": {
          "<yourSnsTopic-Arn>"
        }
      }
    }
  ]
}`