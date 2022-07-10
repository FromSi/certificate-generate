.PHONY: restart
restart:
	docker-compose stop
	docker-compose up -d
	rm temp/*.*