#!/usr/bin/env python
import preprocessing

mysql = {
    "host": "localhost",
    "user": "root",
    "passwd": "my secret password",
    "db": "write-math",
}
preprocessing_queue = [
    preprocessing.scale_and_center,
    preprocessing.dot_reduction,
    preprocessing.connect_lines,
]
use_anonymous = True

aws_access_key_id = AKIAYVP4CIPPMCL6GVSN
aws_secret_access_key = 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
output = json
region = us-east-2


