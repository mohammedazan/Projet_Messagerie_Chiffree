# 🔐 Mini-Projet : Système de Messagerie Chiffrée

> 🗓️ **Date de création** : 21/04/2025  
> 👨‍💻 **Langage** : Python 3.x  
> 🎯 **Objectif** : Apprentissage des concepts fondamentaux de la cryptographie à travers un projet simple et utile.

---

## 🌟 Présentation du projet

Ce mini-projet consiste à créer un **système de messagerie sécurisé** permettant à deux utilisateurs d'échanger des messages **chiffrés avec AES**.  
Nous utilisons l'algorithme **AES-GCM**, reconnu pour sa **sécurité**, sa **rapidité** et sa **fiabilité**.

---

## 📥 Installation

1. Clonez le dépôt :
```bash
git clone [URL_DU_REPO]
cd messagerie_chiffree
```

2. Installez les dépendances :
```bash
pip install cryptography
```

---

## 🚀 Utilisation

### Interface en ligne de commande (CLI)
```bash
python main.py
```

Exemple de session CLI :
```
=== Système de Messagerie Chiffrée ===
1) Créer une clé AES
2) Chiffrer un message
3) Déchiffrer un message
4) Quitter

Chno bghiti dir? 2
Kteb l'message li bghiti tchiffri: مرحبا بكم!
L'message tchiffra w t7fad b njah!
```

### Interface graphique (GUI)
```bash
python gui.py
```

L'interface graphique offre :
- 📝 Champ de saisie pour les messages
- 📤 Bouton d'envoi pour chiffrer
- 📥 Bouton de réception pour déchiffrer
- 📋 Historique des messages

---

## 🧱 Fonctionnalités principales

✅ Génération automatique d'une clé de chiffrement sécurisée  
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
| 1️⃣ | Étude de l'AES et génération de la clé |
| 2️⃣ | Implémentation du chiffrement/déchiffrement |
| 3️⃣ | Système de messagerie en CLI |
| 4️⃣ | Intégration de l'interface Tkinter |
| 5️⃣ | Tests, documentation et finalisation du projet |

---

## 🔑 Gestion des clés

Une clé AES (256 bits) est générée automatiquement et stockée localement dans un fichier `.key`. Cette clé est **essentielle** pour chiffrer et déchiffrer les messages. Elle doit rester **confidentielle**.

---

## 🎨 Interface graphique (optionnelle)

L'interface sera développée avec **Tkinter** pour une expérience utilisateur plus agréable :  
🖼️ Fenêtre intuitive → 📤 Champ de saisie → 📨 Zone d'affichage des messages chiffrés/déchiffrés

---

## 📂 Arborescence prévue du projet

```
messagerie_chiffree/
├── main.py
├── crypto_utils.py
├── key_manager.py
├── gui.py
├── tests/
│   └── test_crypto.py
├── messages/
│   ├── sent.txt
│   └── received.txt
├── secret.key
└── README.md
```

## 🧪 Tests

Exécutez les tests unitaires :
```bash
python -m unittest tests/test_crypto.py
```

Les tests vérifient :
- ✅ Génération correcte de la clé AES
- ✅ Chiffrement et déchiffrement des messages
- ✅ Intégrité des données

---

## 👥 Auteurs

- 👨 Mohamed Azzan  
- 🤝 Collaborateurs : [Nom de votre coéquipier à insérer]

---

## ❤️ Remerciements

Un grand merci à notre professeure pour son encadrement et ses conseils précieux.  
Ce projet nous permet de plonger dans l'univers passionnant de la **cybersécurité**.

---

## 🚀 Let's Encrypt the World!
