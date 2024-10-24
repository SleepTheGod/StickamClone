# Download This
```bash
git clone https://github.com/SleepTheGod/StickamClone
cd StickamClone
```

# Set Up Your Environment
Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
# Install dependencies
```bash
pip install -r requirements.txt
```
# Initialize the database
```bash
from app import db
db.create_all()
```
# Run the Application
```bash
python run.py
```
