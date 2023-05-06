# Running the app locally

1. Run `poetry install`
2. Run ` poetry run python manage.py migrate` to apply migrations
3. Run `poetry run ./manage.py runserver`

# What to do after you made updates to Models?
1. Run `poetry run python manage.py makemigrations` to create a migration reflecting the changes
2. Run `poetry run python manage.py migrate` to apply new migrations