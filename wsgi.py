from app.main import app
import os

PORT = int(os.getenv("PORT", 10000))  # Render передаёт порт через переменную окружения


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)