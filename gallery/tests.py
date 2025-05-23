from django.test import TestCase
from django.urls import reverse
from gallery.models import Image, Category
from datetime import date, datetime, timedelta


# Create your tests here.
class GalleryViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='technology')
        self.old_image = Image.objects.create(title='First computer',
                                              image='https://www.google.com/imgres?q=computer&imgurl=https%3A%2F%2Fcdn.britannica.com%2F77%2F170477-050-1C747EE3%2FLaptop-computer.jpg&imgrefurl=https%3A%2F%2Fwww.britannica.com%2Ftechnology%2Fcomputer&docid=9oCv57c03X8yLM&tbnid=_bAxRLesPf9HpM&vet=12ahUKEwjS0b6UrLmNAxXmBdsEHSYVHY0QM3oECGYQAA..i&w=1600&h=1097&hcb=2&ved=2ahUKEwjS0b6UrLmNAxXmBdsEHSYVHY0QM3oECGYQAA',
                                              created_date=datetime.now() - timedelta(
                                                  days=365),
                                              age_limit=100)
        self.old_image.categories.set([self.category])
        self.new_image = Image.objects.create(title='Second computer',
                                              image='https://www.google.com/imgres?q=computer&imgurl=https%3A%2F%2Frukminim2.flixcart.com%2Fimage%2F850%2F1000%2Fxif0q%2Fdesktop-computer%2Fo%2Fj%2Fw%2F0-hs16-win-11-hasons-original-imah4ky38fubg6mq.jpeg%3Fq%3D20%26crop%3Dfalse&imgrefurl=https%3A%2F%2Fwww.flipkart.com%2Fhasons-core-i5-12th-gen-16-gb-1-tb-windows-11-assembled-desktop-computer%2Fp%2Fitm667a30e9b2990%3Fpid%3DDPCGRDGDDDESS5NH%26cmpid%3Dproduct.share.pp%26_refId%3DPP.9fbe3d8e-d440-42a5-8cae-963bfd5cdf9f.DPCGRDGDDDESS5NH&docid=WzUwiXNwZ0p-hM&tbnid=kiofPcQ9ldnd8M&vet=12ahUKEwi36qqLrbmNAxVjA9sEHZFFGUIQM3oECDQQAA..i&w=850&h=610&hcb=2&ved=2ahUKEwi36qqLrbmNAxVjA9sEHZFFGUIQM3oECDQQAA',
                                              created_date=datetime.now(),
                                              age_limit=40)
        self.new_image.categories.set([self.category])

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_context(self):
        response = self.client.get(reverse('main'))
        self.assertIn(self.new_image, response.context['images'])
        self.assertNotIn(self.old_image, response.context['images'])


class ImageDetailViewTests(TestCase):
    def setUp(self):
        self.image = Image.objects.create(title='First computer',
                                              image='https://www.google.com/imgres?q=computer&imgurl=https%3A%2F%2Fcdn.britannica.com%2F77%2F170477-050-1C747EE3%2FLaptop-computer.jpg&imgrefurl=https%3A%2F%2Fwww.britannica.com%2Ftechnology%2Fcomputer&docid=9oCv57c03X8yLM&tbnid=_bAxRLesPf9HpM&vet=12ahUKEwjS0b6UrLmNAxXmBdsEHSYVHY0QM3oECGYQAA..i&w=1600&h=1097&hcb=2&ved=2ahUKEwjS0b6UrLmNAxXmBdsEHSYVHY0QM3oECGYQAA',
                                              created_date=datetime.now() - timedelta(
                                                  days=365),
                                              age_limit=100)

    def test_image_detail_view_status_code(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
