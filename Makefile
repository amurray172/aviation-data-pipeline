# Makefile

# Run the Python app in Docker
run:
	docker-compose run --rm app python -m main

# Open a shell inside the app container
shell:
	docker-compose run --rm app /bin/bash

# Stop and remove containers
down:
	docker-compose down

# Rebuild the app container
build:
	docker-compose build app
