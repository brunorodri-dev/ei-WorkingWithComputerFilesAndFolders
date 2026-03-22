from pathlib import Path
from datetime import datetime

# Define o diretório raiz onde os arquivos estão localizados
# Pode ser um caminho relativo (como aqui) ou absoluto
root_dir = Path('files')

# Percorre todos os arquivos .txt dentro da pasta e subpastas (recursivamente)
# '**/*.txt' → busca em todas as subpastas arquivos com extensão .txt
for path in root_dir.glob('**/*.txt'):

    # Garante que estamos lidando apenas com arquivos (evita erros com diretórios)
    if path.is_file():

        # Obtém informações do arquivo (metadata do sistema)
        # stat() retorna dados como tamanho, datas, permissões, etc.
        file_stats = path.stat()

        # Converte o timestamp de criação (st_ctime) para um objeto datetime
        # ⚠️ No Windows: geralmente é data de criação
        # ⚠️ No Linux: pode ser última alteração de metadata
        created_date = datetime.fromtimestamp(file_stats.st_ctime)

        # Formata a data para string
        # ⚠️ Importante: usar "-" no lugar de ":" (Windows não permite ":" em nomes de arquivo)
        # Exemplo: 2026-03-22_18-00-10
        created_date_str = created_date.strftime('%Y-%m-%d_%H-%M-%S')

        # Cria um novo nome de arquivo com timestamp + nome original
        # Ex: 2026-03-22_18-00-10_relatorio.txt
        new_filename = f"{created_date_str}_{path.name}"

        # Cria um novo caminho mantendo a mesma pasta, apenas alterando o nome
        new_filepath = path.with_name(new_filename)

        # Renomeia o arquivo (também poderia mover se o caminho fosse diferente)
        path.rename(new_filepath)

        # Exibe o timestamp usado (útil para debug/log)
        print(created_date_str)