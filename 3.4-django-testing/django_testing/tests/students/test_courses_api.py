import pytest as pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_create_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get(f"/api/v1/courses/{course[0].id}/")

    assert response.status_code == 200
    data = response.json()
    assert course[0].name == data['name']


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=15)

    response = client.get(f"/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get(f"/api/v1/courses/?id={course[0].id}")
    assert response.status_code == 200
    data = response.json()
    assert course[0].id == data[0]['id']


@pytest.mark.django_db
def test_filter_name_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get(f"/api/v1/courses/?name={course[0].name}")
    assert response.status_code == 200
    data = response.json()
    assert course[0].name == data[0]['name']


@pytest.mark.django_db
def test_create_one_course(client):
    response = client.post("/api/v1/courses/", data={'name': 'test course'})

    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'test course'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.patch(f"/api/v1/courses/{course[0].id}/", {'name': 'update course name'})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'update course name'


@pytest.mark.django_db
def test_destroy_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.delete(f"/api/v1/courses/{course[0].id}/")
    assert response.status_code == 204
