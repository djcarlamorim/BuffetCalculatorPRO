# SCRIPT DEFINITIVO PARA BUFFET CALCULATOR PRO
Write-Host "=== CONFIGURANDO AMBIENTE ===" -ForegroundColor Green

# 1. Verificar WSL
if (!(wsl -l | Select-String "Ubuntu")) {
    Write-Host "Instalando WSL2 e Ubuntu..." -ForegroundColor Yellow
    wsl --install -d Ubuntu
    Write-Host "Reinicie o computador e execute novamente" -ForegroundColor Red
    exit
}

# 2. Configurar ambiente no WSL
Write-Host "Configurando ambiente Linux..." -ForegroundColor Yellow
wsl -e bash -c "
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git zip unzip openjdk-17-jdk
python3 -m pip install --user buildozer cython==0.29.33
"

# 3. Copiar projeto para WSL
Write-Host "Preparando projeto..." -ForegroundColor Yellow
$projectPath = "C:\Users\CARLOS\BuffetCalculatorPRO\windows_build"
wsl -e bash -c "
mkdir -p ~/projects
cp -r '/mnt/c/Users/CARLOS/BuffetCalculatorPRO/windows_build' ~/projects/
cd ~/projects/windows_build
"

# 4. Executar build
Write-Host "Iniciando build (pode demorar 30-60 minutos)..." -ForegroundColor Yellow
wsl -e bash -c "
cd ~/projects/windows_build
buildozer init
echo '[app]
title = BuffetCalculatorPRO
package.name = buffetcalculatorpro
package.domain = com.carlos
version = 1.0.0
source.dir = .
requirements = python3,kivy==2.1.0
android.permissions = INTERNET
android.api = 33' > buildozer.spec
buildozer -v android debug
"

# 5. Verificar resultado
Write-Host "Verificando resultado..." -ForegroundColor Green
wsl -e bash -c "
if [ -f ~/projects/windows_build/bin/*.apk ]; then
    echo '✅✅✅ APK gerado com sucesso! ✅✅✅'
    ls -lh ~/projects/windows_build/bin/
else
    echo '❌❌❌ Falha no build ❌❌❌'
    echo 'Verifique o log: ~/projects/windows_build/.buildozer/android/platform/build-armeabi-v7a/docker.log'
fi
"

Write-Host "Processo concluído! Verifique acima o resultado." -ForegroundColor Green
pause