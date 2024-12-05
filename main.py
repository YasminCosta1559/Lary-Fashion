from manga import Manga
from biblioteca import Biblioteca
from datetime import datetime

biblioteca = Biblioteca("Biblioteca Central")

mangas = [
    Manga("Naruto", "Masashi Kishimoto"),
    Manga("One Piece", "Eiichiro Oda"),
    Manga("Attack on Titan", "Hajime Isayama"),
    Manga("Dragon Ball", "Akira Toriyama"),
    Manga("My Hero Academia", "Kohei Horikoshi"),
]

for manga in mangas:
    biblioteca.adicionar_manga(manga)

usuario_cadastrado = False
manga_emprestado = False
usuario_atual = None

def mostrar_ajuda():
    print("\n=== Bem-vindo(a) à Ajuda! ===")
    print("Precisa de uma mãozinha para usar o sistema? Aqui vai:")
    print("\n- *Cadastrar usuário*: O primeiro passo é se cadastrar. Afinal, precisamos saber quem você é!")
    print("- *Listar mangas disponíveis*: Explore nosso acervo e veja quais mangas estão disponíveis.")
    print("- *Pegar manga emprestado*: Escolha um dos nossos mangas, mas lembre-se: apenas um por vez.")
    print("- *Devolver manga*: Terminou de ler? Devolva o manga para que outros possam aproveitar.")
    print("- *Sair*: Encerre o programa quando terminar.")
    print("\nFique à vontade para explorar nossa biblioteca. Se precisar, volte aqui para mais ajuda!")
    print("=============================\n")

# Loop principal
while True:
    print("\n")
    print(f"{biblioteca.nome.center(50, ' ')}")
    print(f"Bem-vindo(a) à nossa biblioteca! Escolha uma opção abaixo:\n".center(50, ' '))

    print("\nOpções:")
    if not usuario_cadastrado:
        print("1. Cadastrar usuário")
    print("2. Listar mangas disponíveis")
    print("3. Ajuda")
    print("4. Sair")
    if usuario_cadastrado:
        print("5. Pegar manga emprestado")
        if manga_emprestado:
            print("6. Devolver manga")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if not usuario_cadastrado:
            nome = input("Digite seu nome: ")
            biblioteca.cadastrar_usuario(nome)
            print(f"Bem-vindo(a) à {biblioteca.nome}, {nome}!")
            usuario_cadastrado = True
            usuario_atual = nome
        else:
            print("Você já está cadastrado.")
    elif opcao == "2":
        biblioteca.listar_mangas()
    elif opcao == "3":
        mostrar_ajuda()
    elif opcao == "4":
        if manga_emprestado:
            print(f"{usuario_atual}, você ainda está com um manga emprestado. Por favor, devolva-o antes de sair.")
            biblioteca.devolver_manga(usuario_atual)
            manga_emprestado = False
        print("Obrigado por usar a nossa biblioteca. Foi um prazer ter você por aqui! Até a próxima!")
        break
    elif opcao == "5" and usuario_cadastrado:
        titulo = input(f"{usuario_atual}, digite o título do manga que deseja pegar emprestado: ")
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        biblioteca.pegar_manga(usuario_atual, titulo)
        manga_emprestado = True
        print(f"Manga emprestado em: {data_hora}")
    elif opcao == "6" and usuario_cadastrado and manga_emprestado:
        biblioteca.devolver_manga(usuario_atual)
        manga_emprestado = False
    else:
        print("Opção inválida ou indisponível. Tente novamente.")