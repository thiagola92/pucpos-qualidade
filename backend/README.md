# Backend
This project uses [uv](https://docs.astral.sh/uv/guides/install-python/) as
Python package manager and
[FastAPI](https://github.com/thiagola92/pucpos-arquitetura-b) as framework.

# Usage
Make sure to install uv: https://docs.astral.sh/uv/getting-started/installation/

Install dependencies:

```
uv sync
```

Then start the project in development mode:

```
uv run fastapi dev app.py
```

This will watch the project directory and restart as necessary.

Access through http://127.0.0.1:8000

# References

- https://fastapi.tiangolo.com/
- https://fastapi.tiangolo.com/advanced/additional-status-codes/