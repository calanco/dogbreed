import uvicorn
import dogbreed
import click


@click.command()
@click.option('--debug', type=bool, default=True,
              help='Run dogbreed in debug mode.')
@click.option('-p', '--port', type=int, default=8080,
              help='Expose dogbreed at this port.')
def main(debug, port):
    uvicorn.run(app=dogbreed.app, port=port, debug=debug)


if __name__ == '__main__':
    main()
