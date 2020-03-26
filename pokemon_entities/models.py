from django.db import models


class Pokemon(models.Model):
    """Вид покемона"""
    title = models.CharField(max_length=200, verbose_name='наименование')
    image = models.ImageField(null=True, blank=True, verbose_name='картинка')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='наименование на английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='наименование на японском')
    description = models.TextField(blank=True, verbose_name='описание')
    previous_evolution = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_evolutions', verbose_name='эволюционировал из')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Экземпляр покемона"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон')
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='время появления')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='время исчезновения')
    level = models.IntegerField(default=0, verbose_name='уровень')
    health = models.IntegerField(default=0, verbose_name='здоровье')
    strength = models.IntegerField(default=0, verbose_name='атака')
    defence = models.IntegerField(default=0, verbose_name='защита')
    stamina = models.IntegerField(default=0, verbose_name='выносливость')


    def __str__(self):
        return '{}: {}°, {}°'.format(self.pokemon, self.lat, self.lon)