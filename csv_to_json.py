"""Convert train_data.csv to train_dataset.json with mapped attributes."""

import csv
import json
from pathlib import Path

# CSV column names map directly to JSON attributes
COLUMNS = ["question", "chunk", "extraction_answer", "rules_answer", "url", "label"]


def main(filename):
    script_dir = Path(__file__).parent
    # Use train_dataset.csv if train_data.csv is not found
    csv_path = script_dir / f"{filename}.csv"
    if not csv_path.exists():
        csv_path = script_dir / f"{filename}.csv"
    json_path = script_dir / f"{filename}.json"

    rows = []
    with open(csv_path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Build object with only the requested attributes (in order)
            obj = {key: row.get(key, "") for key in COLUMNS}
            if obj.get("question", "") == "":
                print(f"Skipping empty row: {row}")
                break
            rows.append(obj)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(rows)} records to {json_path}")


if __name__ == "__main__":
    main("train_dataset")
    main("eval_dataset")
