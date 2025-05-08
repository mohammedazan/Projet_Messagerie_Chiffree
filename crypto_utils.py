"""
وحدة التشفير لنظام المراسلة المشفرة
توفر وظائف لتشفير وفك تشفير الرسائل باستخدام AES-GCM
"""

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
from typing import Tuple

def encrypt_message(key: bytes, plaintext: str) -> Tuple[bytes, bytes, bytes]:
    """
    تشفير رسالة باستخدام AES-GCM
    
    يتم إنشاء nonce عشوائي لكل عملية تشفير
    ويتم إرجاع النص المشفر مع nonce و tag للتحقق
    
    Args:
        key (bytes): مفتاح AES-256 (32 بايت)
        plaintext (str): النص المراد تشفيره
        
    Returns:
        Tuple[bytes, bytes, bytes]: (النص المشفر, nonce, tag)
        
    Raises:
        ValueError: إذا كان المفتاح غير صالح
    """
    # إنشاء كائن AESGCM
    aesgcm = AESGCM(key)
    
    # إنشاء nonce عشوائي (12 بايت)
    nonce = os.urandom(12)
    
    # تحويل النص إلى bytes
    plaintext_bytes = plaintext.encode('utf-8')
    
    # تشفير النص
    ciphertext = aesgcm.encrypt(nonce, plaintext_bytes, None)
    
    # استخراج tag (16 بايت الأخيرة)
    tag = ciphertext[-16:]
    ciphertext = ciphertext[:-16]
    
    return ciphertext, nonce, tag

def decrypt_message(key: bytes, ciphertext: bytes, nonce: bytes, tag: bytes) -> str:
    """
    فك تشفير رسالة مشفرة باستخدام AES-GCM
    
    Args:
        key (bytes): مفتاح AES-256 (32 بايت)
        ciphertext (bytes): النص المشفر
        nonce (bytes): القيمة العشوائية المستخدمة في التشفير
        tag (bytes): علامة التحقق من صحة الرسالة
        
    Returns:
        str: النص الأصلي
        
    Raises:
        ValueError: إذا كان المفتاح غير صالح أو إذا كانت الرسالة مزورة
    """
    # إنشاء كائن AESGCM
    aesgcm = AESGCM(key)
    
    # دمج النص المشفر مع tag
    ciphertext_with_tag = ciphertext + tag
    
    # فك تشفير النص
    plaintext_bytes = aesgcm.decrypt(nonce, ciphertext_with_tag, None)
    
    # تحويل النص إلى string
    return plaintext_bytes.decode('utf-8') 