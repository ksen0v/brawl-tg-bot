@echo off
REM Activate the existing virtual environment
call venv\Scripts\activate.bat

echo Starting the bot...
python main.py

pause
