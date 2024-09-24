from Corrida import Corrida
from Passageiro import Passageiro
class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_driver)
        self.add_command("read", self.read_driver)
        self.add_command("update", self.update_driver)
        self.add_command("delete", self.delete_driver)

    def create_driver(self):
        nota = int(input("Entre com a nota do Motorista: "))
        quantCorridas = int(input("Entre com a quantidade de Corridas Realizadas: "))
        corridas = []
        for i in range(quantCorridas):
            notaCorrida = int(input("Entre com a nota da Corrida %d: " % i))
            distanciaCorrida = float(input("Entre com a distancia da Corrida %d: " % i))
            valorCorrida = float(input("Entre com o valor da Corrida %d: " % i))
            nomePassageiro = input("Entre com o nome do Passageiro da Corrida %d: " % i)
            nomeDocumento = input("Entre com o documento do Passageiro da Corrida %d: " % i)

            passageiro = Passageiro(nomePassageiro, nomeDocumento).__dict__
            corrida = Corrida(notaCorrida, distanciaCorrida, valorCorrida, passageiro).__dict__
            corridas.append(corrida)
        self.motorista_model.create_driver(nota, corridas)

    def read_driver(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_driver_by_id(id)
        if motorista:
            print(f"Nota: {motorista['nota']}")
            print(f"Corridas: {motorista['corridas']}")

    def update_driver(self):
        id = input("Entre com o id: ")
        nota = int(input("Entre com a nova nota do Motorista: "))
        quantCorridas = int(input("Entre com a nova quantidade de Corridas Realizadas: "))
        corridas = []
        for i in range(quantCorridas):
            notaCorrida = int(input("Entre com a nova nota da Corrida %d: " % i))
            distanciaCorrida = float(input("Entre com a nova distancia da Corrida %d: " % i))
            valorCorrida = float(input("Entre com o novo valor da Corrida %d: " % i))
            nomePassageiro = input("Entre com o novo nome do Passageiro da Corrida %d: " % i)
            nomeDocumento = input("Entre com o novo documento do Passageiro da Corrida %d: " % i)

            passageiro = Passageiro(nomePassageiro, nomeDocumento).__dict__
            corrida = Corrida(notaCorrida, distanciaCorrida, valorCorrida, passageiro).__dict__
            corridas.append(corrida)
        self.motorista_model.update_driver(id, nota, corridas)

    def delete_driver(self):
        id = input("Entre com o id: ")
        self.motorista_model.delete_driver(id)
        
    def run(self):
        print("Welcome to the Driver CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
