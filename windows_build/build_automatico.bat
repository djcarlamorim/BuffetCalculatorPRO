@echo off
:: CONFIGURADOR DEFINITIVO PARA WINDOWS
set PYTHON=C:\Users\CARLOS\AppData\Local\Programs\Python\Python39\python.exe
set PROJECT=C:\Users\CARLOS\BuffetCalculatorPRO\windows_build

cd /d "%PROJECT%"

echo [1/4] INSTALANDO BUILDÖZER...
"%PYTHON%" -m pip install buildozer==1.4.0 cython==0.29.33

echo [2/4] CRIANDO CONFIGURAÇÃO...
(
echo [app]
echo title = BuffetCalculatorPRO
echo package.name = buffetcalculatorpro
echo package.domain = com.carlos
echo version = 1.0.0
echo source.dir = .
echo requirements = python3,kivy==2.1.0
echo android.permissions = INTERNET
echo android.api = 33
) > buildozer.spec

echo [3/4] INICIANDO BUILD...
set BUILDÖZER_SKIP_SDK_CHECK=1
"%PYTHON%" -m buildozer -v android debug > build.log 2>&1

echo [4/4] RESULTADO:
if exist "bin\*.apk" (
    echo ✅ BUILD SUCESSO! APK em: %PROJECT%\bin\
    dir bin
) else (
    echo ❌ FALHA - Verifique build.log
    type build.log | findstr /i "error fail"
)
pause