@echo off
:: Автоматически находит Python в стандартных путях
where python > %temp%\python_path.txt
set /p PYTHON_PATH= < %temp%\python_path.txt
del %temp%\python_path.txt

"%PYTHON_PATH%" "C:\skypro_final_task_gulnara_106.2\02_lesson\lesson_2_task_5.py"
pause