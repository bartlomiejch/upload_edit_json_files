from django.test import TestCase
from p2_homework.models import Document

# Create your tests here.
class ItemModelTest(TestCase):
	
    def test_default_text(self):
        doc = Document()
        self.assertEqual(doc.docfile, '')
        
    def 
