```bash
uvicorn app.main:app --reload
```

```bash
alembic revision --autogenerate -m "Add user model"
alembic upgrade head 
```