## Развертывание и запуск
    git clone 
    cd e.kom.test
    
    # Устанавливаем виртуальное окружение
    # и все необходимые для работы пакеты
    pytnon3 -m venv venv
    source venv/bin/activate
    pip install -r reuirements.txt
    
    # Запускаем tornado сервер
    python3 runserver.py
    
    # ОПЦИОНАЛЬНО. Если по какой-то причине, файл с тестовой базой (db.json), 
    # содержащей шаблоны форм будет поврежден, то инициализируем бд тестовыми данными.
    python3 db_init.py
    
    # ОПЦИОНАЛЬНО. Скрипт совершающий несколько тестовых POST запроса
    python3 test_queries.py
    
    # ОПЦИОНАЛЬНО. Запуск тестов
    python3 -m unittest