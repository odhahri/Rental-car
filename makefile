.PHONY: makemigraterun
# Default target
default: makemigraterun
# prepare-all:
# 	conda create -n rental-car python==3.11 -y
# 	conda activate rental-car
# 	conda install pip==24.2 -y
# 	pip install -r requirements.txt
# 	docker compose up -d
# 	python manage.py makemigrations
# 	python manage.py migrate
# 	python manage.py runserver

clean-migrations:
	@echo "Cleaning pycache files..."
	@powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	@echo "Cleaning migration files..."
	@powershell -Command "Get-ChildItem -Path . -Recurse -Directory -Filter migrations | ForEach-Object { Get-ChildItem -Path $$_.FullName -File | Where-Object { $$_.Name -ne '__init__.py' -and ($$_.Extension -eq '.py' -or $$_.Extension -eq '.pyc') } | Remove-Item -Force }"
	@echo "All migration files have been cleaned except __init__.py"


makemigraterun:
	CALL conda.bat activate rental-car && python manage.py makemigrations && python manage.py migrate && python manage.py runserver