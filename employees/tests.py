from django.test import TestCase

from .models import Employee

deps = [0, 'AD', 'PR', 'CO']

class EmployeeModelTestCase(TestCase):

    def setUp(self):
        self.bosses = []
        self.tecnics = []

        for i in range(1,4):
            self.bosses.append(Employee.objects.create_user("boss{}".format(i), password="boss123456789", departament=deps[i], role='1'))
        for i in range(1, 13):
            self.tecnics.append(Employee.objects.create_user("tecnic{}".format(i), password="tecnic123456789", departament=deps[(i % 3)+1], role='2', boss=self.bosses[i%3]))
        for i in range(1, 49):
            Employee.objects.create_user("student{}".format(i), password="student123456789", departament=deps[(i % 3)+1], role='3', boss=self.tecnics[i%12])

    def test_promote(self):
        tecnic = self.tecnics[0]
        tecnic.promote()
        self.assertEqual(tecnic.role, '1')
        self.assertEqual(tecnic.is_promoted(), True)
        self.assertEqual(tecnic.has_promoted(), True)
        self.assertEqual(tecnic.times_promoted(), 1)
    
    def test_not_promoted(self):
        tecnic = self.tecnics[1]
        self.assertEqual(tecnic.role, '2')
        self.assertEqual(tecnic.is_promoted(), False)
        self.assertEqual(tecnic.has_promoted(), False)
        self.assertEqual(tecnic.times_promoted(), 0)

    def test_go_travel(self):
        tecnic = self.tecnics[2]
        tecnic.go_travel()
        self.assertEqual(tecnic.is_traveling, True)
        tecnic.end_travel()
        self.assertEqual(tecnic.is_traveling, False)
    
    def test_left_company(self):
        tecnic = self.tecnics[3]
        tecnic.left_company()