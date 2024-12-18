# Jarvis 4.0 Installation Guide

## **Manual Rules**
1. Supported for **64-bit only** (not for 32-bit systems).  
2. **Do not delete** any file or folder related to Jarvis after installation.  
3. Install **Python 3.12.0** only. Do not install a newer version.  
4. Follow the specified paths and steps carefully to avoid errors.  
5. For errors or support, contact: **nk1990347@gmail.com**.  

---

## **Installation Steps**

### **1. Download and Extract**
- Download the **Jarvis 4.0 ZIP/7Z** file.  
- Extract it to your **Desktop**.  
- Navigate to the extracted `Jarvis` folder.

### **2. Install Python**
1. Inside the `Jarvis` folder, run `python-3.12.0-amd64.exe`.  
2. During installation, **enable "Add Python to PATH"** (important).  
3. Complete the installation.

### **3. Setup Virtual Environment**
1. Open **Command Prompt (CMD)**.  
2. Navigate to the Desktop:
   ```bash
   cd Desktop
   ```
3. Install `virtualenv`:
   ```bash
   pip install virtualenv
   ```
4. Create a virtual environment:
   ```bash
   python -m virtualenv jarvis
   ```
   Wait for about 1 minute.  

5. Navigate to the `Jarvis` folder:
   ```bash
   cd jarvis
   ```

6. Check the folder structure in File Explorer under the `Jarvis` folder:
   - Ensure the following are created:
     ```
     Include
     Lib
     Scripts
     .gitignore
     pyvenv.cfg
     ```
   - **Note**: If `Include` or `bin` is missing on some systems, don’t worry.  
   - The other 4 files/folders are essential.

---

## **4. Activate Virtual Environment**
1. Run in CMD:
   ```bash
   Scripts\activate
   ```
2. Upgrade pip:
   ```bash
   python.exe -m pip install --upgrade pip
   ```

---

## **5. Install Required Packages**
Copy and paste the following commands into CMD to install all required packages:  
```bash
pip3 install win32gui
pip3 install standerd-aifc
pip3 install pyttsx3
pip3 install SpeechRecognition
pip3 install pywhatkit
pip3 install pygame
pip3 install pyAudio
pip3 install pvporcupine
pip3 install AppOpener
pip3 install pyautogui
pip3 install keyboard
pip3 install volume-control
pip3 install screen_brightness_control
```

**Note**: If `standerd-aifc` fails, use:  
```bash
pip3 install aifc
```

---

## **6. Configure `start.bat`**
1. In the `Jarvis` folder, locate the file `start.bat`.  
2. Copy `start.bat` and navigate to:  
   ```
   C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
   ```
   Paste the file here.  

3. Create a desktop shortcut for `start.bat`:  
   - Right-click on `start.bat` → `Send to` → `Desktop`.  

4. Set `start.bat` to run as administrator:  
   - Right-click the desktop shortcut → `Properties`.  
   - Click `Advanced` and enable **Run as Administrator**.  
   - Click `OK`.

---

## **7. Final Setup**
1. Open the `Name.txt` file in the `Jarvis` folder.  
2. Enter your name and save the file.  

3. Copy the following files:  
   - `Sounds`, `Name.txt`, `jarvis4.0.py`, `JARVIS_SUPPORTER.img`, `SUPPORTER.img`  
4. Navigate to:
   ```
   C:\Users\Public\
   ```
   Paste the files here.

---

## **Personal Suggestion**
Boost your sound with [FxSound](https://github.com/fxsound2/fxsound-app/raw/latest/release/fxsound_setup.exe).  

---

## **Mini Example for `start.bat`**
For reference, the `start.bat` should be placed in:  
```
C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
