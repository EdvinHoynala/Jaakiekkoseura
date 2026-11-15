# Jääkiekkoseura
* Sovelluksessa käyttäjät pystyvät etsimään peliseuraa jääkiekkoon. Ilmoituksessa lukee missä ja milloin pelivuoro on sekä tarvittava pelaajien määrä, jotta pelivuoro voidaan pitää.
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään ilmoituksia ja muokkaamaan ja poistamaan niitä.
* Käyttäjä näkee sovellukseen lisätyt ilmoitukset.
* Käyttäjä pystyy etsimään ilmoituksia sen perusteella, milloin vuoro on.
* Käyttäjäsivu näyttää, montako ilmoitusta käyttäjä on lähettänyt ja listan ilmoituksista.
* Käyttäjä pystyy valitsemaan esimerkiksi seuraavia luokitteluja:
* Pelipaikka: Metro Areena, Veikkaus Areena, Helsingin jäähalli
* Pelaajan taso: aloittelija, keskitaso tai edistynyt
* Käyttäjä pystyy ilmoittautumaan pelivuoroon. Ilmoituksessa näytetään, ketkä käyttäjät ovat ilmoittautuneet.

# Välipalautus 2:
**Jääkiekkoseuran ilmoitustaulu**
* Web sovellus, jonka avulla jääkiekkoseuran jäsenet voivat julkaista ja selata pelivuoroja, sekä ilmoittaa pelaajien vähimmäismäärän.
## Sovelluksen toiminnot:
- **Käyttäjätunnukset**: Käyttäjä voi luoda uuden tunnuksen ja kirjautua sisään tai ulos sovelluksesta.
- **Ilmoitusten hallinta**: Sisäänkirjautunut käyttäjä voi luoda uusia ilmoituksia, sekä muokata ja poistaa omia ilmoituksiaan.
- **Selaaminen ja hakusanalla etsiminen**: Käyttäjät näkevät kaikki lisätyt ilmoitukset etusivulla. Ilmoituksista voidaan painaa, jolloin nähdään ilmoituksen tarkemmat tiedot. Ilmoituksia voidaan myös etsiä hakusanalla otsikon tai kuvauksen perusteella.
## Sovelluksen käynnistäminen ja testaaminen

1. **Kloonaa repositorio ja siirry projektin kansioon:**
   ```bash
   git clone https://github.com/EdvinHoynala/Jaakiekkoseura
   cd Jaakiekkoseura
   ```

2. **Luo ja aktivoi virtuaaliympäristö sekä asenna Flask:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```

3. **Luo tietokanta (`database.db`) SQL-tiedoston perusteella:**
   ```bash
   sqlite3 database.db < schema.sql
   ```

4. **Käynnistä sovellus:**
   ```bash
   flask run
   ```

5. **Avaa sovellus selaimessa:**
   Siirry osoitteeseen `http://127.0.0.1:5000`, luo uusi käyttäjätunnus ja kirjaudu sisään.

