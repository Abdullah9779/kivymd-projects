# 💬 BlinkChat – Real-Time Chat App with KivyMD & Firebase

**BlinkChat** is a real-time chat application built using **Python**, **KivyMD**, and **Firebase Realtime Database**. It allows two users to send and receive messages instantly in a beautifully designed mobile-style interface.

---

## 🛠️ Tech Stack

- **Frontend:** KivyMD (Material Design for Kivy)
- **Backend:** Firebase Realtime Database
- **Language:** Python

---

## 🚀 Features

- 🔐 User authentication with Firebase
- 💬 Real-time one-on-one chat
- 📱 Stylish KivyMD interface
- 🕒 Message timestamps
- ✅ Status
- ⚡ Fast and lightweight
- and more

---

## Firebase Realtime Database Rules
In Firebase Console → Realtime Database → Rules, paste:

```JSON
{
  "rules": {
    "messages": {
      ".read": "auth != null",
      ".write": "auth != null"
    },
    "users": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
}

```

## Firebase Setup: 

- Update the Firebase **config** object in your **functions.py** in line no 8 with your Firebase project details.


