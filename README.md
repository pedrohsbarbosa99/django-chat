# Example Django Chat WebSocket Application

```
git clone https://github.com/pedrohsbarbosa99/django-chat
cd django-chat/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```
