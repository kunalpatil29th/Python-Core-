# s3_bucket_sim.py

"""
Definition: Amazon S3 (Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
"""

class S3Bucket:
    def __init__(self, name):
        self.name = name
        self.objects = {}

    def upload_file(self, key, data):
        self.objects[key] = data
        print(f"Uploaded to {self.name}/{key}")

    def download_file(self, key):
        return self.objects.get(key, "File not found")

# Simulation
bucket = S3Bucket("my-python-assets")
bucket.upload_file("config.json", '{"theme": "dark"}')
print(bucket.download_file("config.json"))
