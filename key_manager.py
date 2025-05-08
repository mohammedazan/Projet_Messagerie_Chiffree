"""
وحدة إدارة المفاتيح لنظام المراسلة المشفرة
تدير إنشاء وتحميل مفتاح AES-256 لتشفير الرسائل
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import keywrap
from cryptography.hazmat.backends import default_backend
import os
import base64

KEY_FILE = "secret.key"

def generate_key():
    """
    إنشاء مفتاح AES-256 جديد (32 بايت) وحفظه في ملف
    
    يتم إنشاء المفتاح بطريقة آمنة باستخدام os.urandom()
    إذا كان الملف موجودًا بالفعل، تقوم الدالة بإرجاع المفتاح الموجود
    
    Returns:
        bytes: المفتاح المُنشأ
    """
    if os.path.exists(KEY_FILE):
        print(f"L'fichier {KEY_FILE} kayn déja? Ghir n'utilisawh!")
        return load_key()
    
    # إنشاء مفتاح AES-256 (32 بايت)
    key = os.urandom(32)
    
    # تشفير المفتاح بتنسيق base64 للتخزين
    key_b64 = base64.b64encode(key)
    
    # حفظ المفتاح في الملف
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key_b64)
    
    print(f"Clé jdida créée f {KEY_FILE}")
    return key

def load_key():
    """
    تحميل مفتاح AES من الملف
    
    Returns:
        bytes: المفتاح المُحمّل
        
    Raises:
        FileNotFoundError: إذا لم يكن ملف المفتاح موجودًا
        ValueError: إذا لم يمكن فك تشفير المفتاح بشكل صحيح
    """
    try:
        with open(KEY_FILE, "rb") as key_file:
            key_b64 = key_file.read()
            
        # فك تشفير المفتاح من base64
        key = base64.b64decode(key_b64)
        
        # التحقق من حجم المفتاح
        if len(key) != 32:
            raise ValueError("L'clé li charjna 3ndha 32 bytes bach tkhdem mzyan!")
            
        return key
        
    except FileNotFoundError:
        raise FileNotFoundError(f"L'fichier {KEY_FILE} makaynch! Khassna n'crééw l'clé l'awal.")
    except Exception as e:
        raise ValueError(f"Chno 3ndna f l'chargement dyal l'clé: {str(e)}")

# اختبار الوظائف إذا تم تشغيل الملف مباشرة
if __name__ == "__main__":
    print("Test dyal l'clés - Test des clés")
    print("-" * 30)
    
    # إنشاء مفتاح جديد
    print("1. Ghadi n'crééw l'clé...")
    key = generate_key()
    print(f"   L'clé li créina (10 premiers bytes): {key[:10].hex()}")
    
    # تحميل المفتاح
    print("\n2. Ghadi n'chargéw l'clé...")
    loaded_key = load_key()
    print(f"   L'clé li charjna (10 premiers bytes): {loaded_key[:10].hex()}")
    
    # التحقق من تطابق المفاتيح
    print("\n3. Ghadi n'testéw...")
    if key == loaded_key:
        print("   ✅ L'clés kif kif! Kolchi mzyan!")
    else:
        print("   ❌ L'clés machi kif kif! 3ndna mochkil!") 