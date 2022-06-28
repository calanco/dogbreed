import uvicorn
import click


@click.command()
@click.option('--debug', type=bool, default=False,
              help='Run dogbreed in debug mode.')
@click.option('--reload', type=bool, default=False,
              help='Enable auto reload.')
@click.option('-p', '--port', type=int, default=8080,
              help='Expose dogbreed at this port.')
def main(debug, port, reload):
    uvicorn.run(app="dogbreed:app", port=port, debug=debug, reload=reload)


if __name__ == '__main__':
    main()
