import csv, os, json

total_revenue = 0.0
total_items_sold = 0
skipped_rows = 0
revenue_by_item = {}

with open("sample-texts/sales.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        qty_raw = (row.get("qty") or "").strip()
        price_raw = (row.get("price") or "").strip()
        item = (row.get("item") or "").strip()

        try:
            qty = int(qty_raw)
            price = float(price_raw)
        except ValueError:
            skipped_rows += 1
            continue

        line_rev = qty * price
        total_revenue += line_rev
        total_items_sold += qty
        if item:
            revenue_by_item[item] = revenue_by_item.get(item, 0.0) + line_rev

unique_items = len(revenue_by_item)

top_item, top_item_rev = (None, 0.0)
if revenue_by_item:
    top_item, top_item_rev = max(revenue_by_item.items(), key=lambda kv: kv[1])

summary = {
    "total_revenue": round(total_revenue, 2),
    "total_items_sold": total_items_sold,
    "unique_items": unique_items,
    "top_item_by_revenue": {"item": top_item, "revenue": round(top_item_rev, 2)} if top_item else None,
    "skipped_rows": skipped_rows,
}

print(summary)

os.makedirs("sample-outputs", exist_ok=True)
with open("sample-outputs/sales-summary.json", "w") as out:
    json.dump(summary, out, indent=2)
