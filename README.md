## Run this command to create a virtual environment named myfirstproject:
```commandline
python -m venv myfirstproject
```
## Activate Virtual Environment
```commandline
source myfirstproject/bin/activate
```

## Install packages in the virtual environment:
```commandline
pip install -r requirements.txt
```

### Create systemd file
```commandline
[Unit]
Description=SCT Monitoring Tool
After=network.target

[Service]
User=USER_NAME
Group=USER_NAME
WorkingDirectory=/home/rajib/D_drives/app/Python_app/sct_monitoring_tool

# Use full path to venv python
ExecStart=/home/rajib/D_drives/app/Python_app/sct_monitoring_tool/.venv/bin/python3 /home/rajib/D_drives/app/Python_app/sct_monitoring_tool/main.py

# Restart behavior
Restart=always
RestartSec=5

# Environment (optional but recommended)
Environment="PATH=/home/rajib/D_drives/app/Python_app/sct_monitoring_tool/.venv/bin"

# Logging
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```