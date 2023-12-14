## Source bucket

**Bucket policy**

`{
    "Version": "2012-10-17",
    "Id": "Policy1702348481163",
    "Statement": [
        {
            "Sid": "Stmt1702348478409",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "NotResource": [
                "arn:aws:s3:::<your-source-bucket>/*.csv",
                "arn:aws:s3:::<your-source-bucket>/*.excel"
            ]
        }
    ]
}`

## you can add the file formats according to your need