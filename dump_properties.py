#!/usr/bin/env python3
import argparse
import json
import os
from dreame_api import DreameApi

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

    status = api.read_basic_status(did, bind_domain, live=True)
    print(json.dumps({
        "device": device,
        "did": did,
        "bindDomain": bind_domain,
        "status": status,
    }, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
