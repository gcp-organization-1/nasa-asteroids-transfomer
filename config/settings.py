from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    ASTEROIDS_BUCKET = os.getenv("ASTEROIDS_BUCKET")


settings = Settings()