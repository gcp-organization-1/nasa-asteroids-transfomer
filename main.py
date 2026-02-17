from transformer.asteroids_transformer import AsteroidsTransformer
from gcp.gcs import GCSClient

def main(request):
    request_json = request.get_json(silent=True)
    file_path = request_json.get("file_path")

    if not file_path:
        return {"error": "file_path is required"}, 400

    try:
        gcs = GCSClient()
        raw_data = gcs.download_blob(file_path)

        transformer = AsteroidsTransformer()
        df = transformer.transform_asteroids_data(raw_data)

        output_path = "processed/data.csv"

        gcs.upload_transformed_data_to_gcs(df, output_path)

        return {"message": "Transform complete", "file_path": output_path}

    except Exception as e:
        return {"error": str(e)}, 500
