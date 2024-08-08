from api_client import APIConfig

class Department:
    def __init__(self, client: APIConfig) -> None:
        self.client = client

    def all(self):
        return self.client.get('Departamentos')
    
    def create(self, description, n_folha=''):
        data = {
            'Descricao': description,
            'Nfolha': n_folha
        }
        return self.client.post('Departamentos', data=data)

    def delete(self, description):
        endpoint = f"Departamentos?descricao={description}"
        return self.client.delete(endpoint)
    
    def treat_justifications(self):
        action = input("Deseja (v)isualizar, (c)adastrar ou (d)eletar um departamento? ").lower()
        if action == 'v':
            departments = self.all()
            print("Departamentos:", departments)
        elif action == 'c':
            description = input("Informe a descrição do departamento: ")
            nfolha = input("Informe o número da folha (opcional): ")
            response = self.create(description, nfolha)
            print(f"Departamento {description} cadastrado: {response}")
        elif action == 'd':
            description = input("Informe a descrição do departamento que deseja deletar: ")
            response = self.delete(description)
            print(f"Departamento {description} deletado: {response}")