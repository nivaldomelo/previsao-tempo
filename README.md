Documentação do Projeto: Previsão do
Tempo com Tkinter
Descrição
Este projeto é uma aplicação de desktop feita com Python e Tkinter, que permite ao
usuário consultar a previsão do tempo de uma cidade e salvar as informações em uma
planilha Excel. A aplicação utiliza a API do OpenWeatherMap para obter dados de
temperatura e umidade, e armazena esses dados com a data e hora da consulta.
Funcionalidades:
• Consultar a previsão do tempo: Através de um botão, o usuário pode solicitar
a previsão do tempo para a cidade configurada.
• Exibir dados: A temperatura e a umidade do ar são exibidas na interface
gráfica.
• Armazenamento em Excel: A cada consulta, os dados (data e hora,
temperatura, status da umidade) são armazenados em uma planilha Excel.
• Interface gráfica: A aplicação possui uma interface gráfica simples, construída
com Tkinter, que permite ao usuário interagir facilmente com a aplicação.
Tecnologias Utilizadas
• Python: Linguagem de programação principal.
• Tkinter: Biblioteca gráfica para a criação da interface de usuário (UI).
• Requests: Biblioteca para fazer requisições HTTP e obter os dados da API.
• Openpyxl: Biblioteca para manipular e salvar dados em arquivos Excel.
Pré-requisitos
Antes de rodar a aplicação, você precisa instalar as dependências necessárias:
1. 2. Python 3.x instalado. Você pode verificar se o Python está instalado e sua
versão com o comando:
bash
CopiarEditar
python --version
Instalar as bibliotecas necessárias: Execute o seguinte comando para instalar
as dependências:
bash
3. CopiarEditar
pip install requests openpyxl
Obter uma chave da API do OpenWeatherMap:
o Vá até o site do OpenWeatherMap: https://openweathermap.org/
o Crie uma conta e obtenha a sua chave de API.
o Substitua "sua_chave_api_aqui" no código pela chave da API que
você obteve.
Como Usar
1. Configurando o arquivo:
o Abra o código no editor de sua escolha.
o Substitua a variável api_key = "sua_chave_api_aqui" com a chave
da API que você obteve do OpenWeatherMap.
o Caso queira consultar uma cidade diferente, altere a variável cidade =
"São Paulo" para o nome da cidade desejada.
2. Executando a Aplicação:
o Salve o código em um arquivo, por exemplo, app.py.
o Execute o script no terminal ou no editor de sua escolha com o comando:
bash
CopiarEditar
python app.py
o A interface gráfica será aberta.
o Clique no botão "Buscar Previsão" para obter os dados da previsão do
tempo.
3. Exibição dos Dados:
o A temperatura e a umidade do ar da cidade configurada serão exibidas na
interface.
o O status da umidade será classificado como "Baixa", "Normal" ou
"Alta".
o A cada consulta, os dados serão salvos automaticamente na planilha
Excel chamada previsao_temperatura.xlsx.
Estrutura do Projeto
bash
CopiarEditar
previsao_do_tempo/
│
├── app.py └── README.md # Arquivo principal do código ├── previsao_temperatura.xlsx # Planilha que armazena os dados
# Este arquivo de documentação
Explicação do Código
1. Função buscar_previsao()
Esta função faz uma requisição HTTP à API do OpenWeatherMap para obter a previsão
do tempo. Se a requisição for bem-sucedida, ela extrai os dados de temperatura e
umidade, exibe-os na interface gráfica e chama a
função adicionar_dados_planilha() para salvar esses dados.
2. Função adicionar_dados_planilha()
A função verifica se o arquivo Excel já existe. Caso contrário, cria um novo arquivo e
adiciona um cabeçalho com as colunas "Data e Hora", "Temperatura" e "Status da
Umidade". Ela então insere os dados coletados (data/hora, temperatura, status da
umidade) e salva a planilha.
3. Interface Gráfica
A interface gráfica é criada com Tkinter. Ela contém:
• Um botão para buscar a previsão do tempo.
• Dois labels para exibir a temperatura e a umidade.
• A janela da aplicação é centralizada na tela com um tamanho ajustado de
500x400 pixels.
4. Configuração da Janela
A janela é criada com o método geometry(), que define o tamanho da janela e a
posiciona de forma centralizada no meio da tela.
Exemplo de Dados na Planilha
A planilha previsao_temperatura.xlsx será salva com a seguinte estrutura:
Data e Hora Temperatura (°C) Status da Umidade
2025-01-16 14:35:02 30.5 Normal
2025-01-16 15:00:45 29.8 Alta
Considerações Finais
• A aplicação é simples e visa ilustrar como usar APIs externas e salvar dados em
uma planilha Excel.
• A interface gráfica pode ser expandida e melhorada, por exemplo, adicionando
mais informações sobre o clima ou permitindo ao usuário selecionar a cidade.
• Este projeto pode ser a base para criar uma aplicação mais complexa, como um
rastreador de clima para diferentes cidades, com gráficos e relatórios.
