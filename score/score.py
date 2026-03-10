import pygame
import json

from uses.use import SCREEN


class Score:

    def __init__(self):
        self._score = 0
        self._best_score = self.load_score()

    def increase(self):
        self._score += 1

    def show_score(self):
        font = pygame.font.SysFont("Arial", 30)
        score_text = font.render(f"Score: {self._score}",
                                      True, (255, 255, 255))
        SCREEN.blit(score_text, (10, 10))
        self._show_best_score()

    def _show_best_score(self):
        font = pygame.font.SysFont("Arial", 30)
        score_text = font.render(f"Best Score: {self._best_score}",
                                 True, (255, 255, 255))
        SCREEN.blit(score_text, (10, 60))

    def save_score(self, check: bool = False):
        if self._score > self.load_score() or check:
            with open("./score/score.json", "w") as f:
                json.dump({"best_score": self._score}, f)


    @staticmethod
    def load_score():
        try:
            with open("./score/score.json", "r") as f:
                data = json.load(f)
                return data["best_score"]
        except FileNotFoundError:
            return 0


    def update_score(self):
        if self._score > self._best_score:
            self._best_score = self._score

    def reset_score(self):
        self._score = 0
        self._best_score = 0
        self.save_score(check=True)

