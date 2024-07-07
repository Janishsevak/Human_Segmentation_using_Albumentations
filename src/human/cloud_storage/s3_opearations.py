import os
class S3sync:

    def sync_folder_to_s3(self,folder,aws_bucket_uri):
        commond = f"aws s3 sync {folder} {aws_bucket_uri}"
        os.system(commond)

    def sync_folder_to_s3(self,folder,aws_bucket_uri):
        commond = f"aws s3 sync {aws_bucket_uri} {folder}"
        os.system(commond)