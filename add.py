import click

from resources import Resources


def get_resource(ctx, param, value):
    return Resources()


@click.command()
@click.argument('title')
@click.argument('url')
@click.option('--tags', '-t', default="", help="Enter tags in a,b,c format")
@click.option('--resources', callback=get_resource)
def add(resources, title, url, tags):
    tags = tags.split(",")
    resources.add(title, url, tags)


if __name__ == '__main__':
    add()
