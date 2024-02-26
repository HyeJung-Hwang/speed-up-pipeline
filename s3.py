import os

import boto3

AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


def upload_file_to_s3(csv_file_path: str, bucket: str, key: str):
    """
    Load file to AWS S3 bucket. 
    :param file_path: path to csv file in your local file system
    :param bucket: name of S3 bucket
    :param key: file name
    """

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME
    )

    with open(csv_file_path, "rb") as file:
        s3_client.upload_fileobj(file, bucket, key)

    print("CSV file uploaded to S3 successfully!")

if __name__ == "__main__":

    csv_file_path = "./amazonReview.csv"
    bucket = "amazon-review-bucket"
    key = "amazonReview"

    upload_file_to_s3(csv_file_path, bucket, key)
