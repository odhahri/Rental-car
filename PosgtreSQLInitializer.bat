@REM This file is a batch script that automates the installation of PostgreSQL 
@REM and pgAdmin on Windows. It downloads the PostgreSQL and pgAdmin installers, 
@REM installs PostgreSQL silently, creates a new database, and installs pgAdmin silently. 
@REM The script is commented out to prevent accidental execution. 
@REM You can uncomment the relevant sections to run the script.

@REM Do not use this script, its under developement...






@REM @echo off

@REM :: Define variables
@REM set "PG_INSTALLER_URL=https://get.enterprisedb.com/postgresql/postgresql-15.3-1-windows-x64.exe"
@REM set "INSTALL_DIR=C:\Program Files\PostgreSQL\15"
@REM set "DATA_DIR=C:\Program Files\PostgreSQL\15\data"
@REM set "PG_PORT=5432"
@REM set "PG_ADMIN_PASSWORD=changeme"
@REM set "DB_NAME=app-rental-car"
@REM set "PG_ADMIN_URL=https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v6.23/windows/pgadmin4-6.23-x64.exe"

@REM :: Download PostgreSQL installer
@REM echo Downloading PostgreSQL installer...
@REM powershell -Command "Invoke-WebRequest -Uri %PG_INSTALLER_URL% -OutFile postgresql_installer.exe"

@REM :: Install PostgreSQL silently
@REM echo Installing PostgreSQL...
@REM postgresql_installer.exe --mode unattended ^
@REM                           --unattendedmodeui minimal ^
@REM                           --superpassword %PG_ADMIN_PASSWORD% ^
@REM                           --prefix "%INSTALL_DIR%" ^
@REM                           --datadir "%DATA_DIR%" ^
@REM                           --serverport %PG_PORT%

@REM if %errorlevel% neq 0 (
@REM     echo PostgreSQL installation failed.
@REM     exit /b %errorlevel%
@REM )

@REM :: Add PostgreSQL bin directory to PATH
@REM setx PATH "%INSTALL_DIR%\bin;%PATH%"

@REM :: Wait for the service to start
@REM timeout /t 10

@REM :: Create a new database
@REM echo Creating database %DB_NAME%...
@REM psql -U postgres -h localhost -p %PG_PORT% -d postgres -c "CREATE DATABASE \"%DB_NAME%\";"

@REM if %errorlevel% neq 0 (
@REM     echo Database creation failed.
@REM     exit /b %errorlevel%
@REM )

@REM :: Download pgAdmin installer
@REM echo Downloading pgAdmin installer...
@REM powershell -Command "Invoke-WebRequest -Uri %PG_ADMIN_URL% -OutFile pgadmin_installer.exe"

@REM :: Install pgAdmin silently
@REM echo Installing pgAdmin...
@REM pgadmin_installer.exe /SILENT

@REM if %errorlevel% neq 0 (
@REM     echo pgAdmin installation failed.
@REM     exit /b %errorlevel%
@REM )

@REM echo PostgreSQL and pgAdmin setup completed successfully.
@REM exit /b 0
