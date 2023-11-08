import time

class Relogio:
    def mostrar_hora(self):
        hora_atual = time.strftime("%H:%M:%S")
        print("Hora atual:", hora_atual)

relogio = Relogio()
relogio.mostrar_hora()
