## Социальная сеть ВШЭ

<div>&nbsp;</div>

Функционал:
- Чат
- Онлайн/Оффлайн статус
- "Is typing..." индикатор
- Запросы в друзья
- Посты
-  Комменты
- История диалогов
-  Аутентификация

Технический стек:
- Python 3.8 + FastAPI
-  PostgreSQL 13 + async SQLAlchemy (Core) + asyncpg driver
- Neo4j графовая бд
- Socket.IO для чата
- Jwt + refresh tokens rotation для аутентификации
-  Docker + docker-compose для деплоя

<br/>

## Quick start
#### Requirements
- OS: Linux, macOS, Windows 
- Install Docker (https://docs.docker.com/install/)
- (Linux only) Install docker-compose (https://docs.docker.com/compose/install/)
#### Deploy 
Клонируем репу:  
`git clone https://github.com/artgas1/nis_course_backend`  

Переходим в папку проета:  
`cd backend`  

Запускаем все сервисы:  
`docker-compose up`  

Переходим в браузере сюда:
http://localhost  
<br/>
Документация доступна здесь::
http://localhost:8000/docs and http://localhost:8000/redoc
