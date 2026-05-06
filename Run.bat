@echo off
title House Price Predictor - GUI Mode
echo --------------------------------------------------
echo Launching Graphical House Price Predictor...
echo --------------------------------------------------
echo.

:: 1. Navigate to the current folder
cd /d "%~dp0"

:: 2. Check for virtual environment
if not exist venv\Scripts\activate (
    echo [ERROR] Virtual environment 'venv' not found!
    echo Please make sure you have installed the environment in this folder.
    pause
    exit
)

:: 3. Activate the environment
echo [1/2] Activating Virtual Environment...
call venv\Scripts\activate

:: 4. Install Tkinter (Standard on Windows, but checking dependencies)
echo [2/2] Checking for pandas and scikit-learn...
pip install pandas scikit-learn --quiet

:: 5. Run the Tkinter script
echo.
echo Launching GUI window...
python houseusingtkinter.py

:: 6. Handle errors or closing
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The application crashed or could not find houseusingtkinter.py
)

pause