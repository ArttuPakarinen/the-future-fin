# Miten osallistua käännöstalkoisiin
0. Asenna git ja opettele sen peruskomennot (clone, branch, checkout, add, push, pull, commit ja merge).
1. Luo ilmainen github-tili.
2. Ota yhteyettä repon omistajaan ja pyydä tältä oikeuksia
3. Kloonaa projekti omalle koneellesi ja luo branch, jonka nimeät kääntämiesi kappaleiden mukaan, esim. chapter-12.
4. Konekäännetty data löytyy data-kansosta. Kirja on jaettu kolmeen tiedostoon, kappaleet 1-20, 21-37 ja 38-46. Konekäännetyillä tiedostoilla on fi-pääte. Toistaiseksi (04/2023) vain ensimmäinen osa on käännetty. Tätä osaa päivitetään sitä mukaa kun deepl:n kiintiötä tulee lisää ja seuraavat osat saadaan (kone)käännettyä.
 käänätäminen käy yksinkertaisesti muuttamalla fi-loppuisen tiedoston sisältöä. Jotta saisist tämän integroitua helposti gitin käyttämiseen, kannattaa kääntää yksi sivu kerrallaan ja pushata muutokset gittiin heti kun sivu on valmis. Tällöin git-historia pysyy helposti luettavana. 
 5. Kun olet saanut kappaleesi käännettyä, puske loputkin muutokset gittiin ja tee branchistasi merge-request main-branchiin. Valitse työllesi tarkastaja. Kun olet saanut tarkastajan korjausehdotukset käsiteltyä mergetä branchisi mainiin.

# Set up Development Environment (for those who need deepl)
0. Install python, pip and venv
1. Create virtual environment: ```python -m venv env```
2. Open the virtual env: ```source env/bin/activate```
3. Install all the deps: ```pip install -r requirements.txt```
4. Put your deepl token as an env var in command line (linux): ```export DEEPL_TOKEN="<your_token>"```
5. Translate your text by providing the translate.py script with the path of your file you want to translate. We are currently using deepl service which has 500 k char limit / month. Stef's book is roughly 1200 k chars so one month at a time. After the translation is complete, a file with a _fi -suffix is created in the folder.
