# Set up Development Environment
0. Install python, pip and venv
1. Create virtual environment: ```python -m venv env```
2. Open the virtual env: ```source env/bin/activate```
3. Install all the deps: ```pip install -r requirements.txt```
4. Put your deepl token as an env var in command line (linux): ```export DEEPL_TOKEN="<your_token>"```
5. Translate your text by providing the translate.py script with the path of your file you want to translate. We are currently using deepl service which has 500 k char limit / month. Stef's book is roughly 1200 k chars so one month at a time. After the translation is complete, a file with a -fi -suffix is created in the folder.
6. Profit!