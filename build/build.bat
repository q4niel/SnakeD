@echo off
for %%i in (%~dp0..) do set "projDir=%%~fi"
py -3 -B %projDir%/build/bin/main.py