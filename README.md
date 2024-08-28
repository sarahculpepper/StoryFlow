# StoryFlow

**StoryFlow** is an advanced, all-in-one broadcast news story planner inspired by the Nexstar Daybook. It is designed to streamline and enhance the way newsrooms operate, providing a robust toolset for managing news production workflows, content sharing, and team collaboration.

# About the Project

**StoryFlow** is a senior computer science project developed at the University of Louisiana at Lafayette. The project reflects the culmination of extensive study and hands-on experience in software development, with a focus on addressing real-world challenges faced by modern newsrooms.

# Key Features

- **Latakoo & Bitcentral Integration:** Seamlessly integrates with Latakoo's Flight, HUB, and Manifest products, as well as Bitcentral's video management system, allowing for efficient video transfer, automation, and collaboration.

- **Enhanced Security:** StoryFlow is built with security in mind, utilizing HTTPS to ensure secure communication and data protection.

- **AI Video Transcription:** Automatically transcribes video content using advanced AI, saving time and improving accessibility for your newsroom.

- **Supers Field:** Easily manage lower-third graphics and supers directly within the planner.

- **Direct Downloads:** Download video files straight to your machine without needing to transfer through Latakoo, simplifying the workflow.

- **WordPress Integration:** Integrates with WordPress, allowing users to view and manage web pages directly in a new tab within the StoryFlow interface.

- **Improved Organization:** Features a better organization system, making it easier to manage and track stories, scripts, and media assets.

- **News Unit Tracking:** Includes an option to track news units, ensuring all resources are accounted for and efficiently deployed.

- **Car Maintenance Section:** A dedicated section for managing the maintenance needs of your newsroom vehicles, keeping your fleet in top condition.

**StoryFlow** is the next generation of newsroom management, providing everything you need to run a smooth, efficient, and secure broadcast operation. Whether you're coordinating content across multiple markets or simply trying to keep your local newsroom organized, StoryFlow is the tool you need.

# Author

Created by Sarah Culpepper. 

**GitHub:** [@sarahculpepper](https://github.com/sarahculpepper) \
**LinkedIn:** [@sarahcpepper](https://linkedin.com/in/sarahcpepper) \
**Email:** sarah.culpepper2022@gmail.com

## Create Python Virtual Environment

```bash
virtualenv --python=/usr/bin/python3 .venv  # for UNIX and MacOS bash/zsh
```

```bash
python -m virtualenv .venv                  # for Windows git bash and Windows CMD
```

## Activate Python Virtual Environment

```bash
source .venv/bin/activate                   # for UNIX and MacOS bash/zsh
```

```bash
source .venv/Scripts/activate               # for Windows git bash
```

```cmd
.venv\Scripts\activate.bat                  # for Windows CMD
```

For the following steps and for development, keep the virtual environment activated all the time.

## Install Python Requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Collect Static Files

```bash
python manage.py collectstatic --no-input
```

## Run the Django Web Server

```bash
python manage.py runserver
```
