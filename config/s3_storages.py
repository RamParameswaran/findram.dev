from config.settings.base import env
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = env.str("S3_RESOURCES_BUCKET_NAME", default=None)
    custom_domain = env.str("AWS_S3_CUSTOM_DOMAIN", default=None)
    location = "media"


class StaticStorage(S3Boto3Storage):
    bucket_name = env.str("S3_RESOURCES_BUCKET_NAME", default=None)
    custom_domain = env.str("AWS_S3_CUSTOM_DOMAIN", default=None)
    location = "static"
