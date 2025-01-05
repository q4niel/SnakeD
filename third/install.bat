@echo off
for %%i in (%~dp0..) do set "projDir=%%~fi"
py -3 -B %projDir%/third/bin/main.py