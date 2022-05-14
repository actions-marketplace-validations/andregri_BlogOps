test-composite-action:
	./bin/act -v -j run_composite_action --secret-file .secret --env-file .env

test-container-action:
	./bin/act -v -j run_container_action --secret-file .secret --env-file .env

test-python-workflow:
	./bin/act -v -j build --secret-file .secret --env-file .env

test-all:
	./bin/act -v --secret-file .secret --env-file .env