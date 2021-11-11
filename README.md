# Run project

### Set environment variables
`cp .env.example .env`

### Install dependencies
```bash
pip install poetry
poetry install
```

### Create database and update/create tables
`python src/manage.py migrate`
