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

# Diretório onde os arquivos de origem estão localizados (ajuste conforme necessário)
source.dir = ./windows_build  # Ajuste se necessário para o diretório onde seu código está localizado

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
