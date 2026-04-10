

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