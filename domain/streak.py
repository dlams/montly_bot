
class InvalidTheme(Exception):
    pass


class StreakTheme():
    def __init__(self, theme: str):
        self.theme = theme
    
    def get_theme(self) -> str:
        return self.theme

    def render_theme(self, streak):
        return streak


def render_themes(theme: StreakTheme, user_streaks):
    _theme = theme.get_theme()
    if len(_theme) != 4:
        raise InvalidTheme

    for streak in user_streaks:
        yield theme.render_theme(streak)