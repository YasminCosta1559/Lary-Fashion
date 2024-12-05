from manga import Manga

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.mangas = []
        self.usuarios = {}

    def adicionar_manga(self, manga):
        self.mangas.append(manga)
        print(f"Manga '{manga.titulo}' adicionado à biblioteca '{self.nome}'.")

    def listar_mangas(self):
        print(f"Mangas disponíveis na biblioteca '{self.nome}':")
        for manga in self.mangas:
            print(manga)

    def buscar_manga(self, titulo):
        for manga in self.mangas:
            if manga.titulo.lower() == titulo.lower():
                return manga
        print(f"Manga '{titulo}' não encontrado na biblioteca.")
        return None

    def cadastrar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = None
            print(f"Usuário '{nome}' cadastrado com sucesso.")
        else:
            print(f"Usuário '{nome}' já está cadastrado.")

    def pegar_manga(self, nome_usuario, titulo):
        if nome_usuario not in self.usuarios:
            print(f"Usuário '{nome_usuario}' não está cadastrado. Cadastre-se primeiro.")
            return

        if self.usuarios[nome_usuario] is not None:
            print(f"Usuário '{nome_usuario}' precisa devolver o manga '{self.usuarios[nome_usuario].titulo}' antes de pegar outro.")
            return

        manga = self.buscar_manga(titulo)
        if manga and manga.disponivel:
            manga.emprestar(nome_usuario)
            self.usuarios[nome_usuario] = manga
        elif manga:
            print(f"O manga '{titulo}' não está disponível.")

    def devolver_manga(self, nome_usuario):
        if nome_usuario not in self.usuarios:
            print(f"Usuário '{nome_usuario}' não está cadastrado. Cadastre-se primeiro.")
            return

        manga = self.usuarios[nome_usuario]
        if manga is None:
            print(f"Usuário '{nome_usuario}' não tem nenhum manga para devolver.")
        else:
            manga.devolver()
            self.usuarios[nome_usuario] = None
