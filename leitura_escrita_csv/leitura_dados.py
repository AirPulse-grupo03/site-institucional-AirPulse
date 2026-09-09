# Lê arquivos CSV usando os nomes das colunas.
import csv

# Procura arquivos que seguem um padrão de nome.
import glob

# Converte e formata datas e horários.
from datetime import datetime


# Mostra uma mensagem de acordo com o percentual de uso da CPU.
def cpu_use(cpu):

    # As condições são verificadas em ordem.
    # Quando uma delas é atendida, as seguintes não são executadas.
    if cpu < 10.0:
        print("Uso de CPU normal.")

    elif cpu < 30.0:
        print(
            "Uso de CPU moderado. "
            "Operação dentro dos parâmetros esperados."
        )

    elif cpu < 60.0:
        print(
            "Uso de CPU elevado. "
            "Recomenda-se monitoramento."
        )

    elif cpu < 80.0:
        print(
            "Uso de CPU severo. "
            "Avaliar processos que estão consumindo recursos."
        )

    elif cpu < 90.0:
        print(
            "Uso de CPU crítico. "
            "Ação recomendada para evitar degradação do sistema."
        )

    elif cpu < 95.0:
        print(
            "Uso de CPU muito crítico. "
            "Recomenda-se intervenção urgente."
        )

    # Entra aqui quando o uso é de 95% ou mais.
    else:
        print(
            "Uso de CPU extremamente crítico. "
            "Intervenção imediata recomendada."
        )


# Recebe o percentual de uso e a capacidade total da RAM em bytes.
def ram_use(ram, ram_total):

    # Calcula a quantidade de memória usada com base no percentual.
    ram_usada = ram_total * (ram / 100)

    # Converte bytes para GiB, embora as mensagens usem a sigla GB.
    # ** significa potência: 1024 ** 3 é 1024 elevado ao cubo.
    ram_usada_gb = ram_usada / (1024 ** 3)
    ram_total_gb = ram_total / (1024 ** 3)

    # O f antes das aspas permite colocar variáveis dentro das chaves.
    # :.1f mostra uma casa decimal e :.2f mostra duas.
    if ram < 10.0:
        print(
            f"RAM normal: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados)."
        )

    elif ram < 30.0:
        print(
            f"RAM moderada: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados). "
            "Operação dentro dos parâmetros esperados."
        )

    elif ram < 60.0:
        print(
            f"RAM elevada: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados). "
            "Recomenda-se monitoramento."
        )

    elif ram < 80.0:
        print(
            f"RAM severa: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados). "
            "A disponibilidade de memória está reduzida."
        )

    elif ram < 90.0:
        print(
            f"RAM crítica: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados). "
            "Recomenda-se investigar processos com alto consumo de memória."
        )

    elif ram < 95.0:
        print(
            f"RAM muito crítica: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados). "
            "O sistema está próximo do esgotamento de memória."
        )

    else:
        print(
            f"RAM extremamente crítica: {ram:.1f}% "
            f"({ram_usada_gb:.2f} GB de {ram_total_gb:.2f} GB utilizados). "
            "Intervenção técnica imediata recomendada."
        )


# Recebe o percentual de uso e a capacidade total do disco em bytes.
def disco_use(disco, disco_total):

    # Calcula o espaço usado com base no percentual.
    disco_usado = disco_total * (disco / 100)

    # Converte bytes para GiB, embora as mensagens usem a sigla GB.
    disco_usado_gb = disco_usado / (1024 ** 3)
    disco_total_gb = disco_total / (1024 ** 3)

    # Mostra o espaço utilizado e a mensagem correspondente à faixa de uso.
    if disco < 10.0:
        print(
            f"Disco normal: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados)."
        )

    elif disco < 30.0:
        print(
            f"Disco moderado: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados). "
            "Operação dentro dos parâmetros esperados."
        )

    elif disco < 60.0:
        print(
            f"Disco elevado: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados). "
            "Recomenda-se monitoramento."
        )

    elif disco < 80.0:
        print(
            f"Disco severo: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados). "
            "O espaço disponível está sendo reduzido."
        )

    elif disco < 90.0:
        print(
            f"Disco crítico: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados). "
            "Recomenda-se liberar espaço de armazenamento."
        )

    elif disco < 95.0:
        print(
            f"Disco muito crítico: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados). "
            "O armazenamento está próximo da capacidade máxima."
        )

    else:
        print(
            f"Disco extremamente crítico: {disco:.1f}% "
            f"({disco_usado_gb:.2f} GB de {disco_total_gb:.2f} GB utilizados). "
            "Intervenção técnica imediata recomendada."
        )


# Mostra a logo e o título do programa no terminal.
def mostrar_logo():

    # As três aspas permitem escrever um texto com várias linhas.
    # O r mantém barras invertidas como texto literal.
    print(r"""
    █████╗ ██╗██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
   ██╔══██╗██║██╔══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
   ███████║██║██████╔╝██████╔╝██║   ██║██║     ███████╗█████╗
   ██╔══██║██║██╔══██╗██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝
   ██║  ██║██║██║  ██║██║     ╚██████╔╝███████╗███████║███████╗
   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝

                    MONITORAMENTO DE RECURSOS
                CPU • MEMÓRIA RAM • ARMAZENAMENTO
    ==============================================================
""")


# Mostra a logo e as opções disponíveis.
def mostrar_menu():

    mostrar_logo()

    print("""
    +------------------------------------------------------------+
    |                         MENU                               |
    +------------------------------------------------------------+
    |                                                            |
    |                    [1] MONITORAR                           |
    |                    [2] SAIR                                |
    |                                                            |
    +------------------------------------------------------------+
""")


