# buildozer.spec

[app]

# Nome do aplicativo
title = Buffet Calculator PRO

# Nome do pacote (nome do aplicativo)
package.name = buffet_calculator_pro

# Nome do pacote de domínio (reverso do seu domínio)
package.domain = com.carlos

# Fonte que será incluída no pacote (ex.: arquivos .py, .png, .kv)
source.include_exts = py,png,jpg,kv,ttf

# Versão do aplicativo
version = 1.0

# Código de versão (pode ser incrementado)
version_code = 1

# Defina o nome do aplicativo em dispositivos Android
# Esse é o nome do arquivo APK gerado
package.filename = buffet_calculator_pro.apk

# O arquivo principal do seu código Python
# Indique o arquivo Python que será executado
main.py = buffet_calc_pro.py

# Caminho para a biblioteca Python instalada no projeto
# Se você estiver usando bibliotecas externas, defina o caminho para elas aqui
# Exemplo: lib.include = /home/user/mylibs

[buildozer]

# Escolha a plataforma para onde você vai empacotar (android, ios, etc.)
# Isso depende de qual plataforma você quer empacotar seu aplicativo.
# Por exemplo, para Android, use `android`:
target = android

# Defina a versão do SDK Android
android.sdk = 33  # SDK version para Android 33, pode ser 30, 31, 32, ou a versão que você deseja

# Caminho para a JDK
# Não será necessário se a JDK já estiver configurada em seu ambiente.
android.java_home = /path/to/your/java  # Caso tenha o Java em um caminho específico, defina aqui

# Defina a versão mínima do Android
android.minapi = 21  # Ajuste conforme necessário (Android 5.0 em diante é recomendado)

# O arquivo de saída do APK será gerado aqui
android.build_dir = ./build

# Defina as permissões necessárias para o aplicativo no Android
# Se você precisar de permissões específicas, como acessar a câmera ou localização, adicione-as aqui.
# Exemplo de permissões:
# android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_FINE_LOCATION
android.permissions = INTERNET

[dependencies]

# Defina as dependências que seu aplicativo pode precisar.
# Exemplo:
# android.ndk = 21.3.6528147
# python3, kivy, etc.
# Instalar dependências para o projeto no Android.
# Dependências adicionais do Buildozer podem ser definidas aqui:
# Exemplo:
# install_requires = kivy
