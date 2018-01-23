import boto3
client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
BUCKET_NAME = 'ENTER-BUCKET-NAME-HERE'
response_iterator = paginator.paginate(
		Bucket=BUCKET_NAME)
for page in response_iterator:
	for item in page['Contents']:
		response = client.put_object_acl(ACL='private', Bucket=BUCKET_NAME,Key=item['Key'])
		print "Setting ACL for " + item['Key']
