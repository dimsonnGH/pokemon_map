import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def get_pokemon_img_url(pokemon):
    return pokemon.image.url if pokemon.image else ''


def get_dict_from_pokemon(pokemon, request):
    pokemon_dict = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title,
        "img_url": request.build_absolute_uri(get_pokemon_img_url(pokemon)),
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "previous_evolution": get_pokemon_evolution(pokemon.previous_evolution, request),
        "next_evolution" : get_pokemon_evolution(pokemon.next_evolution.first(), request)
    }
    return pokemon_dict

def get_pokemon_evolution(pokemon, request):
    if pokemon:
        evolution = {
            "pokemon_id": pokemon.id,
            "title_ru": pokemon.title,
            "img_url": request.build_absolute_uri(get_pokemon_img_url(pokemon))
        }
    else:
        evolution = None

    return evolution


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    '''with open("pokemon_entities/pokemons.json", encoding="utf-8") as database:
        pokemons = json.load(database)['pokemons']

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon['entities']:
            add_pokemon(
                folium_map, pokemon_entity['lat'], pokemon_entity['lon'],
                pokemon['title_ru'], pokemon['img_url'])

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon['pokemon_id'],
            'img_url': pokemon['img_url'],
            #'title_ru': pokemon['title_ru'],
            'title_ru': 'title_ru',
        })'''

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in PokemonEntity.objects.all():
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title, request.build_absolute_uri(get_pokemon_img_url(pokemon_entity.pokemon)))

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': get_pokemon_img_url(pokemon),
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    '''with open("pokemon_entities/pokemons.json", encoding="utf-8") as database:
        pokemons = json.load(database)['pokemons']

    for pokemon in pokemons:
        if pokemon['pokemon_id'] == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon['entities']:
        add_pokemon(
            folium_map, pokemon_entity['lat'], pokemon_entity['lon'],
            pokemon['title_ru'], pokemon['img_url'])

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})'''

    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon):
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon.title, request.build_absolute_uri(get_pokemon_img_url(pokemon)))


    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': get_dict_from_pokemon(pokemon, request)})
