import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyCID14ihLwqWxMXVg9RVxWuNVpaNYPytbg'
genai.configure(api_key=GOOGLE_API_KEY)


generation_config = {
    "candidate_count":1,
    "temperature":0.4, 
}
safety_settings = {
    "HARASSMENT": 'BLOCK_MEDIUM_AND_ABOVE',
    "HATE": 'BLOCK_MEDIUM_AND_ABOVE',
    "SEXUAL": 'BLOCK_MEDIUM_AND_ABOVE',
    "DANGEROUS": 'BLOCK_MEDIUM_AND_ABOVE'
}
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", #Utilizei o 1.5 para colocar instruções a ele.
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                               system_instruction="Você precisa analisar quão bravo o cliente está, para isso será passado uma nota de 1 (mais calmo) a 5 (mais bravo) e adaptar uma mensagem conforme o nível da nota, tente reter esse aluno sem oferecer benefícios extras, mostre somente a mensagem para enviar e uma análise da situação no prompt, analise por onde foi feita a conversa (WhatsApp ou E-mail) e adapte"
                              ) #Adaptei as instruções conforme situações que passamos durante algum atendimento mais complicado.

#Ele vai capturar a mensagem do aluno e passo um nível de insatisfação que notei sobre o cliente e também o meio de comunicação, para adaptar a linguagem, com isso podemos ter uma resposta mais assertiva.
mensagem_cliente = input("Digite a mensagem do aluno: ")
nota = input("Qual nível de insatisfação do cliente?(1 à 5): ")
meio_comunicacao = input("Por onde você recebeu essa mensagem?(Whatsapp ou Email): ")
instructions = model.generate_content(f"A nota de insatisfação é {nota} e a mensagem recebida foi: {mensagem_cliente} Por meio de um {meio_comunicacao}")
print(instructions.text)