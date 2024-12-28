# noxfile.py
import nox


@nox.session(python=["3.9", "3.13"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")

