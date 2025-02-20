import os
import dotenv

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Параметры SSH
SSH_HOST = os.getenv('SSH_HOST')
SSH_PORT = int(os.getenv('SSH_PORT'))
SSH_USERNAME = os.getenv('SSH_USERNAME')
SSH_PASSWORD = os.getenv('SSH_PASSWORD')

# Параметры PostgreSQL
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Локальный порт для SSH-туннеля
LOCAL_PORT = int(os.getenv('LOCAL_PORT'))
