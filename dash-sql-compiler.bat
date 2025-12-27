@echo off
REM Простой батник для сборки
if "%1"=="" goto error
if "%2"=="" goto error

echo Сборка %1 в %2...
echo.

echo 1. Analyzing...
python main.py %1
if errorlevel 1 goto fail

echo 2. Semantic Analyzing...
python main_semantic.py %1
if errorlevel 1 goto fail

echo 3. Generation LLVM IR...
python code-generator.py %1 %1.ll
if errorlevel 1 goto fail

echo 4. Компиляция заглушек...
gcc -c stub.c -o stub.o
gcc -c runtime.c -o runtime.o

echo 5. Компиляция LLVM IR...
clang -c %1.ll -o %1.o -O0
if errorlevel 1 goto fail

echo 6. Линковка...
gcc %1.o runtime.o stub.o -o %2 -lm -lgcc -lmingwex -lmingw32

echo.
echo Готово! Исполняемый файл: %2
goto end

:fail
echo ОШИБКА на этапе сборки!
goto end

:error
echo Использование: %0 <input_file> <output_exe>
echo Пример: %0 example.dsql program.exe

:end
pause