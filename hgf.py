print(" Anamnese Psicológica")

nome_do_paciente = input("Qual o nome do paciente? ")
idade = int(input("Qual a idade do paciente? "))
altura = float(input("Qual a altura do paciente? (em metros) "))
ansiedade = input("O paciente apresenta sintomas de ansiedade? (True/False) ") == "True"
depressao = input("O paciente já foi diagnosticado com depressão? (True/False) ") == "True"
medicacao = input("O paciente faz uso de medicação controlada? (True/False) ") == "True"
tempo_sono = float(input("Quantas horas o paciente dorme por noite? "))
dorme_bem = tempo_sono >= 7
relacionamento = input("O paciente tem um bom relacionamento familiar? (Sim/Não) ")
trabalho_estresse = int(input("De 0 a 10, qual o nível de estresse no trabalho? "))
relacionamento = input("O paciente tem um bom relacionamento familiar? (Sim/Não) ")
trabalho_estresse = int(input("De 0 a 10, qual o nível de estresse no trabalho? "))
atividade_fisica = input("O paciente pratica atividade física regularmente? (Sim/Não) ")
alimentacao = input("O paciente mantém uma alimentação equilibrada? (Sim/Não) ")
uso_substancias = input("O paciente faz uso de álcool, tabaco ou outras substâncias? (Sim/Não) ")
episodios_estresse = input("O paciente já teve episódios recentes de estresse intenso? (Sim/Não) ")
horas_trabalho = int(input("Quantas horas o paciente trabalha por dia? "))
satisfacao_trabalho = input("O paciente está satisfeito com o trabalho? (Sim/Não) ") == "Sim"
suporte_social = input("O paciente sente que tem apoio social? (Sim/Não) ") == "Sim"
idade_inicial_terapia = float(input("Há quanto tempo o paciente iniciou a terapia? (em anos) "))