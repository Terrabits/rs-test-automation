@echo off
SET "ROOT_DIR=%~dp0.."


setlocal
cd /d "%ROOT_DIR%"


REM clean
rmdir /S /Q app
rmdir /S /Q build\run
rmdir /S /Q dist
mkdir dist
