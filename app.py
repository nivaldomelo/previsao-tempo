import tkinter as tk
import requests
import openpyxl
from datetime import datetime

# pip install requests openpyxl

# Função para buscar a previsão do tempo
def buscar_previsao():
    
    api_key = "insira_aqui_sua_chave"  # Substitua pela sua chave API do OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?id=524901&lang=fr&appid={api_key}"
    response = requests.get(url)
    dados = response.json()
    print(dados)
    
    # Verifica se a resposta contém a chave 'main'
    if response.status_code == 200 and 'main' in dados:
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        if umidade < 30:
            status_umidade = "Baixa"
        elif umidade < 60:
            status_umidade = "Normal"
        else:
            status_umidade = "Alta"
        
        # Exibindo na interface gráfica
        label_temperatura.config(text=f"Temperatura: {temperatura}°C")
        label_umidade.config(text=f"Umidade: {umidade}% ({status_umidade})")
    
        adicionar_dados_planilha(temperatura, umidade, status_umidade)
    else:
        label_temperatura.config(text="Erro ao obter dados.")
        label_umidade.config(text="Tente novamente!")

# Função para adicionar os dados na planilha Excel
def adicionar_dados_planilha(temperatura, umidade, status_umidade):
    try:
        wb = openpyxl.load_workbook('previsao_temperatura.xlsx')
        sheet = wb.active
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.append(["Data e Hora", "Temperatura (°C)", "Status da Umidade"])
    
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([data_hora, temperatura, status_umidade])
    wb.save('previsao_temperatura.xlsx')

root = tk.Tk()
root.title("Previsão do Tempo")

largura = 500
altura = 400
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = int((largura_tela - largura) / 2)
pos_y = int((altura_tela - altura) / 2)

root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Botão para buscar a previsão
botao_buscar = tk.Button(root, text="Buscar Previsão", command=buscar_previsao, font=("Arial", 12))
botao_buscar.pack(pady=20)

# Labels para exibir temperatura e umidade
label_temperatura = tk.Label(root, text="Temperatura: - °C", font=("Arial", 16))
label_temperatura.pack(pady=10)

label_umidade = tk.Label(root, text="Umidade: - %", font=("Arial", 16))
label_umidade.pack(pady=10)

root.mainloop()
