import requests, time

def sui_vanish():
    print("Sui — Mystic Whale Vanish (> 100M SUI moved with Move privacy)")
    seen = set()
    while True:
        r = requests.get("https://suiscan.xyz/mainnet/api/transactions?limit=40")
        for tx in r.json().get("data", []):
            h = tx["txDigest"]
            if h in seen: continue
            seen.add(h)

            # Look for massive coin merges or private transfers
            amount = 0
            for obj in tx.get("balanceChanges", []):
                if obj.get("coinType") == "0x2::sui::SUI":
                    amount += abs(int(obj["amount"]))

            if amount >= 100_000_000_000_000_000:  # > 100M SUI (9 decimals)
                print(f"MYSTIC WHALE VANISHED\n"
                      f"{amount/1e9:,.0f} SUI moved in one Move call\n"
                      f"Sender: {tx['sender'][:12]}...\n"
                      f"Tx: https://suiscan.xyz/mainnet/tx/{h}\n"
                      f"→ Sui's object model just swallowed a fortune\n"
                      f"→ Could be private transfer, zkLogin, or deep liquidity move\n"
                      f"→ The chain saw it. The world didn't.\n"
                      f"{'-'*80}")
        time.sleep(1.4)

if __name__ == "__main__":
    sui_vanish()
