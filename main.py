from config import API_BASE_URL, API_AUTH_BASE_URL, USERNAME, PASSWORD
from api_client import APIConfig
from department import Department
from justification import Justification
from funcoes import Funcoes

def main():
    client = APIConfig(
        auth_url=API_AUTH_BASE_URL,
        api_url=API_BASE_URL,
        username=USERNAME,
        password=PASSWORD
    )

    # bank_id = input("Digite o numero do banco de dados")
    bank_id = '98294'
    client.set_bank_id(bank_id)

    while True:
        action = input("O que gostaria de ver:\n1 - Departamento\n2 - Justificativa\n3 - Funções\n4 - Sair\n")

        match action:
            case '1':
                department = Department(client)
                department.treat_justifications()
            case '2':
                justification = Justification(client)
                justification.treat_justifications()
            case '3':
                functions = Funcoes(client)
                functions.treat_justifications()
            case '4':
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente.")
                
if __name__ == '__main__':
    main()