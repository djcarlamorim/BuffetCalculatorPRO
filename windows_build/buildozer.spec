[app]

# Configurações básicas
title = BuffetCalculatorPRO
package.name = buffetcalculatorpro
package.domain = com.carlos
version = 1.0.0
version.code = 1

# Arquivos
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,json
main.py = main.py  # Confirme se este é seu arquivo principal

# Dependências
requirements = python3,kivy==2.2.1,plyer

# Orientação (portrait para apps de cálculo)
orientation = portrait

# Permissões Android
android.permissions = INTERNET

# Configurações Android
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 23b  # Versão mais leve

# Ícone (adicione um arquivo icon.png na pasta)
icon.filename = %(source.dir)s/icon.png

# Otimizações
android.debug = 0  # Mude para 1 durante desenvolvimento
android.allow_backup = False
android.fullscreen = 0  # Mantém a barra de status
android.wakelock = 0

# Aceleração de hardware
android.hardware_accelerated = 1

# Configurações de tamanho
android.arch = armeabi-v7a  # Para compatibilidade máxima

# Comportamento do teclado
android.softinput_mode = adjust_resize

# Logs (útil para depuração)
log_level = 1
