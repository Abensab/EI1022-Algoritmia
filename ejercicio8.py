class Estudiante:
    __slots__ = ('nombre', 'diccionario')

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.diccionario = {}

    def califica(self, asignatura: str, nota: float):
        self.diccionario[asignatura] = nota

    def nota(self, asignatura: str):
        return self.diccionario.get(asignatura) if asignatura in self.diccionario.keys() else None

    def media(self):
        return (sum(v for k, v in self.diccionario.items()) / len(self.diccionario) if len(self.diccionario) > 0 else None)


    def muestra_expediente(self):
        return self.nombre+'\n'+''.join(
            '\t {0} - {1}\n'.format(str(k), str(v)) for k, v in self.diccionario.items())


es = Estudiante("PACO")
es.califica("EI02", 3.05)
es.califica("EI04", 10.0)
print(es.nota("EI02"))
print(es.media())
print(es.muestra_expediente())
