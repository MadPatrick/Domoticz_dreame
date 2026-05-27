# Domoticz Dreame API Plugin v0.8.0 complete

Dit is een complete schone versie voor jouw Dreame L40 Ultra / `dreame.vacuum.r2492j`.

## Wat zit erin

- Werkende DreameHome backend uit de eerder werkende `v90.5.2`
- Geen Xiaomi
- Geen `python-miio`
- Geen Home Assistant dependency
- Modeldetectie
- Status, batterij, foutmelding, details
- Start / Pause / Dock / Stop / Locate
- Zuigkracht selector
- Waterniveau selector
- Room cache + Room Clean selector
- Tools:
  - `learn_room.py`
  - `test_login.py`
  - `dump_properties.py`
  - `test_fastcommand_probe.py`

## Installatie schoon

```bash
cd /home/patrick/domoticz/plugins
sudo systemctl stop domoticz

mv dreame dreame.backup.$(date +%Y%m%d_%H%M%S)
mkdir dreame
cd dreame
unzip /pad/naar/domoticz_dreame_api_v0_8_0_complete.zip

pip3 install -U requests
sudo systemctl start domoticz
```

## Kamers beheren

Omdat de L40 map/room-data niet via de normale `sendCommand` route komt, gebruikt v0.8.0 een stabiele room cache.

Lijst tonen:

```bash
python3 learn_room.py list
```

Kamer toevoegen:

```bash
python3 learn_room.py add --id 16 --name "Keuken"
python3 learn_room.py add --id 17 --name "Woonkamer"
```

Kamer verwijderen:

```bash
python3 learn_room.py delete --id 16
```

Daarna Domoticz herstarten.  
Als de selector niet vernieuwt omdat jouw Domoticz geen `UpdateOptions()` ondersteunt, verwijder dan eenmalig het device `Dreame Room Clean` in Domoticz en herstart Domoticz.

## Room ID's vinden

De API geeft bij jouw model nog geen rooms terug via de normale route. Mogelijke manieren:

1. Test met:
```bash
python3 test_fastcommand_probe.py --username 'mail' --password 'pass' --country eu
```

2. Gebruik app/log/proxy analyse om segment IDs te vinden.

3. Als je room IDs al kent: voeg ze direct toe met `learn_room.py`.

## Belangrijk

De room-clean payload gebruikt:

```json
[[room_id, 1, 1]]
```

via Dreame `START_CUSTOM`. Dit is de meest waarschijnlijke segment-clean route voor deze modelgeneratie, maar kan per firmware afwijken.


## v0.8.1
- Device names now use the robot name from Dreame Home (example: Truus Status).
