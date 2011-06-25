# -*- coding: utf-8 -*-

from django.db import models


class Organization(models.Model):
    """En organisation som har tjänster i katalogen"""
    name = models.CharField(u"Namn", max_length=255)
    number = models.CharField(u"Organisationsnummer", max_length=11)
    website = models.URLField(u"Länk", verify_exists = False)
    phone = models.CharField(u"Telefon", max_length=255)
    email = models.EmailField(u"E-post")
    address = models.CharField(u"Adress", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Organisation" 
        verbose_name_plural = u"Organisationer"
        ordering = ('name',)



class Personal(models.Model):
    """Person i en organisation som agerar kontakt för en eller flera tjänster."""
    name = models.CharField(u"Namn t.ex. <em>Karl Karlsson</em>", max_length=255)
    email = models.EmailField(u"E-post")
    phone = models.CharField(u"Telefon", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Kontaktperson" 
        verbose_name_plural = u"Kontaktpersoner"
        ordering = ('name',)



class Contact(models.Model):
    role_name = models.CharField(u"Rollnamn", max_length=255)
    role_description = models.TextField(u"Rollbeskrivning")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    personal = models.ForeignKey(Personal)
    
    def __unicode__(self):
        return self.personal.name + " (" + self.role_name + ")"

    class Meta:
        verbose_name= u"Kontakt" 
        verbose_name_plural = u"Kontakter"
        ordering = ('role_name',)


class Category(models.Model):
    """Kategori"""
    title = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name= u"Kategori" 
        verbose_name_plural = u"Kategorier"
        ordering = ('title',)



class Protocol(models.Model):
    """Protokoll som tjänsten använder"""
    title = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning")
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name= u"Protokoll" 
        verbose_name_plural = u"Protokoll"
        ordering = ('title',)



class Service(models.Model):
    """En tjänst i katalogen"""
    title = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning")
    URL = models.URLField(u"Länk", verify_exists = False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    contacts = models.ManyToManyField(Contact, related_name="services")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name= u"Tjänst" 
        verbose_name_plural = u"Tjänster"
        ordering = ('title',)



class ServiceProperty(models.Model):
    """Egenskaper för en tjänst"""
    version = models.CharField(u"Version", max_length=100)
    current_state = models.CharField(max_length=100)
    URL_test = models.URLField(u"Länk till testversion", verify_exists = False)
    URL_info = models.URLField(u"Länk till informationssida", verify_exists = False)
    keywords = models.TextField(u"Nyckelord, kommaseparerade")
    availability = models.TextField(u"Tillgänglighet")
    authentication = models.CharField(max_length=100)
    other = models.TextField(u"Övrig information")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Relationer
    protocol = models.ForeignKey(Protocol)
    service = models.ForeignKey(Service)
    categories = models.ManyToManyField(Category, related_name='service_property')
    contacts = models.ManyToManyField(Contact)
    

    def __unicode__(self):
        return self.version

    class Meta:
        verbose_name= u"Tjänsteegenskaper" 
        verbose_name_plural = u"Tjänsteegenskaper"
        ordering = ('-version',)
