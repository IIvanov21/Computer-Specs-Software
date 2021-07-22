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

class TestCreate(TestBase):
    def test_add_get(self):
        response=self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Build name:',response.data)
        self.assertIn(b'1.Create a build name to asscociate with your choices.',response.data)
        self.assertIn(b'2.Use the links below to choose parts for your build.',response.data)

    def test_add_get_links(self):
        response=self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Read Functions',response.data)
        self.assertIn(b'Motherboard',response.data)
        self.assertIn(b'Case',response.data)
        self.assertIn(b'CPU',response.data)

    def test_add_name_exists(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato'),follow_redirects=True)
        self.assertIn(b'Build name already exists!',response.data)

    def test_add_name_created(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        self.assertIn(b'Build name added successfully!',response.data)

    def test_add_new_motherboard(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        response=self.client.post(url_for('addMotherboard'), data = dict(build_name='Potato2',keyType="XL-ATX",make="Asus",model="Strix",series='350-f gaming'),follow_redirects=True)
        self.assertIn(b'Added new motherboard',response.data)
    
    def test_add_new_motherboard_two(self):
        response=self.client.post(url_for('addMotherboard'), data = dict(build_name='Potato2',keyType="XL-ATX",make="Asus",model="Strix",series='350-f gaming'),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)

    def test_add_new_cpu(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        response=self.client.post(url_for('addCPU'), data = dict(build_name='Potato2',make="AMD",model="Ryzen 5",series='3600x'),follow_redirects=True)
        self.assertIn(b'Added a CPU!',response.data)
    
    def test_add_new_cpu_two(self):
        response=self.client.post(url_for('addCPU'), data = dict(build_name='Potato2',make="AMD",model="Ryzen 5",series='3600x'),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)

    def test_add_new_case(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        response=self.client.post(url_for('addCase'), data = dict(build_name='Potato2',keyType="XL-ATX", make="NZXT",model="H510"),follow_redirects=True)
        self.assertIn(b'Added a Case!',response.data)
    
    def test_add_new_case_two(self):
        response=self.client.post(url_for('addCase'), data = dict(build_name='Potato2',keyType="XL-ATX", make="NZXT",model="H510"),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)

class TestUpdate(TestBase):
    def test_update_name(self):
        response=self.client.post(url_for('update'), data = dict(build_name='Potato',new_build_name='Potato2'),follow_redirects=True)
        self.assertIn(b'Update the build name successfully!',response.data)

    def test_update_name_two(self):
        response=self.client.post(url_for('update'), data = dict(build_name='Potato',new_build_name='Potato'),follow_redirects=True)
        self.assertIn(b'There is another build using this name! Please try again.',response.data)

    def test_update_name_three(self):
        response=self.client.post(url_for('update'), data = dict(build_name='Potato2',new_build_name='Potato'),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data) 

    def test_update_motherboard(self):
        response=self.client.post(url_for('updateMotherboard'), data = dict(build_name='Potato',keyType="XL-ATX",make="Asus",model="Strix",series='350-f gaming'),follow_redirects=True)
        self.assertIn(b'Updated your motherboard choice!',response.data)  

    def test_update_motherboard_two(self):
        response=self.client.post(url_for('updateMotherboard'), data = dict(build_name='Potato2',keyType="XL-ATX",make="Asus",model="Strix",series='350-f gaming'),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)

    def test_update_motherboard_three(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        response=self.client.post(url_for('updateMotherboard'), data = dict(build_name='Potato2',keyType="XL-ATX",make="Asus",model="Strix",series='350-f gaming'),follow_redirects=True)
        self.assertIn(b'Ensure a motherboard was added to the build!',response.data)

    def test_update_new_cpu(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        response=self.client.post(url_for('updateCPU'), data = dict(build_name='Potato2',make="AMD",model="Ryzen 5",series='3600x'),follow_redirects=True)
        self.assertIn(b'Couldnt find the desired CPU ensure it has been added!',response.data)
    
    def test_update_new_cpu_two(self):
        response=self.client.post(url_for('updateCPU'), data = dict(build_name='Potato2',make="AMD",model="Ryzen 5",series='3600x'),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)

    def test_update_new_cpu_three(self):
        response=self.client.post(url_for('updateCPU'), data = dict(build_name='Potato',make="AMD",model="Ryzen 5",series='3600x'),follow_redirects=True)
        self.assertIn(b'Updated the CPU!',response.data)

    def test_update_new_case(self):
        response=self.client.post(url_for('updateCase'), data = dict(build_name='Potato',keyType="XL-ATX", make="Corsair",model="H310"),follow_redirects=True)
        self.assertIn(b'Updated your case choice!',response.data)
    
    def test_update_new_case_two(self):
        response=self.client.post(url_for('updateCase'), data = dict(build_name='Potato2',keyType="XL-ATX", make="NZXT",model="H510"),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)

    def test_update_new_case_three(self):
        response=self.client.post(url_for('add'), data = dict(name='Potato2'),follow_redirects=True)
        response=self.client.post(url_for('updateCase'), data = dict(build_name='Potato2',keyType="XL-ATX", make="NZXT",model="H510"),follow_redirects=True)
        self.assertIn(b'Ensure you have added a case to this build!',response.data)

class TestDelete(TestBase):
    def test_delete_all(self):
        response=self.client.post(url_for('delete'), data = dict(build_name='Potato',section="All"),follow_redirects=True)
        self.assertIn(b'Succefully deleted the selected build!',response.data)
    def test_delete_all_two(self):
        response=self.client.post(url_for('delete'), data = dict(build_name='Potato2',section="All"),follow_redirects=True)
        self.assertIn(b'Build name doesnt exist.. Try again!',response.data)
    def test_delete_motherboard(self):
        response=self.client.post(url_for('delete'), data = dict(build_name='Potato',section="Motherboard"),follow_redirects=True)
        self.assertIn(b'Deleted the motherboard choice for this build!',response.data)
    def test_delete_cpu(self):
        response=self.client.post(url_for('delete'), data = dict(build_name='Potato',section="CPU"),follow_redirects=True)
        self.assertIn(b'Deleted the CPU choice for this build!',response.data)
    def test_delete_case(self):
        response=self.client.post(url_for('delete'), data = dict(build_name='Potato',section="Case"),follow_redirects=True)
        self.assertIn(b'Deleted the case choice for this build!',response.data)