from pathlib import Path
import zipfile

# Define o diretório onde estão os arquivos
root_dir = Path('files')

# Define o caminho do arquivo zip que será criado
archive_path = root_dir / Path('archive.zip')

# Abre (ou cria) o arquivo zip no modo 'w' (write)
# ⚠️ Se já existir, ele será sobrescrito
with zipfile.ZipFile(archive_path, 'w') as zf:

    # Percorre todos os arquivos .txt dentro da pasta e subpastas
    for path in root_dir.glob('**/*.txt'):

        # Adiciona o arquivo ao zip
        zf.write(path)

        # Remove o arquivo original após compactar
        # ⚠️ Isso é uma ação destrutiva (não tem volta)
        path.unlink()