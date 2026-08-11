import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)
    return  encoded_bytes

def decrypt_pass(password):
    decoded_bytes = base64.b64decode(password)
    decoded_data = decoded_bytes.decode()
    print(decoded_data)

user_pass = input("Enter your password: ")
encoded_pass = encrypt_pass(user_pass)
decrypt_pass(encoded_pass)


