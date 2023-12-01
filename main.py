
import requests
import json


kjennemerke = input(f'TIPS: \nDR85499 er en sivil politibil\nEE69130 er en personbil\nSkriv inn kjennemerke: ')
#kjennemerke = "DR85499" #Sivil politibil
#kjennemerke = "ee69130" #vår bil
base_url = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata?kjennemerke=' + kjennemerke

Header = {
    'SVV-Authorization': 'Apikey {Sett inn din API nøkkel her utenkrøllparantes}',
}

response = requests.get(base_url, headers=Header)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    tilleggsgodkjenninger = data['kjoretoydataListe'][0]['godkjenning']['tilleggsgodkjenninger']

    if len(tilleggsgodkjenninger) > 0:
        kodeNavn = tilleggsgodkjenninger[0]['godkjenningstype']['kodeNavn']
        neringskode = data['kjoretoydataListe'][0]['registrering']['neringskode']
        if kodeNavn == 'Utrykning' and neringskode == '82.110':
            print('Kjøretøyet er godkjent for utrykning, kan være sivil eller militær politi')
        else:
            print('Kjøretøyet er godkjent for utrykning, men ikke politi')
    else:
        print('Kjøretøyet er ikke godkjent for utrykning, vanlig bil')

else:
    print(f"Failed to retrieve data, status code: {response.status_code}")
    print(response.text)


