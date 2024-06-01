test:
	docker-compose exec -it web python manage.py test

create-admin-user:
	docker-compose exec -it web python manage.py createadminuser --username admin --password admin --noinput --email admin@admin.com


