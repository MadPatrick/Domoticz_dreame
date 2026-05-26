# Domoticz_dreame

Domoticz plugin voor een Dreame robotstofzuiger (lokale aansturing via `python-miio`).

## Setup en installatie

1. **Kopieer de plugin naar Domoticz:** plaats `plugin.py` in `domoticz/plugins/domoticz-dreame-plus/plugin.py`.

2. **Installeer dependency** (in dezelfde Python-omgeving als Domoticz):
    ```bash
    pip3 install python-miio
    ```

3. **Herstart Domoticz**

4. **Voeg hardware toe in Domoticz**
   - Type: `Dreame Plus Vacuum`
   - Address: IP-adres van de robot
   - Port: `54321`
   - Mode1: token
   - Mode2: polling interval (standaard `30`)
   - Mode3: optioneel kamers, bv. `kitchen:1,living_room:2`

## Token ophalen

Na installatie van `python-miio` kun je het token ophalen met:

```bash
miiocli cloud
```

Daarna log je interactief in met je Xiaomi-account en zie je per device o.a.:
- `Token`
- `IP`
- `Model`

Gebruik de gevonden `Token` in Domoticz bij **Mode1**.
