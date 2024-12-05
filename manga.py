from datetime import datetime


class Manga:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.usuario = None
        self.data_emprestimo = None

    def emprestar(self, usuario):
        if self.disponivel:
            self.disponivel = False
            self.usuario = usuario
            self.data_emprestimo = datetime.now()
            print(f"Manga '{self.titulo}' emprestado para {usuario} em {self.data_emprestimo.strftime('%d/%m/%Y às %H:%M')}.")
        else:
            print(f"O manga '{self.titulo}' já está emprestado para {self.usuario}.")

    def devolver(self):
        if not self.disponivel:
            print(f"Manga '{self.titulo}' devolvido por {self.usuario}.")
            self.disponivel = True
            self.usuario = None
            self.data_emprestimo = None
        else:
            print(f"O manga '{self.titulo}' já está disponível na biblioteca.")

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.usuario} em {self.data_emprestimo.strftime('%d/%m/%Y às %H:%M')}"
        return f"Título: {self.titulo}, Autor: {self.autor}, Status: {status}"
