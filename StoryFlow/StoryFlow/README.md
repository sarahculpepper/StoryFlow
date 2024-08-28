# Project Title

**Insert project description here**

**Change the URLs of the deployed app on Render**

The project is deployed on Render:
[https://django-project-template.onrender.com](https://django-project-template.onrender.com)

To develop the Django application, clone this repository and follow the instructions:

## What's Already Included in the Django Template?

-   User Authentication System:
    -   [Login](https://django-project-template.onrender.com/accounts/login/)
    -   [User Registration](https://django-project-template.onrender.com/accounts/signup/)

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

## Developer's Guide

### Visual Studio Code

It's highly recommended to use [VSCode](https://code.visualstudio.com/) for the development.

The project repository includes VSCode-specific settings ([.vscode/settings.json](.vscode/settings.json))
that are helpful for developing Django applications.

With the python virtual environment active, from the root of the repository,
open the VSCode using the following command:

```bash
code .
```

Please install all the extensions (specified in [.vscode/extensions.json](.vscode/extensions.json))
recommended by VSCode upon opening the project in the code editor.

The [requirements.txt](requirements.txt) file includes the python packages required for some
of the VScode extensions. That's why VSCode needs to be opened from the bash or command
line with an active python virtual environment in which all the project-specific python packages
are installed.

Some fonts to reduce eye strain and provide better coding experience:

-   [FiraCode](https://github.com/tonsky/FiraCode)
-   [Jet Brains Mono](https://github.com/JetBrains/JetBrainsMono)
-   [Hack](https://github.com/source-foundry/Hack)

### GitLab CI/CD pipelines

Before performing a `git push`, run these commands to ensure that the new code changes passes
the pipeline stages:

#### Python linting

**Pipeline Stage**: _lint_

To ensure code changes meet the python coding and documentation standards, run the following
commands:

```bash
pylama .
```

If the above command raises errors, fix the lines specified in the error messages.

#### Django migrations

**Pipeline Stage**: _build_

To ensure Django migration files are created, applied, and added to git, run the following commands:

```bash
python manage.py makemigrations --check
python manage.py migrate --check
```

If the any of the above commands raises an error, create migration files and add to the commit.

#### Django Tests

**Pipeline Stage**: _test_

To ensure code changes passes all unit tests, run the following commands:

```bash
python manage.py test
```

## Team Members

**Update the last name, first name, Render app name, and URLs in the table below **

| Member ID | Role         | Last Name | First Name | Render App           |
| --------- | ------------ | --------- | ---------- | -------------------- |
| A         | Team Lead    | Last Name | First Name | [URL Text](FULL URL) |
| B         | Tech Lead    | Last Name | First Name | [URL Text](FULL URL) |
| C         | Product Lead | Last Name | First Name | [URL Text](FULL URL) |
| D         | Flex Lead    | Last Name | First Name | [URL Text](FULL URL) |

## Install Cypress

Download and install [NodeJS v18 LTS](https://nodejs.org/en/download/).

If the installation is successful, you will be able to run `npm` command from the CMD, bash, or terminal.

Open another CMD prompt, bash, or terminal, navigate to the project's root directory, and run the command:

```bash
npm install cypress
```

This will download the cypress binaries in `node_modules` directory.

It will take several minutes to download and install cypress.


## Run Cypress E2E tests

To execute all the cypress tests, run the following command:
```bash
npx cypress open
```
This command will open a browser window. Select the test as `E2E`.

If there are multiple browsers on your machine, it will prompt to you to choose a browser to run Cypress tests.

Upon choosing a browser to run Cypress tests, click on the `test.cy.js` file to start the tests.


### (optional)
Below command executes all Cypress tests in the terminal (tested in Linux bash):
```bash
npx cypress run --headless
```

## (Optional) Use Docker Containers for Development

See [DOCKER.md](DOCKER.md) file.
