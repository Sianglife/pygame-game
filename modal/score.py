from modal.gui import score_label


class Score:
    def __init__(self):
        self.score = 0
        self.score_label = score_label

    def hide(self):
        self.score_label.hide()

    def show(self):
        self.score_label.show()

    def reset(self):
        self.score = 0
        self.update_label()

    def plus(self):
        self.score += 1
        self.update_label()

    def update_label(self):
        self.score_label.set_text(f'Score: {self.score}')

    def gameover(self):
        self.score_label.set_text(f'Game Over! Final Score: {self.score}')
