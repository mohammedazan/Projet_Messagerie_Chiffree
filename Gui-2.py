"""
الواجهة الرسومية لنظام المراسلة المشفرة
توفر واجهة مستخدم رسومية باستخدام Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
import base64
import os
from key_manager import generate_key
from crypto_utils import encrypt_message, decrypt_message

class MessagerieApp:
    """التطبيق الرئيسي للواجهة الرسومية"""
    
    def __init__(self, root):
        """تهيئة الواجهة الرسومية
        
        Args:
            root: نافذة Tkinter الرئيسية
        """
        self.root = root
        self.root.title("Système de Messagerie Chiffrée")
        self.root.geometry("400x500")
        
        # إنشاء مجلد الرسائل إذا لم يكن موجودًا
        if not os.path.exists("messages"):
            os.makedirs("messages")
        
        self._create_widgets()
        self._load_message_history()
    
    def _create_widgets(self):
        """إنشاء عناصر الواجهة"""
        # إطار الإدخال
        input_frame = ttk.LabelFrame(self.root, text="Kteb l'message", padding=10)
        input_frame.pack(fill="x", padx=10, pady=5)
        
        # حقل إدخال الرسالة
        self.message_entry = ttk.Entry(input_frame, width=40)
        self.message_entry.pack(fill="x", pady=5)
        
        # إطار الأزرار
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack(fill="x")
        
        # زر الإرسال
        send_button = ttk.Button(
            button_frame,
            text="Chiffrer",
            command=self._send_message
        )
        send_button.pack(side="left", padx=5)
        
        # زر الاستلام
        receive_button = ttk.Button(
            button_frame,
            text="Déchiffrer",
            command=self._receive_message
        )
        receive_button.pack(side="left", padx=5)
        
        # إطار الرسالة المستلمة
        received_frame = ttk.LabelFrame(self.root, text="L'message l'akhir", padding=10)
        received_frame.pack(fill="x", padx=10, pady=5)
        
        self.received_label = ttk.Label(received_frame, text="Ma3ndnach messages")
        self.received_label.pack(fill="x")
        
        # إطار سجل الرسائل
        history_frame = ttk.LabelFrame(self.root, text="L'historique dyal l'messages", padding=10)
        history_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # منطقة النص للسجل
        self.history_text = tk.Text(history_frame, height=10, wrap="word")
        self.history_text.pack(fill="both", expand=True)
        
        # شريط التمرير للسجل
        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.history_text.configure(yscrollcommand=scrollbar.set)
    
    def _load_message_history(self):
        """تحميل سجل الرسائل من الملف"""
        try:
            if os.path.exists("messages/received.txt"):
                with open("messages/received.txt", "r", encoding="utf-8") as f:
                    messages = f.readlines()
                    for message in messages:
                        self.history_text.insert("end", message)
                        self.history_text.see("end")
        except Exception as e:
            messagebox.showerror("Erreur", f"Kan 3ndna mochkil f l'chargement: {str(e)}")
    
    def _send_message(self):
        """إرسال وتشفير رسالة"""
        try:
            # الحصول على النص من حقل الإدخال
            plaintext = self.message_entry.get().strip()
            if not plaintext:
                messagebox.showwarning("Attention", "Kteb chi message 3afak!")
                return
            
            # إنشاء/تحميل المفتاح
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
            
            # مسح حقل الإدخال
            self.message_entry.delete(0, "end")
            
            messagebox.showinfo("Succès", "L'message tchiffra w t7fad b njah!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Kan 3ndna mochkil f l'chiffrement: {str(e)}")
    
    def _receive_message(self):
        """استلام وفك تشفير آخر رسالة"""
        try:
            # التحقق من وجود الملف
            if not os.path.exists("messages/sent.txt"):
                messagebox.showinfo("Info", "Ma3ndnach messages mchiffrin")
                return
            
            # قراءة آخر سطر من الملف
            with open("messages/sent.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    messagebox.showinfo("Info", "Ma3ndnach messages mchiffrin")
                    return
                
                last_line = lines[-1].strip()
            
            # فصل المكونات
            ciphertext_b64, nonce_b64, tag_b64 = last_line.split("|")
            
            # فك ترميز المكونات
            ciphertext = base64.b64decode(ciphertext_b64)
            nonce = base64.b64decode(nonce_b64)
            tag = base64.b64decode(tag_b64)
            
            # إنشاء/تحميل المفتاح
            key = generate_key()
            
            # فك تشفير الرسالة
            plaintext = decrypt_message(key, ciphertext, nonce, tag)
            
            # تحديث التسمية
            self.received_label.configure(text=plaintext)
            
            # حفظ الرسالة المستلمة
            with open("messages/received.txt", "a", encoding="utf-8") as f:
                f.write(f"{plaintext}\n")
            
            # تحديث سجل الرسائل
            self.history_text.insert("end", f"{plaintext}\n")
            self.history_text.see("end")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Kan 3ndna mochkil f l'déchiffrement: {str(e)}")

def main():
    """الدالة الرئيسية"""
    root = tk.Tk()
    app = MessagerieApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 