import pytest
import domain.streak


def test_raise_when_apply_invalid_theme():
    invalid_theme = domain.streak.StreakTheme("INVALID")
    with pytest.raises(domain.streak.InvalidTheme):
        for _ in domain.streak.render_themes(invalid_theme, []):
            ...


# def test_apply_correct_theme():
#     theme_1 = domain.streak.StreakTheme("GOOD")