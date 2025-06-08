@echo off
REM Check if virtual environment folder "venv" exists, if not create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

echo Installing required Python packages...
pip install -r requirements.txt

echo Starting the bot...
python main.py

pause
