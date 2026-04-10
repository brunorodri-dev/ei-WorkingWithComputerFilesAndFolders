📂 Manipulação de Arquivos com PathlibRepositório de exemplos práticos para automação de arquivos em Python, evoluindo do básico ao avançado.🚀 Por que Pathlib?Diferente do antigo os.path, o pathlib trata caminhos como objetos, tornando o código mais legível e multiplataforma.📚 Índice de ExemplosArquivoDescriçãoFunções Principaisex01-02Fundamentos e Renomeaçãoexists(), name, rename()ex03-04Estrutura e Hierarquiaglob(), parts, parentex05-06Datas e Extensõesstat(), with_suffix()ex07-11Automação e Limpezatouch(), zipfile, rglob(), unlink()🛠️ Comandos Essenciais (Cheat Sheet)

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