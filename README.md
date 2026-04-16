\# Pipeline de Dados IoT



\## 📌 Descrição

Projeto de pipeline de dados para análise de temperatura de dispositivos IoT.



Os dados são coletados de um arquivo CSV, processados com Python e armazenados em PostgreSQL (Docker). Um dashboard em Streamlit exibe os dados.



\---



\## 🚀 Tecnologias

\- Python

\- Pandas

\- SQLAlchemy

\- PostgreSQL

\- Docker

\- Streamlit

\- Plotly



\---



\## ⚙️ Execução



\### 1. Criar ambiente

python -m venv venv  

venv\\Scripts\\activate  



\### 2. Instalar dependências

pip install pandas psycopg2-binary sqlalchemy streamlit plotly  



\### 3. Rodar pipeline

cd src  

python pipeline.py  



\### 4. Rodar dashboard

streamlit run dashboard.py  



\---



\## 📊 Views



\- Média de temperatura por sala  

\- Leituras por hora  

\- Temperatura máxima e mínima por dia  



\---



\## 📈 Insights



\- Identificação de padrões de temperatura  

\- Monitoramento por horário  

\- Análise por ambiente  

