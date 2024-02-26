import os

import boto3

AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


def upload_file_to_s3(file_path: str, bucket: str, key: str):
    """
    Load file to AWS S3 bucket. 
    :param file_path: path to file in your local file system
    :param bucket: name of S3 bucket
    :param key: file name
    """

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME
    )

    with open(file_path, "rb") as file:
        s3_client.upload_fileobj(file, bucket, key)

    print("File uploaded to S3 successfully!")


def download_file_from_s3(bucket: str, key: str, local_file_path: str):
    """
    Download file from AWS S3 bucket.
    :param bucket: name of S3 bucket
    :param key: file name in S3 bucket
    :param local_file_path: local path to save the downloaded file
    """

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME
    )

    try:
        with open(local_file_path, "wb") as file:
            s3_client.download_fileobj(bucket, key, file)
        print(f"File '{key}' downloaded from S3 to '{local_file_path}' successfully!")
    except Exception as e:
        print(f"Error downloading file from S3: {e}")

if __name__ == "__main__":

    parquet_file_path = "./amazonReivew.parquet"
    bucket = "amazon-review-bucket"
    key = "amazonReview.parquet"

    upload_file_to_s3(parquet_file_path, bucket, key)
