import streamlit as st
import numpy as np
import librosa
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib  # Para carregar o LabelEncoder






# Carrega o CSS personalizado
st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)



# Função para carregar o modelo
@st.cache_resource
def load_audio_classification_model():
    model = load_model('models/audio_classification_model_reduced2.h5')
    return model

# Função para carregar o LabelEncoder
@st.cache_resource
def load_label_encoder():
    label_encoder = joblib.load('models/label_encoder2.pkl')  # Carregar o LabelEncoder
    return label_encoder

# Mapeamento de classes para nomes em português (agora um dicionário)
class_names_pt = {

    0:  "Música na Rua", 
    1: "Latido de Cachorro", 
    2: "Crianças Brincando", 
    3: "Tiro",
    4: "Furação", 
    5: "Motor Funcionando",
    6: "Perfuradora",
    7: "Buzina de Carro" , 
    8: "Siren",
    9: "Ar Condicionado"
}

# Função para processar o áudio
def process_audio(file):
    # Lê o arquivo de áudio
    y, sr = librosa.load(file, sr=None)  # Lê o arquivo de áudio em formato de array
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)  # Extrai 40 MFCCs
    mfccs_scaled = np.mean(mfccs.T, axis=0)  # Calcula a média ao longo do tempo
    return mfccs_scaled

# Função para fazer a previsão
def predict(model, audio_features):
    audio_features = audio_features.reshape(1, -1)  # Ajustar formato para entrada do modelo
    prediction = model.predict(audio_features)
    return np.argmax(prediction, axis=1)  # Retorna o índice da classe prevista

# Iniciar a interface Streamlit
def main():
    st.title("Classificador de Áudio")
    st.write("Suba um arquivo de áudio para classificação.")
    
    # Carregar o modelo e o LabelEncoder
    model = load_audio_classification_model()
    label_encoder = load_label_encoder()
    
    # Upload do arquivo de áudio
    audio_file = st.file_uploader("Escolha um arquivo de áudio", type=["wav", "mp3"])
    
    if audio_file is not None:
        # Exibe o áudio
        st.audio(audio_file, format="audio/wav")
        
        # Processar o áudio
        audio_features = process_audio(audio_file)
        
        # Fazer a previsão
        prediction_class = predict(model, audio_features)
        
        # Mapear a classe numérica para o nome da classe em português
        predicted_label = class_names_pt.get(prediction_class[0], "Classe desconhecida")  # Obter o nome da classe
        
        # Exibir o resultado da classificação com mensagem de sucesso
        st.success(f"A classe prevista é: {predicted_label}")  # Exibe o nome da classe

# Rodar a aplicação
if __name__ == "__main__":
    main()
