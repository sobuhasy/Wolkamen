import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
    
    def draw(self):
        self.render_game_objects()

    def render_game_objects(self, objects_to_render):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return{
            '1': self.get_texture('res/texture/1.png'),
            '2': self.get_texture('res/texture/2.png'),
            '3': self.get_texture('res/texture/3.png'),
            '4': self.get_texture('res/texture/4.png'),
            '5': self.get_texture('res/texture/5.png')
        }