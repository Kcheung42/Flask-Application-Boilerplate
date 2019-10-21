from flask.cli import FlaskGroup
from project import create_app, db
import sys
import unittest

app = create_app()

cli = FlaskGroup(create_app=create_app)
# Now you can work with the app and db directly
# docker-compose exec app flask shell
# >>> app
# >>> db


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
