import pytest

from hw_14.project import Project
from hw_14.user import User


@pytest.fixture
def project():
    return Project([User('34', 'igor', '2'), User('435', 'katya', '3')])


@pytest.fixture
def admin():
    return User('34', 'igor', '2')


@pytest.fixture
def user():
    return User('356', 'Petya', '3')


def test_from_json(project):
    lengts = len(project.from_json('users.json').user_lst)
    assert lengts == 4


def test_login(project, admin):
    project.login(admin.u_id, admin.name)
    assert project.admin == admin


def test_add_user(project, user, admin):
    project.login(admin.u_id, admin.name)
    project.add_user(user.u_id, user.name, user.level)
    assert user in project.user_lst


def test_del_user(project, admin):
    project.login(admin.u_id, admin.name)
    project.del_user(project.user_lst[1].u_id, project.user_lst[1].name, project.user_lst[1].level)
    assert len(project.user_lst) == 1


if __name__ == '__main__':
    pytest.main(['-v'])


