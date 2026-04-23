from pathlib import Path

import pandas as pd


def run_demo() -> None:
    """Create a tiny DataFrame and save it as CSV to data/processed."""
    df = pd.DataFrame(
        {
            "name": ["Anna", "Bo", "Carla"],
            "score": [85, 92, 78],
        }
    )

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "scores.csv"

    df.to_csv(output_path, index=False)
    print(f"Saved demo data to: {output_path}")


if __name__ == "__main__":
    run_demo()