# Lê os dados salvos nos CSVs e calcula o resumo geral.
def processar_dados():

    # Procura arquivos que começam com dados_ e terminam com .csv.
    # ./ representa a pasta de trabalho atual da execução,
    # que não é necessariamente a pasta onde está o código.
    arquivos = glob.glob("./dados_*.csv")

    # Acumulam os percentuais de todos os registros lidos.
    soma_cpu = 0
    soma_ram = 0
    soma_disco = 0

    # Conta quantos registros foram processados para calcular as médias.
    quantidade_registros = 0

    # len retorna a quantidade de arquivos encontrados.
    if len(arquivos) == 0:

        print("""
    +------------------------------------------------------------+
    |                         AVISO                              |
    +------------------------------------------------------------+
    |                                                            |
    |          Nenhum arquivo dados_*.csv encontrado.            |
    |                                                            |
    +------------------------------------------------------------+
""")

        # Encerra esta função quando não há arquivos para ler.
        return

    print("""
    +------------------------------------------------------------+
    |                INICIANDO MONITORAMENTO                     |
    +------------------------------------------------------------+
""")

    # Percorre cada arquivo encontrado.
    for nome_arquivo in arquivos:

        # Abre o arquivo para leitura.
        # UTF-8 é a codificação usada para interpretar o texto.
        # O with fecha o arquivo automaticamente ao sair do bloco.
        with open(
            nome_arquivo,
            mode="r",
            encoding="utf-8"
        ) as arquivo:

            # Usa a primeira linha como cabeçalho.
            # Cada registro é lido como um dicionário:
            # o nome da coluna é a chave e o conteúdo é o valor.
            leitor = csv.DictReader(arquivo)

            # Percorre os registros do arquivo, sem incluir o cabeçalho.
            for linha in leitor:

                # Pega o conteúdo da coluna username.
                username = linha["username"]

                # Transforma a data escrita no CSV em um objeto datetime.
                # O formato esperado é ano-mês-dia hora:minuto:segundo.
                timestamp = datetime.strptime(
                    linha["timestamp"],
                    "%Y-%m-%d %H:%M:%S"
                )

                # Os valores do CSV chegam como texto.
                # float converte esses valores para números decimais.
                cpu = float(linha["cpu"])
                ram = float(linha["ram"])
                ram_total = float(linha["ram_total"])
                disco = float(linha["disco"])
                disco_total = float(linha["disco_total"])

                # += soma o novo valor ao que já estava na variável.
                soma_cpu += cpu
                soma_ram += ram
                soma_disco += disco

                # Conta mais um registro processado.
                quantidade_registros += 1

                # Mostra os dados do registro atual.
                # \n pula uma linha.
                # strftime formata a data para dia/mês/ano hora:minuto:segundo.
                print(
                    "\n \n \n "
                    "==============================================================\n"
                    f"Usuário: {username}\n"
                    f"Horário: {timestamp.strftime('%d/%m/%Y %H:%M:%S')}\n"
                    "--------------------------------------------------------------\n"
                    f"CPU:   {cpu:.1f}%\n"
                    f"RAM:   {ram:.1f}%\n"
                    f"Disco: {disco:.1f}%\n"
                    "=============================================================="
                )

                # Chama cada função com os valores do registro atual.
                print("\n[ CPU ]")
                cpu_use(cpu)

                print("\n[ MEMÓRIA RAM ]")
                ram_use(ram, ram_total)

                print("\n[ DISCO ]")
                disco_use(disco, disco_total)

    # Só calcula as médias se houver registros, evitando divisão por zero.
    if quantidade_registros > 0:

        # Calcula a média dos percentuais de todos os arquivos juntos.
        # Cada registro tem o mesmo peso no cálculo.
        media_cpu = soma_cpu / quantidade_registros
        media_ram = soma_ram / quantidade_registros
        media_disco = soma_disco / quantidade_registros

        # Mostra a quantidade de registros e as médias calculadas.
        print(
            "\n\n"
            "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
            "+                   RESUMO GERAL DOS FMC                     +\n"
            "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
            f"\nRegistros analisados: {quantidade_registros}\n"
            "\n"
            "--------------------------- CPU ------------------------------\n"
            f"Média de utilização: {media_cpu:.1f}%\n"
            "\n"
            "--------------------------- RAM ------------------------------\n"
            f"Média de utilização: {media_ram:.1f}%\n"
            "\n"
            "-------------------------- DISCO -----------------------------\n"
            f"Média de utilização: {media_disco:.1f}%\n"
            "\n"
            "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        )


# Controla o menu e a escolha do usuário.
def iniciar():

    # Repete o menu até que o break seja executado.
    while True:

        mostrar_menu()

        # input espera o usuário digitar e pressionar ENTER.
        # O valor recebido é um texto, por isso as comparações usam aspas.
        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            print("\nOpção selecionada: Monitorar\n")

            # Lê e analisa os arquivos CSV.
            processar_dados()

            # Aguarda ENTER antes de mostrar o menu novamente.
            input(
                "\nPressione ENTER para voltar ao menu..."
            )

        elif opcao == "2":

            print("""
    +------------------------------------------------------------+
    |                                                            |
    |                  AIRPULSE ENCERRADO                        |
    |                                                            |
    +------------------------------------------------------------+
""")

            # Sai do while e encerra a função.
            break

        else:

            # Avisa quando o usuário digita algo diferente de 1 ou 2.
            print("""
    +------------------------------------------------------------+
    |                     OPÇÃO INVÁLIDA                         |
    +------------------------------------------------------------+
    |                                                            |
    |                Digite 1 para Monitorar                     |
    |                Digite 2 para Sair                          |
    |                                                            |
    +------------------------------------------------------------+
""")


# Chama a função que inicia o programa.
iniciar()