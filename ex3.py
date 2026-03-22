from pathlib import Path

# Define o diretório raiz
root_dir = Path('files')

# Busca recursivamente todos os arquivos .txt dentro de "files"
# '**/*.txt' → significa:
# **  = todas as subpastas
# *.txt = todos os arquivos com extensão .txt
file_paths = root_dir.glob('**/*.txt')

# Percorre todos os caminhos encontrados
for path in file_paths:

    # Garante que estamos lidando com um arquivo (boa prática)
    if path.is_file():

        # path.parts → retorna uma tupla com cada parte do caminho
        # Ex: ('files', 'subpasta', 'arquivo.txt')
        # [-2] → pega o nome da pasta pai
        parent_folder = path.parts[-2]

        # Cria um novo nome:
        # Ex: subpasta_arquivo.txt
        new_filename = f"{parent_folder}_{path.name}"

        print(f"New filename: {new_filename}")

        # Cria o novo caminho com o nome atualizado
        # Mantém o arquivo na mesma pasta
        new_filepath = path.with_name(new_filename)

        print(f"Final path: {new_filepath}")

        # Renomeia o arquivo
        path.rename(new_filepath)