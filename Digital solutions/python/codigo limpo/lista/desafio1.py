import  time
def contagem(tempo):
    for i in range (tempo, 0 , -1):
        print(f"Contagem:{i}")
        time.sleep(1)
    print("FIM")


tempo = int(input("quanto vai ser a contagem regresiva: "))
contagem(tempo)

