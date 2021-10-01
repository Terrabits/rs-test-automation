@echo off
SET "ROOT_DIR=%~dp0.."


setlocal
cd /d "%ROOT_DIR%"


REM build python (api)
pyinstaller run.spec --noconfirm --distpath="app"
