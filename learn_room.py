#!/usr/bin/env python3
import argparse
import json
import os
import time

CACHE = "room_cache.json"

def load(path):
    if not os.path.exists(path):
        return {"version": 1, "rooms": []}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        data = {"version": 1, "rooms": data}
    data.setdefault("version", 1)
    data.setdefault("rooms", [])
    return data

def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    try:
        os.chmod(path, 0o600)
    except Exception:
        pass

def main():
    p = argparse.ArgumentParser(description="Manage Dreame room_cache.json")
    p.add_argument("command", choices=["list", "add", "delete", "clear"])
    p.add_argument("--id", type=int)
    p.add_argument("--name")
    p.add_argument("--file", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), CACHE))
    args = p.parse_args()

    data = load(args.file)

    if args.command == "list":
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    if args.command == "clear":
        data["rooms"] = []
        save(args.file, data)
        print("Cleared rooms")
        return

    if args.command == "add":
        if args.id is None or not args.name:
            raise SystemExit("add requires --id and --name")
        rooms = [r for r in data["rooms"] if int(r.get("id")) != args.id]
        rooms.append({"id": args.id, "name": args.name, "source": "manual", "last_seen": int(time.time())})
        data["rooms"] = sorted(rooms, key=lambda r: int(r["id"]))
        save(args.file, data)
        print("Added room {}: {}".format(args.id, args.name))
        return

    if args.command == "delete":
        if args.id is None:
            raise SystemExit("delete requires --id")
        data["rooms"] = [r for r in data["rooms"] if int(r.get("id")) != args.id]
        save(args.file, data)
        print("Deleted room {}".format(args.id))

if __name__ == "__main__":
    main()
