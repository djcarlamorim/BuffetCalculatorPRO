@echo off
:: CORREÇÃO DEFINITIVA PARA SEU NDK
:: Caminho corrigido: C:\Users\CARLOS\android-sdk\ndk\23.1.7779620\android-ndk-r23b

title AJUSTE DE CAMINHO NDK - BUFFET CALCULATOR PRO
color 0A

set NDK_ROOT=C:\Users\CARLOS\android-sdk\ndk\23.1.7779620\android-ndk-r23b
set BUILD_TOOLS=C:\Users\CARLOS\android-sdk\build-tools\33.0.0-5

echo.
echo [1/4] VERIFICANDO ESTRUTURA DO NDK...
if not exist "%NDK_ROOT%\build\cmake\android.toolchain.cmake" (
   echo ❌ ARQUIVO ESSENCIAL FALTANTE: android.toolchain.cmake
   echo Verifique se o NDK foi extraído corretamente
   pause
   exit /b
)

echo [2/4] ATUALIZANDO VARIÁVEIS DE AMBIENTE...
setx ANDROID_NDK_ROOT "%NDK_ROOT%"
setx ANDROID_NDK_HOME "%NDK_ROOT%"
setx PATH "%PATH%;%NDK_ROOT%;%BUILD_TOOLS%"

echo [3/4] ATUALIZANDO buildozer.spec...
(
echo [app]
echo android.ndk_path = %NDK_ROOT%
echo android.sdk_path = C:\Users\CARLOS\android-sdk
echo android.build_tools_version = 33.0.0-5
) > buildozer.spec

echo [4/4] TESTANDO CONFIGURAÇÃO...
call "%NDK_ROOT%\ndk-build.cmd" --version >nul
if %errorlevel% equ 0 (
   echo ✅ NDK CONFIGURADO COM SUCESSO!
   echo Caminho: %NDK_ROOT%
) else (
   echo ❌ FALHA NA VERIFICAÇÃO DO NDK
)

echo.
echo ⚠️ IMPORTANTE:
echo 1) Feche TODAS as janelas do CMD
echo 2) Reabra como Administrador
echo 3) Execute novamente o build
pause