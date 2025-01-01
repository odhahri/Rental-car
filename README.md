# Project Setup and Running Instructions

## Prerequisites

Make sure you have the following installed on your system:
- Python 3.11 or later
- miniconda
- docker desktop

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/odhahri/Rental-car.git
    cd app_localtion_car_ssr_project_
    if using vscode, use tap code . to open IDE with the project
    ```

2. **Create a virtual environment (using miniconda or anaconda):**
    ```sh
    conda env create -n rental-car python=3.11
    ```

3. **Activate the virtual environment:**
        - Conda command
      ```
      conda activate rental-car
      ```

4. **Install the required dependencies:**
    ```
    conda install pip=24.2
    pip install -r requirements.txt
    ```

## Running the Project

1. **Create and Run the database container:**
    ```.env
    precize your database configuration in the .env file 
    exemple :   DATABASE_NAME=app_rental_car
                DATABASE_USER=postgres
                DATABASE_PASSWORD=changeme
                DATABASE_HOST=localhost
                DATABASE_PORT=54320
    ```
    ```sh
    docker compose up -d
    ```
    ```
    Access docker desktop and open pgAdmin from the running container, then create your database.
    ```

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 
    ```

2. ** Access the application via the web:**
    Open your web browser and go to `http://localhost:8000`

## Additional Commands

- **Deactivate the virtual environment:**
  ```sh
  conda deactivate
  ```



