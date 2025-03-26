import os
from dotenv import load_dotenv

load_dotenv()  # если ты используешь .env файл

# Базовые настройки
BASE_URL = os.getenv('BASE_URL', 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
ENV = os.getenv('ENV', 'dev')  # dev / stage / prod
HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
TIMEOUT = int(os.getenv('TIMEOUT', 5000))

# Пользователи
ADMIN_LOGIN = os.getenv('ADMIN_LOGIN', 'Admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

# Тестовые данные
DEFAULT_USER = {
    "name": 'Тестовый Пользователь',
    "login": 'Admin',
    "password": 'admin123'
}
