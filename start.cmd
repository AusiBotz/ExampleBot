@echo off
cls
:startLoop
title Discord Bot - client.py
python3 client.py
timeout -T 1 /NoBreak>NUL
goto startLoop
