#!/usr/bin/env python3
import argparse
import json
import os
from dreame_api import DreameApi

METHODS = [
    "get_map_rooms", "get_rooms", "getRoomList", "get_room_mapping",
    "get_map", "get_current_map", "get_device_map", "get_map_data", "get_map_info",
]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--username", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--country", default="eu")
    p.add_argument("--did", default=None)
    args = p.parse_args()

    token_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dreame_token_cache.json")
    api = DreameApi(args.username, args.password, args.country, token_file=token_file, logger=print)
    api.login()
    device = api.select_device(args.did)
    did = str(device.get("did") or device.get("deviceId") or device.get("id"))
    bind_domain = api.get_bind_domain(device)

    print(json.dumps({"device": device, "did": did, "bindDomain": bind_domain}, indent=2, ensure_ascii=False))

    for method in METHODS:
        print("\n--- send_command {} ---".format(method))
        try:
            result = api.send_command(did, bind_domain, method, {})
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except Exception as exc:
            print("FAILED:", exc)

if __name__ == "__main__":
    main()
