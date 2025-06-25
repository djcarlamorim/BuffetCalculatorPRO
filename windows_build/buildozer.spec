[app]
# Configurações do aplicativo
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
requirements = python3,kivy
android.ndk_path = $HOME/android-sdk/ndk/25.1.8937393
android.sdk_path = $HOME/android-sdk
android.p4a_dir = $GITHUB_WORKSPACE/build/.buildozer/android/platform/python-for-android

# Versão do aplicativo
version = 1.0.0
# Se desejar usar versão regex, pode descomentar a linha abaixo
# version.regex = ^(\d+\.\d+\.\d+)$
