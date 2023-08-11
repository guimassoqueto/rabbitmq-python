a:
	poetry run python main.py

# install all dependencies
s: 
	poetry shell

i: 
	poetry install

u:
	poetry update

# install pre-commit, update its dependencies and install hook for commit messages
pc:
	pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg

# init rabbitmq container
rmq:
	docker compose up rabbitmq -d

or:
	open https://github.com/guimassoqueto/rabbitmq-python

env:
	cp .env.sample .env