import typer


app = typer.Typer()


@app.callback()
def main_callback() -> None:
    pass


@app.command("create-meeting")
def create_meeting(
    title: str = typer.Option(..., "--title"),
    date: str = typer.Option(..., "--date"),
    owner: str = typer.Option(..., "--owner"),
) -> None:
    print("Meeting Summary:")
    print(f"  Title: {title}")
    print(f"  Date: {date}")
    print(f"  Owner: {owner}")
    print("  Status: Successfully created!")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
