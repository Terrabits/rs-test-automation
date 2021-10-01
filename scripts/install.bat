@echo off
SET "ROOT_DIR=%~dp0.."


setlocal
cd /d "%ROOT_DIR%"


REM install python dependencies
pip install --upgrade  pip setuptools
pip install --requires requirements.txt

REM install node dependencies
npm install --save-dev
