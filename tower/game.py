from dataclasses import dataclass
import pygame
from tower.states import GameState, StateError
from tower import constants

@dataclass
class TowerGame:

    screen: pygame.Surface
    screen_rect: pygame.Rect
    fullscreen: bool
    state: GameState

    @classmethod
    def create(cls, fullscreen=False):
        game = cls(
            screen=None,
            screen_rect=constants.SCREENRECT,
            fullscreen=fullscreen,
            state=GameState.initializing
        )
        game.init()
        return game

    def set_state(self, state):
        self.state = state

    def assert_state_is(self, *expected_states: GameState):
        """
        Asserts that the game engine is one of
        `expected_states`. If that assertions fails, raise
        `StateError`.
        """
        if not self.state in expected_states:
            raise StateError(
                f"Expected the game state to be one of {expected_states} not {self.state}"
            )


    def loop(self):
        while self.state != GameState.quitting:
            if self.state == GameState.main_menu:
                # pass control to the game menu's loop
                pass
            elif self.state == GameState.map_editing:
                # edit map
                pass
            elif self.state == GameState.game_playing:
                # etc
                pass
        self.quit()

    def quit(self):
        pygame.quit()

    def start_game(self):
        self.assert_state_is(GameState.initialized)
        self.set_state(GameState.main_menu)
        self.loop()

    def init(self):
        self.set_state(GameState.initializing)
        pygame.init()
        window_style = pygame.FULLSCREEN if self.fullscreen else 0
        # We want 32 bits of color depth
        bit_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
        screen = pygame.display.set_mode(self.screen_rect.size, window_style, bit_depth)
        pygame.mixer.pre_init(
            frequency=44100,
            size=32,
            # N.B.: 2 here means stereo, not the number of channels to
            # use in the mixer
            channels=2,
            buffer=512,
        )
        pygame.font.init()
        self.screen = screen
        self.state = GameState.initialized

        self.assert_state_is(GameState.initialized)

