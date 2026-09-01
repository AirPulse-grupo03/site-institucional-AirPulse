import csv
import glob
from datetime import datetime


def cpu_use(cpu):

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

    else:
        print(
            "Uso de CPU extremamente crítico. "
            "Intervenção imediata recomendada."
        )


def ram_use(ram, ram_total):

    ram_usada = ram_total * (ram / 100)

    ram_usada_gb = ram_usada / (1024 ** 3)
    ram_total_gb = ram_total / (1024 ** 3)

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


def disco_use(disco, disco_total):

    disco_usado = disco_total * (disco / 100)

    disco_usado_gb = disco_usado / (1024 ** 3)
    disco_total_gb = disco_total / (1024 ** 3)

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


def mostrar_logo():

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


def processar_dados():

    arquivos = glob.glob("./dados_*.csv")

    soma_cpu = 0
    soma_ram = 0
    soma_disco = 0
    quantidade_registros = 0

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

        return

    print("""
    +------------------------------------------------------------+
    |                INICIANDO MONITORAMENTO                     |
    +------------------------------------------------------------+
""")

    for nome_arquivo in arquivos:

        with open(
            nome_arquivo,
            mode="r",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.DictReader(arquivo)

            for linha in leitor:

                username = linha["username"]

                timestamp = datetime.strptime(
                    linha["timestamp"],
                    "%Y-%m-%d %H:%M:%S"
                )

                cpu = float(linha["cpu"])
                ram = float(linha["ram"])
                ram_total = float(linha["ram_total"])
                disco = float(linha["disco"])
                disco_total = float(linha["disco_total"])

                soma_cpu += cpu
                soma_ram += ram
                soma_disco += disco

                quantidade_registros += 1

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

                print("\n[ CPU ]")
                cpu_use(cpu)

                print("\n[ MEMÓRIA RAM ]")
                ram_use(ram, ram_total)

                print("\n[ DISCO ]")
                disco_use(disco, disco_total)

    if quantidade_registros > 0:

        media_cpu = soma_cpu / quantidade_registros
        media_ram = soma_ram / quantidade_registros
        media_disco = soma_disco / quantidade_registros

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


def iniciar():

    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            print("\nOpção selecionada: Monitorar\n")

            processar_dados()

            input(
                "\nPressione ENTER para voltar ao menu..."
            )

        elif opcao == "2":

            print("""
    +------------------------------------------------------------+
    |                                                            |
    |                  AIRPULSE ENCERRADO                         |
    |                                                            |
    +------------------------------------------------------------+
""")

            break

        else:

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


iniciar()   