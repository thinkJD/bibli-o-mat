#!/bin/bash

# Install Docker if not already installed
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    sudo systemctl start docker
    sudo systemctl enable docker
    echo "Docker installed successfully."
else
    echo "Docker already installed."
fi

# Create the systemd service file
sudo tee /etc/systemd/system/bibli-o-mat.service > /dev/null <<EOT
[Unit]
Description=Bibli-o-mat Docker Container

[Service]
Type=oneshot
ExecStart=/usr/bin/docker run --rm -v bibli-o-mat/data:/src/app/data -v bibli-o-mat/logs:/var/log/bibli-o-mat bibli-o-mat-image
ExecStop=/usr/bin/docker stop \$(docker ps -q --filter ancestor=bibli-o-mat-image)
TimeoutStopSec=30
StandardOutput=journal+file:/var/log/bibli-o-mat/%Y-%m-%d_%H-%M-%S.log
StandardError=journal+file:/var/log/bibli-o-mat/%Y-%m-%d_%H-%M-%S.log

[Install]
WantedBy=multi-user.target
EOT

# Reload systemd to pick up the new service file
sudo systemctl daemon-reload

# Create the cron job
(crontab -l ; echo "0 1 * * * systemctl start bibli-o-mat.service") | crontab -

echo "Setup completed successfully."
