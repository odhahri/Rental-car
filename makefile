.PHONY: makemigraterun

# prepare-all:
# 	conda create -n rental-car python==3.11 -y
# 	conda activate rental-car
# 	conda install pip==24.2 -y
# 	pip install -r requirements.txt
# 	docker compose up -d
# 	python manage.py makemigrations
# 	python manage.py migrate
# 	python manage.py runserver

makemigraterun:
	CALL conda.bat activate rental-car
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver