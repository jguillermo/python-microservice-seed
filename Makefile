.DEFAULT_GOAL := help

## GENERAL ##
OWNER 			= utp
SERVICE_NAME 	= flash
PATH_PREFIX 	= "/v1"

## DEPLOY ##
ENV 			?= dev
export DEPLOY_REGION 	?= eu-west-1
ACCOUNT_ID		?= 929226109038


## RESULT_VARS ##
PROJECT_NAME	= $(OWNER)-$(ENV)-$(SERVICE_NAME)
export CONTAINER_NAME 	= $(PROJECT_NAME)_backend
export IMAGE_DEV		= $(PROJECT_NAME):dev
export IMAGE_TEST = getmin/test-e2e:node-1.0

## Target Commons ##

build: ## build image to dev: make build
	cp app/requirements.txt docker/dev/resources/requirements.txt
	docker build -f docker/dev/Dockerfile -t $(IMAGE_DEV) docker/dev/
	rm -f docker/dev/resources/requirements.txt

up: ## up docker containers: make up
	docker-compose up -d
	@make status

start: ## up docker containers: make up
	make up

down: ## Stops and removes the docker containers: make down
	docker-compose down

status: ## Show containers status: make status
	docker-compose ps

stop: ## Stops and removes the docker containers, use me with: make down
	docker-compose stop

restart: ## Restart all containers, use me with: make restart
	docker-compose restart
	@make status

ssh: ## Connect to container for ssh protocol
	docker exec -it $(CONTAINER_NAME) bash

log: ## Show container logs
	docker-compose logs -f backend

install-lib: ## Connect to container for ssh protocol install with pip: make install-lib
	docker exec -it $(CONTAINER_NAME) pip-3.5 install $(LIB)

tests: ## Run the unitTests
	@docker run --rm -t -v $(PWD)/app:/app:rw --entrypoint /resources/test.sh $(IMAGE_DEV)
	@sudo chown -R $(USER):$(USER) $(PWD)/app/*

tests-e2e: ## Run the end to end Tests
	docker-compose -f docker-compose.test.yml run --rm test

## Migrate ##
migrate: ## Execute migrate
	docker run --rm -t -v $(PWD)/app:/app:rw --entrypoint /resources/alembic.sh $(IMAGE_DEV) upgrade head; \

revision: ## Create a new revision
	@docker run --rm -t -v $(PWD)/app:/app:rw -v $(PWD)/alembic:/alembic:rw --entrypoint /resources/alembic.sh $(IMAGE_DEV) revision -m "$(DESC)"
	@sudo chown -R $(USER) $(PWD)/app/alembic/versions

downgrade: ## Execute migrate
	@docker run --rm -t -v $(PWD)/app:/app:rw \
			--entrypoint /resources/alembic.sh $(IMAGE_DEV) downgrade base

migrate-id: ## Execute migrate
	@docker run --rm -t -v $(PWD)/alembic:/alembic:rw --entrypoint /resources/alembic.sh $(IMAGE_DEV) upgrade $(ID)

## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
