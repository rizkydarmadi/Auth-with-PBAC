## Alembic auto migrations

### Requirements

- python 3.11
- docker-compose
- ubuntu/macOS or windows (ubuntu/macOS recomended)

### create database

if you dont have installed database in your computer you can use docker compose with command `sudo docker-compose up`

### How to use

- clone this repo `git clone https://github.com/rizkydarmadi/alembic_automigrations.git`
- make virtual environtment for linux/macOS `python -m venv env`
- use the environtment `source env/bin/activate`
- installl library `pip install -r requirements.txt`
- configurate settings.py file
- configurate alembic.ini
- lets make migrations `alembic revision --autogenerate -m "create_table_user"`
- upgrade migrations `alembic upgrade head`
- ready to use 🚀🚀🚀🚀🚀🚀
