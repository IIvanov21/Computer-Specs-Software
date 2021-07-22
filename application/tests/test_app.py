from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.classes import Motherboard,CPU,ComputerCase, Build


class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)

        return app

    def setUp(self):
        db.create_all()

        new_build=Build(name='Potato')
        db.session.add(new_build)
        db.session.commit()
        new_motherboard_entry=Motherboard(keyType='XL-ATX',make='Asus',model='Strix',
            series='360b',build=Build.query.filter_by(name='Potato').first())
        new_cpu_entry=CPU(make='AMD',series='3600x',model='Ryzen5',build=Build.query.filter_by(name='Potato').first())
        new_case_entry=ComputerCase(keyType='XL-ATX',make='NZXT',model='H510',build=Build.query.filter_by(name='Potato').first())

        db.session.add(new_motherboard_entry)
        db.session.add(new_case_entry)
        db.session.add(new_cpu_entry)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_read_get(self):
        response=self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Build name',response.data)
    
    def test_read_get_existing(self):
        response=self.client.post(url_for('read'), data = dict(build_name='Potato'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Motherboard name:',response.data)
        self.assertIn(b'XL-ATX Asus Strix 360b',response.data)
        self.assertIn(b'CPU name:',response.data)
        self.assertIn(b'AMD Ryzen5 3600x',response.data)
        self.assertIn(b'Case name:',response.data)
        self.assertIn(b'XL-ATX NZXT H510',response.data)

    def test_read_get_nonexisting(self):
        response=self.client.post(url_for('read'), data = dict(build_name='PotatoIsNotExistant'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)
        self.assertIn(b'You havent added a motherboard!',response.data)
        self.assertIn(b'You havent added a CPU!',response.data)
        self.assertIn(b'You havent added a case!',response.data)

    def test_read_get_links(self):
        response=self.client.post(url_for('read'), data = dict(build_name='Potato'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Functions',response.data)
        self.assertIn(b'Update Functions',response.data)
        self.assertIn(b'Delete Functions',response.data)
    def test_read_get_error_links(self):
        response=self.client.post(url_for('read'), data = dict(build_name='PotatoIsNotExistant'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Select Motherboard!',response.data)
        self.assertIn(b'Select CPU!',response.data)
        self.assertIn(b'Select Case!',response.data)


