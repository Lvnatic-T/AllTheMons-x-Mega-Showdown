@echo off
echo Building projects before publishing...
python tools\build.py
echo.
echo Publishing to Modrinth...
python tools\publish.py
pause
