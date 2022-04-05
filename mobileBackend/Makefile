COMMIT_FILE=../COMMIT_MSG.md
DJANGO=python manage.py

commit:
	git commit --file=${COMMIT_FILE}

venv:
	source venv/bin/activate

migrate:
	${DJANGO} makemigrations
	${DJANGO} migrate