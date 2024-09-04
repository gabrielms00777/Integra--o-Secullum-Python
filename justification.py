from api_client import APIConfig

class Justification:
    def __init__(self, client: APIConfig) -> None:
        self.client = client
        self.standard_justifications = [
            # {'NomeAbreviado': 'TES1', 'NomeCompleto': 'TESTE 1'},
            # {'NomeAbreviado': 'TES2', 'NomeCompleto': 'TESTE 2'},
            # {'NomeAbreviado': 'TES3', 'NomeCompleto': 'TESTE 3'},
            {'NomeAbreviado': 'D MED', 'NomeCompleto': 'DECLARACAO MEDICA'},
            {'NomeAbreviado': 'AT MED', 'NomeCompleto': 'ATESTADO MEDICO'},
            {'NomeAbreviado': 'FALTA', 'NomeCompleto': 'FALTA INJUSTIFICADA', 'DescontarDsr': True, 'LancarComoHorasFalta': True},
            {'NomeAbreviado': 'FERIAS', 'NomeCompleto': 'FERIAS'},
            {'NomeAbreviado': 'FOLGA', 'NomeCompleto': 'FOLGA'},
            {'NomeAbreviado': 'INSS', 'NomeCompleto': 'AFASTAMENTO INSS'},
            {'NomeAbreviado': 'LIC MAT', 'NomeCompleto': 'LICENCA MATERNIDADE'},
            {'NomeAbreviado': 'LIC PAT', 'NomeCompleto': 'LICENCA PATERNIDADE'},
            {'NomeAbreviado': 'REUNIAO', 'NomeCompleto': 'REUNIAO'},
            {'NomeAbreviado': 'SERV EX', 'NomeCompleto': 'SERVICO EXTERNO'},
            {'NomeAbreviado': 'LUTO', 'NomeCompleto': 'LUTO FAMILIAR'},
        ]

    def all(self):
        return self.client.get('Justificativas')

    def create(self, short_name, full_name, discount_dsr=False, launch_like_hours_missing=False):
        data = {
            'NomeAbreviado': short_name,
            'NomeCompleto': full_name,
            'DescontarDsr': discount_dsr,
            'LancarComoHorasFalta': launch_like_hours_missing
        }

        return self.client.post('Justificativas', data)
    
    def delete(self, short_name):
        return self.client.delete(f'Justificativas?nomeAbreviado={short_name}')
    
    def standard_record(self):
        for justification in self.standard_justifications:
            short_name = justification['NomeAbreviado']
            full_name = justification['NomeCompleto']
            discount_dsr = justification.get('DescontarDsr', False)
            launch_like_hours_missing = justification.get('LancarComoHorasFalta', False)
            
            response = self.create(
                short_name,
                full_name,
                discount_dsr,
                launch_like_hours_missing
            )
            print(f"Justificativa {justification['NomeAbreviado']} cadastrada: {response}")

    def treat_justifications(self):
        option = input("Deseja cadastrar as justificativas padrão? (s/n): ").lower()

        if option == 's':
            self.standard_record()
        else:
            action = input("Deseja (v)isualizar ou (c)adastrar uma nova justificativa? ").lower()

            if action == 'v':
                justificativas = self.all()
                print("Justificativas:", justificativas)
            elif action == 'c':
                short_name = input("Informe o nome abreviado da justificativa: ")
                full_name = input("Informe o nome completo da justificativa: ")
                discount_dsr = input("Descontar DSR? (s/n): ").lower() == 's'
                launch_like_hours_missing = input("Lançar como horas falta? (s/n): ").lower() == 's'
                response = self.create(short_name, full_name, discount_dsr, launch_like_hours_missing)
                print(f"Justificativa {short_name} cadastrada: {response}")