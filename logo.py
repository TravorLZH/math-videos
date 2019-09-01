from manimlib.imports import *

class LogoScene(Scene):
    def construct(self):
        welcome=TextMobject("Welcome to Travor Liu's",
            tex_to_color_map={
                "Welcome":GREEN,
                "Travor Liu":BLUE
            })
        e_def=TexMobject(r"e=\lim_{n\to\infty}\left(1+{1\over {n}}\right)^n",
            tex_to_color_map={
                r"\lim_{n\to\infty}":MAROON
            })
        circle_int=TexMobject(r"\int_{-r}^r2\sqrt{r^2-x^2}dx=\pi r^2",
            tex_to_color_map={
                r"\int_{-r}^r":YELLOW
            })
        moments=TextMobject("Moments").scale(2)
        moments.set_color_by_gradient(RED,YELLOW,GREEN,PURPLE)
        gp=VGroup(e_def,welcome,moments,circle_int).arrange(DOWN)
        self.add(gp)
        self.wait()
