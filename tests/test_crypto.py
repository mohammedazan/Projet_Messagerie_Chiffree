"""
اختبارات الوحدات لنظام المراسلة المشفرة
تختبر وظائف التشفير وفك التشفير
"""

import unittest
import os
from key_manager import generate_key
from crypto_utils import encrypt_message, decrypt_message

class TestCrypto(unittest.TestCase):
    """فئة اختبار وظائف التشفير"""
    
    def setUp(self):
        """إعداد بيئة الاختبار"""
        # حذف ملف المفتاح إذا كان موجودًا
        if os.path.exists("secret.key"):
            os.remove("secret.key")
    
    def tearDown(self):
        """تنظيف بعد الاختبار"""
        # حذف ملف المفتاح بعد الاختبار
        if os.path.exists("secret.key"):
            os.remove("secret.key")
    
    def test_generate_key(self):
        """اختبار إنشاء المفتاح"""
        # إنشاء مفتاح جديد
        key = generate_key()
        
        # التحقق من نوع المفتاح
        self.assertIsInstance(key, bytes, "L'clé khassha tkun men type bytes")
        
        # التحقق من طول المفتاح
        self.assertEqual(len(key), 32, "L'clé khassha tkun 32 bytes")
    
    def test_encrypt_decrypt(self):
        """اختبار التشفير وفك التشفير"""
        # نص للاختبار
        original_text = "مرحبًا بكم في نظام المراسلة المشفرة!"
        
        # إنشاء مفتاح
        key = generate_key()
        
        # تشفير النص
        ciphertext, nonce, tag = encrypt_message(key, original_text)
        
        # التحقق من نوع المكونات
        self.assertIsInstance(ciphertext, bytes, "L'message mchiffré khass ykun men type bytes")
        self.assertIsInstance(nonce, bytes, "Nonce khass ykun men type bytes")
        self.assertIsInstance(tag, bytes, "Tag khass ykun men type bytes")
        
        # التحقق من طول nonce
        self.assertEqual(len(nonce), 12, "Nonce khass ykun 12 bytes")
        
        # فك تشفير النص
        decrypted_text = decrypt_message(key, ciphertext, nonce, tag)
        
        # التحقق من تطابق النص الأصلي
        self.assertEqual(decrypted_text, original_text, 
                        "L'message li jbna khass ykun kif kif bach n3rfo belli kolchi mzyan!")

if __name__ == '__main__':
    unittest.main() 