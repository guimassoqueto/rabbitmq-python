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

rm:
	>/home/gmassoqueto/scrap/scrap-fiber/static/thunder/tmp.txt && rm /home/gmassoqueto/scrap/scrap-fiber/static/thunder/*

or:
	make rm && open https://github.com/guimassoqueto/scrap-template-requester

env:
	cp .env.sample .env