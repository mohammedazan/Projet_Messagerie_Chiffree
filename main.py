"""
الواجهة الرئيسية لنظام المراسلة المشفرة
توفر واجهة سطر الأوامر للتفاعل مع النظام
"""

import os
import base64
from key_manager import generate_key
from crypto_utils import encrypt_message, decrypt_message

def create_messages_directory():
    """إنشاء مجلد الرسائل إذا لم يكن موجودًا"""
    if not os.path.exists("messages"):
        os.makedirs("messages")

def menu():
    """عرض القائمة الرئيسية"""
    print("\n=== Système de Messagerie Chiffrée ===")
    print("1) Créer une clé AES")
    print("2) Chiffrer un message")
    print("3) Déchiffrer un message")
    print("4) Quitter")
    return input("Chno bghiti dir? ")

def send_message():
    """تشفير وحفظ رسالة"""
    try:
        # طلب النص من المستخدم
        plaintext = input("\nKteb l'message li bghiti tchiffri: ")
        
        # إنشاء المفتاح إذا لم يكن موجودًا
        key = generate_key()
        
        # تشفير الرسالة
        ciphertext, nonce, tag = encrypt_message(key, plaintext)
        
        # ترميز المكونات باستخدام base64
        ciphertext_b64 = base64.b64encode(ciphertext).decode()
        nonce_b64 = base64.b64encode(nonce).decode()
        tag_b64 = base64.b64encode(tag).decode()
        
        # حفظ الرسالة المشفرة
        with open("messages/sent.txt", "a", encoding="utf-8") as f:
            f.write(f"{ciphertext_b64}|{nonce_b64}|{tag_b64}\n")
        
        print("L'message tchiffra w t7fad b njah!")
        
    except Exception as e:
        print(f"Kan 3ndna mochkil f l'chiffrement: {str(e)}")

def receive_message():
    """قراءة وفك تشفير آخر رسالة"""
    try:
        # التحقق من وجود الملف
        if not os.path.exists("messages/sent.txt"):
            print("Ma3ndnach messages mchiffrin.")
            return
        
        # قراءة آخر سطر من الملف
        with open("messages/sent.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("Ma3ndnach messages mchiffrin.")
                return
            
            last_line = lines[-1].strip()
        
        # فصل المكونات
        ciphertext_b64, nonce_b64, tag_b64 = last_line.split("|")
        
        # فك ترميز المكونات
        ciphertext = base64.b64decode(ciphertext_b64)
        nonce = base64.b64decode(nonce_b64)
        tag = base64.b64decode(tag_b64)
        
        # إنشاء المفتاح
        key = generate_key()
        
        # فك تشفير الرسالة
        plaintext = decrypt_message(key, ciphertext, nonce, tag)
        
        # حفظ الرسالة المستلمة
        with open("messages/received.txt", "a", encoding="utf-8") as f:
            f.write(f"{plaintext}\n")
        
        print(f"\nL'message l'asli: {plaintext}")
        
    except Exception as e:
        print(f"Kan 3ndna mochkil f l'déchiffrement: {str(e)}")

def main():
    """الدالة الرئيسية"""
    create_messages_directory()
    
    while True:
        choice = menu()
        
        if choice == "1":
            key = generate_key()
            print(f"\nL'clé tcrét b njah!")
            
        elif choice == "2":
            send_message()
            
        elif choice == "3":
            receive_message()
            
        elif choice == "4":
            print("\nMerhba bik tani!")
            break
            
        else:
            print("\nHad l'choix machi mzyan. Jreb tani.")

if __name__ == "__main__":
    main() 