import typer
from rich.console import Console
from pathlib import Path
import json

from transformer import CandidateTransformer
from config import load_config

app = typer.Typer(help="Eightfold Multi-Source Candidate Data Transformer")
console = Console()

@app.command()
def transform(
    inputs: list[Path] = typer.Argument(..., help="Input files"),
    config: Path = typer.Option(None, "--config", "-c", help="Custom config"),
    output: Path = typer.Option("output.json", "--output", "-o")
):
    transformer = CandidateTransformer()
    console.print(f"Processing {len(inputs)} sources...")
    
    profiles = []
    for inp in inputs:
        console.print(f"  → {inp}")
        profile = transformer.process_source(inp)
        if profile:
            profiles.append(profile)
    
    merged = transformer.merge_profiles(profiles)
    config_dict = load_config(config)
    final = transformer.project(merged, config_dict)
    
    with open(output, "w") as f:
        json.dump(final, f, indent=2, default=str)
    
    console.print(f"[green]Success! Output → {output}[/green]")
    return final

if __name__ == "__main__":
    app()