from ClasePersonal import Personal
class Investigador(Personal):
    __areaInv: str
    __tipoInv: str

    def __init__(self, **kwargs):
        self.__areaInv = kwargs["area"]
        self.__tipoInv = kwargs["tipo"]
        super().__init__(**kwargs)

    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getArea(self):
        return self.__areaInv

    def getTipo(self):
        return self.__tipoInv

    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getCuil(),
                    apellido= self.getApellido(),
                    nombre= self.getNombre(),
                    sueldo= self.getSueldo(),
                    anti= self.getAnti(),
                    area = self.__areaInv,
                    tipo = self.__tipoInv
                )
            )
            return d
