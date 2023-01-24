import nox


locations = "src", "tests", "noxfile.py", "docs/conf.py"
package = "new_repository"


@nox.session(python="3.8")
def tests(session):
    """Run the test suite."""
    session.run("poetry", "install", "--no-dev", external=True)
    session.run("pytest", "--cov")


@nox.session(python="3.8")
def lint(session):
    """Lint using flake8."""
    args = locations
    session.install("flake8")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session):
    """Run black code formatter."""
    args = locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def xdoctest(session):
    """Run examples with xdoctest."""
    args = ["all"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("xdoctest")
    session.run("python", "-m", "xdoctest", package, *args)


@nox.session(python="3.8")
def docs(session):
    """Build the documentation."""
    session.install("sphinx")
    session.run("sphinx-build", "docs", "docs/_build")