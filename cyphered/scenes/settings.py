import pygame

from ._base import BaseScene
from ..ui import Button
from ..services.settings import Settings
from cyphered.ui.Text_displ import text_displ


class SettingsScene(BaseScene):
    def __init__(self):
        BaseScene.__init__(self)
        if Settings.jump_key == "space":
            self.jump_button = Button("пробел", font_size=25, step_x=-160)  # fontt='./Resources/font.ttf')
        elif Settings.jump_key == "w":
            self.jump_button = Button("w", font_size=25, step_x=-160)
        if Settings.move_keys == "arrows":
            self.rightleft_button = Button("стрелки", step_x=300, font_size=25)
        elif Settings.move_keys == "ad":
            self.rightleft_button = Button("ad", step_x=300, font_size=25)
        self.music_button_plus = Button("+", font_color=(255, 255, 255), step_x=-390, font_size=35)
        self.music_button_minus = Button("-", font_color=(255, 255, 255), step_x=-430, font_size=35)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.music_button_plus[2].collidepoint(mouse_pos):
                        pass
                    if self.jump_button[2].collidepoint(mouse_pos):
                        if Settings.jump_key == "w":
                            Settings.jump_key = 'space'
                        else:
                            Settings.jump_key = 'w'
                    if self.rightleft_button[2].collidepoint(mouse_pos):
                        if Settings.move_keys == "arrows":
                            Settings.move_keys = "ad"
                        else:
                            Settings.move_keys = "arrows"
                    Settings.save_settings()

    def render(self, screen):
        # if music == 'on':
        #     color_music_button = (255, 0, 0)
        pygame.draw.rect(screen, (0, 0, 0), self.music_button_plus[2])
        screen.blit(self.music_button_plus[0], self.music_button_plus[1])
        pygame.draw.rect(screen, (0, 0, 0), self.music_button_minus[2])
        screen.blit(self.music_button_minus[0], self.music_button_minus[1])
        text_displ("Громкость музыки", screen, step_x=-390, step_y=-80, font_size=25,
                   font1="./resources/fonts/font.ttf")
        text_displ("Прыжок", screen, step_x=-160, step_y=-80, font_size=25,
                   font1="./resources/fonts/font.ttf")
        text_displ("Управление кнопками движения вправо-влево", screen, step_x=250, step_y=-80, font_size=25,
                   font1="./resources/fonts/font.ttf")

        pygame.draw.rect(screen, (0, 0, 0), self.jump_button[2])
        screen.blit(self.jump_button[0], self.jump_button[1])
        pygame.draw.rect(screen, (0, 0, 0), self.rightleft_button[2])
        screen.blit(self.rightleft_button[0], self.rightleft_button[1])