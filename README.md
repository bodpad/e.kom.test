## Развертывание и запуск
    git clone https://github.com/bodpad/e.kom.test.git
    cd e.kom.test
    
    # Устанавливаем виртуальное окружение
    # и все необходимые для работы пакеты
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    # Запускаем tornado сервер
    python3 runserver.py
    
    # ОПЦИОНАЛЬНО. Если по какой-то причине, файл с тестовой базой (db.json), 
    # содержащей шаблоны форм будет поврежден, то инициализируем бд тестовыми данными.
    python3 db_init.py
    
    # ОПЦИОНАЛЬНО. Скрипт совершающий несколько тестовых POST запросов
    python3 test_post_requests.py
    
    # ОПЦИОНАЛЬНО. Запуск тестов
    python3 -m unittest
