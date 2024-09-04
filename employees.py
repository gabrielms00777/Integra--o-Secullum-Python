from api_client import APIConfig

class Employees:
    def __init__(self, client: APIConfig):
        self.client = client
        self.standard_employees = self.standard_employees = [
    {
        "Nome": "ODETE GALVAO BARBOSA DE OLIVEIRA",
        "Cpf": "178.755.758-85",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "FAXINEIRO",
        "NumeroFolha": "001025",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "07/06/2010",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "166.472.885.71"
    },
    {
        "Nome": "PATRICIA APARECIDA NUNES DE SOUSA",
        "Cpf": "215.238.528-44",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "PORTEIRA",
        "NumeroFolha": "001035",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "07/04/2011",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "126.328.431.64"
    },
    {
        "Nome": "ELIAS DE JESUS COSTA",
        "Cpf": "071.468.068-04",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "PORTEIRO DE EDI",
        "NumeroFolha": "001039",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "02/01/2013",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "121.517.315.20"
    },
    {
        "Nome": "DAYANE FRANCIS DE OLIVEIRA",
        "Cpf": "348.510.848-03",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "FAXINEIRO (A) FERISTA",
        "NumeroFolha": "001057",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "26/01/2015",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "128.120.631.67"
    },
    {
        "Nome": "LUIS HENRIQUE SIMAO DOS SANTOS",
        "Cpf": "426.295.578-80",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "PORTEIRO",
        "NumeroFolha": "002021",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "01/05/2017",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "164.833.729.82"
    },
    {
        "Nome": "CARLOS ALBERTO PEREIRA DA SILVA",
        "Cpf": "088.583.828-97",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "ZELADOR",
        "NumeroFolha": "002040",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "19/08/2019",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "120.848.502.92"
    },
    {
        "Nome": "SABINO FRANCISCO DOS SANTOS",
        "Cpf": "887.217.526-72",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "FAXINEIRO(A)",
        "NumeroFolha": "002046",
        "Cidade": "SERRANA",
        "Admissao": "26/05/2020",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "123.989.751.60"
    },
    {
        "Nome": "RODRIGO BARBOZA DE OLIVEIRA",
        "Cpf": "159.757.218-73",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "PORTEIRO",
        "NumeroFolha": "003022",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "17/02/2024",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "124.927.947.94"
    },
    {
        "Nome": "RAFAEL MALVASO DANTAS",
        "Cpf": "318.026.528-09",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "PORTEIRO (A) FERISTA",
        "NumeroFolha": "003025",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "29/07/2024",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "129.720.031.54"
    },
    {
        "Nome": "ELAINE DA SILVA",
        "Cpf": "156.232.168-46",
        "DepartamentoDescricao": "MUDAR",
        "FuncaoDescricao": "FAXINEIRA",
        "NumeroFolha": "003026",
        "Cidade": "RIBEIRAO PRETO",
        "Admissao": "26/08/2024",
        "EmpresaCnpjCpf": "10914074000197",
        "HorarioNumero": "1",
        "NumeroPis": "124.151.641.37"
    }
]


    def all(self):
        return self.client.get('Funcionarios')

    def create(self, nome, numero_folha, cpf, numero_pis, admissao, empresa_cnpj_cpf, horario_numero, departamento_descricao, funcao_descricao):
        data = {
            'Nome': nome,
            'NumeroFolha': numero_folha,
            'Cpf': cpf,
            'NumeroPis': numero_pis,
            'Admissao': admissao,
            'EmpresaCnpjCpf': empresa_cnpj_cpf,
            'HorarioNumero': horario_numero,
            'DepartamentoDescricao': departamento_descricao,
            'FuncaoDescricao': funcao_descricao
        }

        return self.client.post('Funcionarios', data)
    
    def standard_record(self):
        for employee in self.standard_employees:
            nome = employee['Nome']
            numero_folha = employee['NumeroFolha']
            cpf = employee['Cpf']
            numero_pis = employee['NumeroPis']
            admissao = employee['Admissao']
            empresa_cnpj_cpf = employee['EmpresaCnpjCpf']
            horario_numero = employee['HorarioNumero']
            departamento_descricao = employee['DepartamentoDescricao']
            funcao_descricao = employee['FuncaoDescricao']
            
            response = self.create(
                nome,
                numero_folha,
                cpf,
                numero_pis,
                admissao,
                empresa_cnpj_cpf,
                horario_numero,
                departamento_descricao,
                funcao_descricao
            )
            print(f"Funcionário {employee['Nome']} cadastrado: {response}")

    def treat_justifications(self):
        option = input("Cadastrar Funcionarios? ").lower()

        match option:
            case 's':
                # print("Funcionarios:", self.all())
                print(self.standard_record())

            