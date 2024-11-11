# 🎧 **IA para Análise de Áudio** 🤖

Este projeto utiliza **Deep Learning** para a classificação de diferentes tipos de sons (como buzinas de carro, cães latindo, sirenes, etc.) com base nas características extraídas de arquivos de áudio. Utilizamos o framework **TensorFlow** para treinar o modelo e a biblioteca **Librosa** para extração de características acústicas, com uma interface simples construída com **Streamlit**. 💡

## 🚀 **Como rodar o projeto**

### 📦 **Pré-requisitos**

Antes de começar, verifique se você possui o seguinte instalado no seu computador:

- **Python 3.x** (preferencialmente 3.10 ou superior) 🐍
- **TensorFlow** (usado para o modelo de deep learning) 🤖
- **Librosa** (para a extração de características de áudio) 🎶
- **Streamlit** (para a interface de usuário) 🖥️
- **joblib** (para carregar o LabelEncoder) 📦

### 💻 **Passo a passo para rodar no seu sistema**

#### Para **Mac** 🍏 / **Linux** 🐧 / **Windows** 💻:

1. **Clone o repositório**:
   Abra seu terminal (ou prompt de comando) e clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/thaleson/IA_audio_analysis.git
   cd IA_audio_analysis
   ```

2. **Crie e ative um ambiente virtual**:
   Para garantir que todas as dependências sejam instaladas corretamente, é recomendado criar um ambiente virtual.

   - **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Instale as dependências**:
   Instale as bibliotecas necessárias com o **pip**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Baixe os arquivos de modelo e encoder**:
   Certifique-se de que os arquivos do modelo (`audio_classification_model_reduced2.h5`) e do encoder (`label_encoder2.pkl`) estejam na pasta do projeto. Você pode precisar baixar esses arquivos separadamente, caso não os tenha.

5. **Execute a aplicação Streamlit**:
   Após garantir que tudo esteja instalado corretamente, você pode rodar a aplicação com o seguinte comando:

   ```bash
   streamlit run app.py
   ```

6. **Acesse o aplicativo**:
   O Streamlit irá abrir uma interface na web onde você poderá fazer o upload de arquivos de áudio para classificar. 🎤

### 🎶 **Como utilizar a aplicação**

1. **Faça o upload de um arquivo de áudio**: 
   Clique no botão de upload de áudio e escolha um arquivo no formato **wav** ou **mp3**.

2. **Veja o resultado da classificação**:
   Após o upload, a IA processará o áudio e mostrará o tipo de som que foi classificado. 🎧

3. **Resultado em português**: 
   A classe do áudio será exibida em português para você! 📊

---

## 🔧 **Tecnologias utilizadas**

- **TensorFlow**: Para a criação e treinamento do modelo de Deep Learning 🧠
- **Librosa**: Para a extração de características acústicas dos arquivos de áudio 🎶
- **Streamlit**: Para a construção de uma interface web interativa 🌐
- **joblib**: Para salvar e carregar o modelo do **LabelEncoder** 💾

---

## 🚨 **Limitações do modelo**

⚠️ **O modelo não é perfeito**. Ele pode cometer erros, principalmente em situações com ruídos ou sons que não estão nos dados de treinamento. No entanto, ele consegue classificar com uma boa precisão os tipos de sons mais comuns. 📉

---

## 📈 **Melhorias futuras**

💭 Estou sempre em busca de melhorias! Algumas possíveis evoluções para este projeto incluem:

- Melhorar a precisão do modelo com mais dados de treinamento 🏋️‍♂️
- Adicionar novas funcionalidades, como a classificação de novos tipos de áudio 🎤
- Explorar o uso de **NLP** para análise e extração de informações a partir de áudios transcritos 📝

---

## 📂 **Estrutura do repositório**

```plaintext
IA_audio_analysis/
│
├── app.py                  # Arquivo principal da aplicação Streamlit
├── audio_classification_model_reduced2.h5  # Modelo de deep learning treinado
├── label_encoder2.pkl      # LabelEncoder para mapear classes para os nomes em português
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo! 😉
```

---

## 📣 **Contribuindo para o projeto**

Se você tem alguma sugestão de melhoria, correção de bugs ou deseja contribuir de alguma forma, fique à vontade para abrir um **Pull Request** ou uma **Issue**! 📬




