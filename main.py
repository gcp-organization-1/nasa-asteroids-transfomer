from transformer.asteroids_transformer import AsteroidsTransformer

def main(request):
    try:
        request_json = request.get_json(silent=True)
        if request_json is None:
            return {"error": "Request body must be JSON"}, 400

        transformer = AsteroidsTransformer()
        df = transformer.transform_asteroids_data(request_json)
        to_str = df.to_string()
        return to_str

    except Exception as e:
        return {"error": str(e)}, 500