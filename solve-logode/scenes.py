from manimlib.imports import *

eqn_str=r"{dN\over d{t}}=rN\left({K-N\over K}\right)"

class OpenningScene(Scene):
    def construct(self):
        title=TextMobject("How to solve logistic equation",
            tex_to_color_map={
                "How":YELLOW,
                "solve":GREEN,
                "logistic":ORANGE
            }).scale(2)
        eqn=TexMobject(eqn_str,
            tex_to_color_map={
                "N":ORANGE,
                "K":GREEN,
                "{t}":YELLOW
            })
        gp=VGroup(title,eqn).arrange(DOWN)
        self.play(FadeIn(title))
        self.play(Write(eqn))
        self.wait()
        self.play(FadeOut(gp))
        self.wait()

class AnalyzeEqnScene(Scene):
    def construct(self):
        eqn=TexMobject(eqn_str).scale(1.5).to_edge(UP)
        self.play(Write(eqn))
