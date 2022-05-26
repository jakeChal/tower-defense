import importlib.resources
import pygame

def load(module_path, name):
    return importlib.resources.path(module_path, name)

def import_image(asset_name: str):
    with load("tower.assets.gfx", asset_name) as resource:
        return pygame.image.load(resource).convert_alpha()


def import_sound(asset_name: str):
    with load("tower.assets.audio", asset_name) as resource:
        return pygame.mixer.Sound(resource)