# DATU_STR_nosleguma_projekts_2025

Izstrādājot projektu Jums ir nepieciešams izveidot README.md datni, kur Jūs (OBLIGĀTI latviešu valodā):

·       detalizēti aprakstīsiet projekta uzdevumu;

·       izskaidrosiet kādas Python bibliotēkas un kāpēc tiek izmantotas projekta izstrādes laikā

·       projekta izstrādes laikā jāizmanto savas definētas datu struktūras

·       aprakstīsies programmatūras izmantošanas metodes

 Eiropas ceļošanas plāns. Projekta uzdevums ir izstrādāt programmu, kas ļaus apskatīt ievadītās Eiropas pilsētas laikapstākļus noteiktajās dienās, kā arī tiek izvadīti apskates objektu dati, balstoties uz norādīto daudzumu.

# Projekta izmantošana:

Ievades daļa

- Ievada Eiropas pilsētu( nav obligāti jābūt galvaspilsētai, bet jārēķinās ar to, ka var neizvadīt daudz apskates objektus).
- Ievada celošanas ilgumu( dienās).
- Ievada vēlamo skaitu ar apskates objektiem.

Izvades daļa

- Izvada laika prognozi izvēlētajam dienu skaitam( sākot no pašreizējā datuma tiks izvadīti dati), kur tabulā tiek izvadīti precīzi datumu, maksimālā, minimālā un vidējā temperatūra, kā arī nokrišņu aprakstu.
- Izvada paziņojumu par apskates objektu meklēšanu.
- Izvada noteiktu skaitu ar apskates objektiem( var izvadīt mazāk nekā vēlamo skaitu, jo nav pietiekami daudz apskates objektu), kur tabulā tiek izvadīta apskates objektu numerācija, to nosaukums, adrese un apskates objektu tips.

# Informācija par Python izmantotajām bibliotēkām
- os- strādā ar operētājsistēmu un dod piekļuvi .env failam, kurā glabā API atslēgu.
- requests- strādā ar HTTP pieprasījumu veikšanu uz ārējā tīmekļa(https://www.inyourpocket.com/continent/europe) un laikapstākļu API(https://www.weatherapi.com/).
- time- strādā ar laika funkciju, šajā gadījumā, lai mājaslapa nemestu kļūdu par pārāk ātru pieprasījumu veikšanu.
- no datetime izmanto datetime- strādā ar datumiem un laikiem, pārvēršot datumu formātu no YYYY-MM-DD uz DD.MM.YYYY.
- no bs4 izmanto BeautifulSoup- strādā ar HTML satura analizēšanu un apstrādi, iegūstot tūrisma vietu nosaukumus, adreses un tipus no ārējā tīmekļa.
- no tabulate izmanto tabulate- strādā ar satu attēlošanu tabulas formātā konsolē, izvadot laika prognozi un apskates objektu vietas.
- no dotenv izmanto load_dotenv- strādā ar API atslēgu iegūšanu no .env faila.

# Projekta definētā datu struktūra
Projekta uzdevuma realizēšanai tiek izmantota HashTable datu struktūra, lai glabātu un organizētu apskates objektu informāciju efektīvā un vienkāršā veidā.


