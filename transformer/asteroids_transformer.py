import pandas as pd

class AsteroidsTransformer:
    def __init__(self):
        self.records = []

    def transform_asteroids_data(self, data):

        for date in data["near_earth_objects"]:
            print(date)
            for obj in data["near_earth_objects"][date]:
                record = {
                    "id": obj.get("id"),
                    "name": obj.get("name"),
                    "absolute_magnitude": obj.get("absolute_magnitude_h"),
                    "estimated_diameter_min_km": obj["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                    "estimated_diameter_max_km": obj["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    "is_potentially_hazardous": obj.get("is_potentially_hazardous_asteroid"),
                    "date": obj["close_approach_data"][0].get("close_approach_date"),
                    "relative_velocity_km_per_sec": obj["close_approach_data"][0]["relative_velocity"].get(
                        "kilometers_per_second"),
                    "miss_distance_km": obj["close_approach_data"][0]["miss_distance"].get("kilometers"),
                    "orbiting_body": obj["close_approach_data"][0].get("orbiting_body"),
                }

                self.records.append(record)

        df = pd.DataFrame(self.records)
        print(df)
        return df

