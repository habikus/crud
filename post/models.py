from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Kisiler(models.Model):
    adsoyad = models.CharField(max_length=60, verbose_name='Adı ve Soyadı')
    sinifi = models.CharField(max_length=60, verbose_name='Sınıfı')
    nosu = models.CharField(max_length=60, verbose_name='Nosu')
    telefonu = models.CharField(max_length=60, verbose_name='Telefonu')
    email = models.EmailField(verbose_name='e-Mail')
    aciklama  = models.TextField(verbose_name='Açıklama')
    # aciklama = RichTextField(verbose_name="Açıklama")
    slug = models.SlugField(unique=True, editable=False, max_length=70)

    def __str__(self):                      # Admin listede Project Object yerine Adı ve Soyadı yazacak
        return self.adsoyad

    def get_absolute_url(self):     # ayrıntılı inceleme slug ile farkı ne
        return reverse('kisi_incele', kwargs={'slug': self.slug})
    #   return "/%s.html" % self.slug

    def get_absolute_url2(self):     # ayrıntılı inceleme slug ile farkı ne
        return reverse('kisi_incelefull', kwargs={'slug': self.slug})
    #   return "/%s.html" % self.slug

    # def get_create_url(self):
    #     return reverse('post:create', kwargs={'slug': self.slug})
    #
    def get_update_url(self):
        return reverse('kisi_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('kisi_delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.adsoyad.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Kisiler.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):                  # Kaydet deyince bu procedure devreye girer
        self.slug = self.get_unique_slug()
        return super(Kisiler, self).save(*args, **kwargs)

    class Meta:                                       # Adminde Kisilers yerine Kişiler gözükür
        verbose_name_plural = 'Kişiler'

class Kitaplar(models.Model):
    kitapadi = models.CharField(max_length=60, verbose_name='Kitap Adı')
    yazari = models.CharField(max_length=60, verbose_name='Yazarı')
    yayinevi = models.CharField(max_length=60, verbose_name='Yayinevi')
    turu = models.CharField(max_length=60, verbose_name='Türü')
    aciklama  = models.TextField(verbose_name='Açıklama')
    #aciklama = RichTextField(verbose_name="Açıklama")
    slug = models.SlugField(unique=True, editable=False, max_length=70)

    def __str__(self):
        return self.kitapadi

    def get_absolute_url(self):     # ayrıntılı inceleme slug ile farkı ne
        return reverse('kitap_incele', kwargs={'slug': self.slug})
    #   return "/%s.html" % self.slug

    def get_absolute_url2(self):     # ayrıntılı inceleme slug ile farkı ne
        return reverse('kitap_incelefull', kwargs={'slug': self.slug})
    #   return "/%s.html" % self.slug

    def get_update_url(self):
        return reverse('kitap_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('kitap_delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.kitapadi.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Kitaplar.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):                  # Kaydet deyince bu procedure devreye girer
        self.slug = self.get_unique_slug()
        return super(Kitaplar, self).save(*args, **kwargs)

    class Meta:                           # Adminde Kitaplars yerine Kitaplar gözükür
        verbose_name_plural = 'Kitaplar'

class Hareketler(models.Model):
    adsoyad = models.CharField(max_length=60, verbose_name='Adı Soyadı')
    kitapadi = models.CharField(max_length=60, verbose_name='Kitap Adı')
    alistarihi = models.DateTimeField(verbose_name="Alış Tarihi", auto_now_add=False)
    verilistarihi =  models.DateTimeField(verbose_name="Veriliş Tarihi", auto_now_add=False)
    aciklama = models.TextField(verbose_name='Açıklama')
    slug = models.SlugField(unique=True, editable=False, max_length=70)

    def __str__(self):
        return self.adsoyad

    def get_absolute_url(self):     # ayrıntılı inceleme slug ile farkı ne
        return reverse('hareket_incele', kwargs={'slug': self.slug})

    def get_absolute_url2(self):     # ayrıntılı inceleme slug ile farkı ne
        return reverse('hareket_incelefull', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('hareket_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('hareket_delete', kwargs={'slug': self.slug})


    def get_unique_slug(self):
        slug = slugify(self.adsoyad.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Hareketler.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):                  # Kaydet deyince bu procedure devreye girer
        self.slug = self.get_unique_slug()
        return super(Hareketler, self).save(*args, **kwargs)

    class Meta:                           # Adminde Hareketlers yerine Hareketler gözükür
        verbose_name_plural = 'Hareketler'