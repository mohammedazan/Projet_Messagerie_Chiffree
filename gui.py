"""
Interface graphique pour le système de messagerie chiffrée
Simule deux téléphones (A et B) qui peuvent s'envoyer des messages chiffrés
Style inspiré de WhatsApp
"""

import tkinter as tk
from tkinter import ttk, messagebox
import base64
import os
from key_manager import generate_key
from crypto_utils import encrypt_message, decrypt_message

class PhoneFrame(tk.Frame):
    """Frame représentant un téléphone avec sa zone de conversation et ses contrôles"""
    
    def __init__(self, parent, phone_id, other_phone_id):
        """Initialisation d'un téléphone
        
        Args:
            parent: Widget parent Tkinter
            phone_id (str): Identifiant du téléphone ('A' ou 'B')
            other_phone_id (str): Identifiant de l'autre téléphone
        """
        super().__init__(parent, bg='#E4DDD6')
        self.phone_id = phone_id
        self.other_phone_id = other_phone_id
        self.last_received_message = None  # Pour stocker le dernier message reçu
        
        # Création des dossiers et fichiers nécessaires
        if not os.path.exists("messages"):
            os.makedirs("messages")
            
        # Création des fichiers s'ils n'existent pas
        open(f"messages/received_{self.phone_id}.txt", 'a').close()
        open(f"messages/sent_{self.phone_id}.txt", 'a').close()
        
        self._create_widgets()
        self._setup_styles()
        self._load_message_history()
        
    def _create_message_frame(self, text, is_sent=True):
        """Crée un frame pour un message individuel"""
        message_frame = tk.Frame(self.conversation, bg='#E4DDD6')
        
        # Frame pour la bulle de message
        bubble_frame = tk.Frame(
            message_frame,
            bg='#DCF8C6' if is_sent else 'white',
        )
        bubble_frame.pack(
            side='right' if is_sent else 'left',
            pady=5,
            padx=10
        )
        
        # Label pour le texte du message
        message_label = tk.Label(
            bubble_frame,
            text=text,
            wraplength=300,
            justify='left',
            bg=bubble_frame['bg'],
            font=('Segoe UI', 10),
            padx=10,
            pady=5
        )
        message_label.pack()
        
        return message_frame

    def _add_message_to_conversation(self, text, is_sent=True):
        """Ajoute un message à la conversation"""
        self.conversation.configure(state='normal')
        message_frame = self._create_message_frame(text, is_sent)
        self.conversation.window_create('end', window=message_frame)
        self.conversation.insert('end', '\n')
        self.conversation.configure(state='disabled')
        self.conversation.see('end')

    def _load_message_history(self):
        """Charge l'historique des messages"""
        try:
            received_file = f"messages/received_{self.phone_id}.txt"
            if os.path.exists(received_file):
                with open(received_file, "r", encoding="utf-8") as f:
                    messages = f.readlines()
                    for message in messages:
                        self._add_message_to_conversation(message.strip(), False)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement: {str(e)}")

    def _setup_styles(self):
        """Configuration des styles pour l'interface"""
        style = ttk.Style()
        style.configure('Modern.TButton',
                       font=('Segoe UI', 9),
                       padding=5)
        
        self.conversation.configure(
            bg='#E4DDD6',
            padx=10,
            pady=10,
            wrap='word',
            font=('Segoe UI', 10),
            cursor='arrow'
        )
        
        self.message_entry.configure(
            font=('Segoe UI', 10),
            bg='white',
            relief='flat',
            highlightthickness=1,
            highlightcolor='#25D366',
            highlightbackground='#cccccc'
        )

    def _create_widgets(self):
        """Création des widgets du téléphone"""
        main_container = tk.Frame(self, bg='#E4DDD6')
        main_container.pack(fill='both', expand=True)
        
        # Frame pour le chat
        chat_frame = tk.Frame(main_container, bg='#E4DDD6')
        chat_frame.pack(fill='both', expand=True)
        
        # Barre de titre
        header_frame = tk.Frame(chat_frame, bg='#075E54', height=40)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        contact_name = tk.Label(
            header_frame,
            text=f"Phone {self.phone_id}",
            font=('Segoe UI', 12, 'bold'),
            bg='#075E54',
            fg='white'
        )
        contact_name.pack(side='left', padx=10, pady=5)
        
        # Zone de conversation
        self.conversation = tk.Text(
            chat_frame,
            height=15,  # Réduit la hauteur pour faire de la place pour la zone de fichier
            wrap='word',
            state='disabled',
            cursor='arrow',
            bg='#E4DDD6',
            relief='flat'
        )
        self.conversation.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Zone de saisie
        input_frame = tk.Frame(chat_frame, bg='#f0f0f0', height=50)
        input_frame.pack(fill='x')
        input_frame.pack_propagate(False)
        
        self.message_entry = tk.Entry(input_frame)
        self.message_entry.pack(
            side='left',
            fill='x',
            expand=True,
            padx=(10, 5),
            pady=10
        )
        
        self.message_entry.bind('<Return>', lambda e: self._send_message())
        
        ttk.Button(
            input_frame,
            text="Envoyer",
            style='Modern.TButton',
            command=self._send_message
        ).pack(side='right', padx=(0, 10), pady=10)
        
        ttk.Button(
            input_frame,
            text="Recevoir",
            style='Modern.TButton',
            command=self._receive_message
        ).pack(side='right', padx=5, pady=10)
        
        # Séparateur
        ttk.Separator(main_container, orient='horizontal').pack(fill='x', pady=10)
        
        # Frame pour l'affichage du fichier
        file_frame = tk.Frame(main_container, bg='white', height=200)
        file_frame.pack(fill='x', padx=5, pady=5)
        
        # Label pour le nom du fichier
        tk.Label(
            file_frame,
            text=f"sent_{self.phone_id}.txt",
            font=('Consolas', 10),
            bg='white',
            anchor='w'
        ).pack(fill='x', padx=5, pady=2)
        
        # Zone de texte pour le contenu du fichier
        self.file_content = tk.Text(
            file_frame,
            height=8,
            wrap='none',
            font=('Consolas', 9),
            bg='white'
        )
        self.file_content.pack(fill='both', expand=True, padx=5, pady=2)
        
        # Scrollbar horizontale pour le contenu du fichier
        h_scrollbar = ttk.Scrollbar(file_frame, orient='horizontal', command=self.file_content.xview)
        h_scrollbar.pack(fill='x')
        self.file_content.configure(xscrollcommand=h_scrollbar.set)
        
        # Mettre à jour le contenu du fichier
        self._update_file_content()
        
    def _update_file_content(self):
        """Met à jour l'affichage du contenu du fichier sent_X.txt"""
        try:
            self.file_content.delete('1.0', tk.END)
            if os.path.exists(f"messages/sent_{self.phone_id}.txt"):
                with open(f"messages/sent_{self.phone_id}.txt", 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.file_content.insert('1.0', content)
        except Exception as e:
            self.file_content.insert('1.0', f"Erreur de lecture: {str(e)}")
        
        # Programmer la prochaine mise à jour
        self.after(1000, self._update_file_content)

    def _send_message(self):
        """Chiffre et envoie un message"""
        try:
            plaintext = self.message_entry.get().strip()
            if not plaintext:
                return
            
            # Chiffrement
            key = generate_key()
            ciphertext, nonce, tag = encrypt_message(key, plaintext)
            
            # Encodage base64
            ciphertext_b64 = base64.b64encode(ciphertext).decode()
            nonce_b64 = base64.b64encode(nonce).decode()
            tag_b64 = base64.b64encode(tag).decode()
            
            # Créer le message chiffré
            encrypted_message = f"{ciphertext_b64}|{nonce_b64}|{tag_b64}\n"
            
            # Sauvegarde du message chiffré
            with open(f"messages/sent_{self.phone_id}.txt", "a", encoding="utf-8") as f:
                f.write(encrypted_message)
            
            # Mise à jour de l'interface
            self.message_entry.delete(0, "end")
            self._add_message_to_conversation(plaintext, True)
            
            # Réinitialiser le dernier message reçu pour l'autre téléphone via l'application principale
            app = self.master.master  # Accéder à l'instance MessagerieApp
            if isinstance(app, MessagerieApp):
                other_phone = app.phone_a if self.phone_id == "B" else app.phone_b
                if other_phone:
                    other_phone.last_received_message = None
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chiffrement: {str(e)}")
    
    def _receive_message(self):
        """Reçoit et déchiffre le dernier message"""
        try:
            sent_file = f"messages/sent_{self.other_phone_id}.txt"
            if not os.path.exists(sent_file):
                return
            
            with open(sent_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    return
                
                last_line = lines[-1].strip()
                
                # Vérifier si c'est le même message que le dernier reçu
                if last_line == self.last_received_message:
                    return  # Ne rien faire si c'est le même message
                
                # Mettre à jour le dernier message reçu
                self.last_received_message = last_line
            
            # Décodage des composants
            ciphertext_b64, nonce_b64, tag_b64 = last_line.split("|")
            ciphertext = base64.b64decode(ciphertext_b64)
            nonce = base64.b64decode(nonce_b64)
            tag = base64.b64decode(tag_b64)
            
            # Déchiffrement
            key = generate_key()
            plaintext = decrypt_message(key, ciphertext, nonce, tag)
            
            # Sauvegarde du message déchiffré
            with open(f"messages/received_{self.phone_id}.txt", "a", encoding="utf-8") as f:
                f.write(f"{plaintext}\n")
            
            # Mise à jour de l'interface
            self._add_message_to_conversation(plaintext, False)
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du déchiffrement: {str(e)}")

class MessagerieApp:
    """Application principale de messagerie"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsSecure - Messagerie Chiffrée")
        self.root.geometry("1200x800")  # Augmenté la hauteur pour accommoder la zone de fichier
        self.root.configure(bg='#f0f0f0')
        
        self._create_widgets()
        
    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill="both", expand=True)
        
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Phone A (à gauche)
        self.phone_a = PhoneFrame(main_frame, "A", "B")
        self.phone_a.grid(row=0, column=0, padx=10, sticky="nsew")
        
        # Séparateur vertical
        ttk.Separator(main_frame, orient="vertical").grid(row=0, column=1, sticky="ns", padx=20)
        
        # Phone B (à droite)
        self.phone_b = PhoneFrame(main_frame, "B", "A")
        self.phone_b.grid(row=0, column=2, padx=10, sticky="nsew")

def main():
    root = tk.Tk()
    app = MessagerieApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 