This script was initially written to address incorrect ACL's being set on a respective S3 bucket. For private content on S3 we generally want the objects to be accessible through the use of IAM roles that allow S3 GET/PUT actions.
This means that the acl of 'private' is our best bet as it's the default permission scheme out of the box when initially creating an S3 bucket and uploading objects (full-access for bucket owner). If you're one of those that accidently wrote code to upload objects into S3 with a public acl (public-read) than you'll want to run this.

The instructions are simple, define the bucket-name within the first two method calls and the code will handle the rest!
