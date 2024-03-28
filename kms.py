import hmac  
import hashlib  
from datetime import datetime


def calculate_password_hmacsha256(shared_key, message):
    try:
        sk = shared_key.encode('utf-8')  
        message_bytes = message.encode('utf-8') 
        
        # Cria um objeto HMAC do tipo SHA256 - hash
        hash_message = hmac.new(sk, message_bytes, hashlib.sha256).digest()

        sbinary = "".join(format(byte, '02x') for byte in hash_message)
        return sbinary
    
    except Exception as e:
        print(f"Erro ao calcular o hash: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    data_atual = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    message = f"user{data_atual}"

    shared_key = "ce6a1d32exemplo"
    result = calculate_password_hmacsha256(shared_key, message)

    if result is not None:
        print(result)
    else:
        print("Erro ao calcular o hash.")
