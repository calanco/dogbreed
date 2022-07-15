import uvicorn
import click


@click.command()
@click.option("--port", type=int, default=8080, help="Expose dogbreed at this port.")
@click.option(
    "--host", type=str, default="0.0.0.0", help="Expose dogbreed at this host."
)
@click.option("--debug", type=bool, default=False, help="Run dogbreed in debug mode.")
@click.option("--reload", type=bool, default=False, help="Enable auto reload.")
def main(debug, port, reload, host):
    uvicorn.run(app="app.main:app", port=port, host=host, debug=debug, reload=reload)


if __name__ == "__main__":
    main()
