from pathlib import Path

# Define o diretório onde os arquivos serão criados
root_dir = Path('files')

# Loop de 1 até 20 (range não inclui o último número, por isso vai até 21)
for i in range(1, 21):

    # Cria o nome do arquivo como string
    # Ex: '1.txt', '2.txt', ..., '20.txt'
    filename = str(i) + '.txt'

    # Combina o diretório com o nome do arquivo
    # root_dir / filename → forma moderna de criar caminhos com pathlib
    file_path = root_dir / filename

    # Cria o arquivo vazio
    # Se o arquivo já existir, não sobrescreve (comportamento seguro)
    file_path.touch()