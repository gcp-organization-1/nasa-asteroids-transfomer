from google.cloud import storage
from config.settings import settings
import json

class GCSClient:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(settings.ASTEROIDS_BUCKET)

    def upload_transformed_data_to_gcs(self, df, destination):
        blob = self.bucket.blob(destination)

        csv_data = df.to_csv(index=False)

        blob.upload_from_string(csv_data, content_type="text/csv")

        print(f"Uploaded")

    def download_blob(self, source_blob_name):
        blob = self.bucket.blob(source_blob_name)
        return json.loads(blob.download_as_text())
