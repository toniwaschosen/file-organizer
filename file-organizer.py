import os

#=============================
# CRIAÇÃO DAS PASTAS
#=============================
tipos_de_arquivo = []
for file in os.listdir():
    if os.path.isfile(file) and '.' in file:
        extensao = (file.split('.'))[-1].lower()
        tipos_de_arquivo.append(extensao)
        
tipos_de_arquivo = set(tipos_de_arquivo)
print('Tipos de arquivos encontrados:', tipos_de_arquivo)
    
for pasta in tipos_de_arquivo:
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        
#===============================
# ORGANIZAÇÃO DOS ARQUIVOS
#===============================
script_atual = os.path.basename(__file__)
for file in os.listdir():
    if os.path.isfile(file) and '.' in file and file != script_atual:
        extensao = (file.split('.'))[-1].lower()
        destino = os.path.join(extensao, file)
        os.rename(file, destino)