import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import *


class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

    def render(self):
        super(GameOverScene, self).render()

        self.clearText()
        self.addText("PRESS F1 TO RESTART THE GAME", 400, 400, size=30)

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.type == 2:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)

