.PHONY: restart
restart:
	docker compose stop
	docker compose up -d
	rm -rf temp/*.*
	
.PHONY: stop
stop:
	docker compose stop
	
.PHONY: run
run:
	docker compose up -d
	
