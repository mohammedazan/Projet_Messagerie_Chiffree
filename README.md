# 🔐 Mini-Projet : Système de Messagerie Chiffrée

> 🗓️ **Date de création** : 21/04/2025  
> 👨‍💻 **Langage** : Python 3.x  
> 🎯 **Objectif** : Apprentissage des concepts fondamentaux de la cryptographie à travers un projet simple et utile.

---

## 🌟 Présentation du projet

Ce mini-projet consiste à créer un **système de messagerie sécurisé** permettant à deux utilisateurs d’échanger des messages **chiffrés avec AES**.  
Nous utilisons l'algorithme **AES-GCM**, reconnu pour sa **sécurité**, sa **rapidité** et sa **fiabilité**.

---

## 🧱 Fonctionnalités principales

✅ Génération automatique d’une clé de chiffrement sécurisée  
✅ Sauvegarde de la clé dans un fichier `.key`  
✅ Chiffrement & déchiffrement des messages texte  
✅ Envoi/réception de messages via la ligne de commande (CLI)  
✅ Interface graphique optionnelle avec **Tkinter**  
✅ Système modulaire pour une meilleure organisation du code

---

## 🛠️ Technologies utilisées

| Outil/Librairie | Utilisation |
|-----------------|-------------|
| 🐍 Python 3      | Langage principal du projet |
| 🔐 Cryptography  | Chiffrement AES-GCM |
| 📁 Tkinter       | Interface graphique (optionnelle) |
| 📄 VS Code       | Environnement de développement |

---

## 📅 Planning du projet

| Semaine | Tâches prévues |
|--------|----------------|
| 1️⃣ | Étude de l’AES et génération de la clé |
| 2️⃣ | Implémentation du chiffrement/déchiffrement |
| 3️⃣ | Système de messagerie en CLI |
| 4️⃣ | Intégration de l’interface Tkinter |
| 5️⃣ | Tests, documentation et finalisation du projet |

---

## 🔑 Gestion des clés

Une clé AES (256 bits) est générée automatiquement et stockée localement dans un fichier `.key`. Cette clé est **essentielle** pour chiffrer et déchiffrer les messages. Elle doit rester **confidentielle**.

---

## 🎨 Interface graphique (optionnelle)

L’interface sera développée avec **Tkinter** pour une expérience utilisateur plus agréable :  
🖼️ Fenêtre intuitive → 📤 Champ de saisie → 📨 Zone d'affichage des messages chiffrés/déchiffrés

---

## 📂 Arborescence prévue du projet

```
messagerie_chiffree/
├── main.py
├── crypto_utils.py
├── key_manager.py
├── gui.py (optionnel)
├── messages/
│   ├── sent.txt
│   └── received.txt
├── secret.key
└── README.md
```

---

## 👥 Auteurs

- 👨 Mohamed Azzan  
- 🤝 Collaborateurs : [Nom de votre coéquipier à insérer]

---

## ❤️ Remerciements

Un grand merci à notre professeure pour son encadrement et ses conseils précieux.  
Ce projet nous permet de plonger dans l’univers passionnant de la **cybersécurité**.

---

## 🚀 Let's Encrypt the World!
