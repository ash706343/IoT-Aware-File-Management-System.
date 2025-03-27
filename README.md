# IoT-Aware File Management System
A cloud-based file management system designed for IoT devices and users.  

__________________________________________________________________________________________________________________________
📖 Project Overview
The IoT-Aware File Management System allows users and IoT devices to upload, store, and manage files efficiently. The system includes:
✅ A web-based interface for users to upload files.
✅ A REST API for IoT devices to upload files automatically.
✅ A secure storage system for managing files.
_____________________________________________________________________________________________________________________

🎯 Goals:
Provide a centralized cloud-based file management system.

Allow IoT devices to send data efficiently.

Enable users to access and manage uploaded files easily.

_______________________________________________________________________________________________________________________

🛠️ Features & Functionalities   

1️⃣ Frontend (Web Interface)
✔️ Users can upload files manually via a web interface.
✔️ Displays upload success/failure messages.

2️⃣ Backend (Flask API)
✔️ Accepts file uploads from users & IoT devices.
✔️ Stores uploaded files securely in a designated directory.
✔️ Provides an API for IoT devices to send data.

3️⃣ IoT Device Integration
✔️ IoT devices can automatically send files using HTTP requests.
✔️ Uses a Python script to upload files at scheduled intervals.
