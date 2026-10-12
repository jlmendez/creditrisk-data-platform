from pathlib import Path
import csv
import random

def generate_loans(n=100, seed=42):
    rng = random.Random(seed)
    output = Path("data/raw/prestamos.csv")
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["loan_id", "monto", "dias_mora"])

        for i in range(1, n + 1):
            writer.writerow([
                i,
                rng.randint(5000, 150000),
                rng.choice([0, 0, 0, 15, 30, 60, 90])
            ])

    return output

if __name__ == "__main__":
    path = generate_loans()
    print(f"Archivo generado: {path}")
