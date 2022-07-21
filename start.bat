@echo off

if not exist Lib  (
	echo Creating
	virtualenv . --creator venv
) 
Scripts\Activate && if not exist Lib\site-packages\pygame (
	pip install -r requirements.txt 
	py run.py 
	Scripts\deactivate
) else (
	echo Pygame already installed
	py run.py 
	Scripts\deactivate
) 

