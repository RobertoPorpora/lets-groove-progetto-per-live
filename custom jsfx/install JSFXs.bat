@echo off
setlocal

REM Get REAPER resource path (default location)
set "REAPER_PATH=%APPDATA%\REAPER"
set "FX_PATH=%REAPER_PATH%\Effects\robertoporpora"

echo Installing JSFX to: %FX_PATH%
echo.

REM Create Effects folder if it doesn't exist
if not exist "%FX_PATH%" (
mkdir "%FX_PATH%"
)

REM Copy all JSFX files
copy /Y "*.jsfx" "%FX_PATH%"

echo.
echo Done!
pause
