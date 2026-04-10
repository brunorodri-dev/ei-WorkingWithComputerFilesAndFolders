📂 Manipulação de Arquivos com Pathlib Repositório de exemplos práticos para automação de arquivos em Python, evoluindo do básico ao avançado. 

🚀 Por que Pathlib? Diferente do antigo os.path, o pathlib trata caminhos como objetos, tornando o código mais legível e multiplataforma.

📚 Índice de Exemplos Arquivo Descrição Funções Principais ex01-02 Fundamentos e Renomeação exists(), name, rename()ex03-04 Estrutura e Hierarquiaglob (), parts, parent ex05-06 Datas e Extensões stat(), with_suffix () ex07-11 Automação e Limpeza touch(), zipfile, rglob(), unlink()

🛠️ Comandos Essenciais (Cheat Sheet)

# Criar referência e verificar propriedades
p = Path("docs/relatorio.pdf")
print(p.stem)    # relatorio
print(p.suffix)  # .pdf

# Busca recursiva (procura em todas as subpastas)
for arq in Path(".").rglob("*.txt"):
    print(arq)

# Criar, Alterar Extensão e Deletar
p.touch()                        # Cria arquivo vazio
p.with_suffix(".txt")            # Simula troca de extensão
# p.unlink()                     # Deleta o arquivo
