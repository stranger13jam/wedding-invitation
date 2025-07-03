secrets:
	python3 init/app/generate_secrets.py

admins:
	python3 init/app/create_admins.py

contents:
	python3 init/app/create_contents.py

up:
	docker compose up -d

stop:
	docker compose stop

down:
	docker compose down -v