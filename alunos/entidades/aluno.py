class Aluno:
    def __init__(self, nome, sexo, niver_data, telefone, sala):
        self._nome = nome
        self._sexo = sexo
        self._niver_data = niver_data
        self._telefone = telefone
        self._sala = sala

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def niver_data(self):
        return self._niver_data

    @niver_data.setter
    def niver_data(self, niver_data):
        self._niver_data = niver_data

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def sala(self):
        return self._sala

    @sala.setter
    def sala(self, sala):
        self._sala = sala
