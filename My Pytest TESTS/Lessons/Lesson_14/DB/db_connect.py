from sshtunnel import SSHTunnelForwarder
from psycopg import connect
# from psycopg.rows import dict_row  # Импортируем dict_row для работы с курсором в виде словаря
import config

# Функция для установки подключения к PostgreSQL через SSH-туннель
def get_db_connection():
    try:
        # Настройка SSH-туннеля
        tunnel = SSHTunnelForwarder(
            (config.SSH_HOST, config.SSH_PORT),
            ssh_username=config.SSH_USERNAME,
            ssh_password=config.SSH_PASSWORD,
            remote_bind_address=(config.DB_HOST, config.DB_PORT),
            local_bind_address=("0.0.0.0", config.LOCAL_PORT),
        )

        # Запуск SSH-туннеля
        tunnel.start()
        print("SSH-туннель успешно создан!")

        # Параметры для подключения к PostgreSQL через туннель
        conn_params = {
            "host": "localhost",
            "port": config.LOCAL_PORT,
            "dbname": config.DB_NAME,
            "user": config.DB_USER,
            "password": config.DB_PASSWORD,
        }

        # Установка подключения к PostgreSQL
        conn = connect(**conn_params)
        print("Подключение к PostgreSQL успешно установлено!")
        return conn, tunnel

    except Exception as e:
        print(f"Ошибка при подключении к PostgreSQL: {e}")
        if 'tunnel' in locals():
            tunnel.stop()
        raise e


# Функция для выполнения SQL-запросов
def execute_query(query):
    conn, tunnel = get_db_connection()
    try:
        with conn.cursor() as cursor:
            # Выполнение переданного SQL-запроса
            cursor.execute(query)

            # Получение всех результатов
            data = cursor.fetchall()
            return data

    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

    finally:
        # Закрытие соединений
        if conn:
            conn.close()
        if tunnel:
            tunnel.stop()
        print("Соединения закрыты.")
