[app]
# Configurações do aplicativo
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
requirements = python3,kivy
version = 2.0  # Versão do aplicativo
# Para usar regex em vez de uma versão fixa:
# version.regex = ^(\d+\.\d+\.\d+)$

# Android
android.ndk_path = $HOME/android-sdk/ndk/25.1.8937393
android.sdk_path = $HOME/android-sdk
android.p4a_dir = $GITHUB_WORKSPACE/build/.buildozer/android/platform/python-for-android

# Configurações específicas do Android
android.permissions = INTERNET

# Definir a arquitetura
# Se estiver criando para uma arquitetura específica, adicione:
# android.arch = armeabi-v7a,arm64-v8a,x86,x86_64

# Outras configurações
# O caminho do arquivo de logo (se necessário)
# icon.filename = %(source.dir)/myapp/icon.png

# Configurações para a versão da aplicação
# version.regex = 2.0.* 
