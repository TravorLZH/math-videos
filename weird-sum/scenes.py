from manimlib.imports import *

class IntroScene(Scene):
    def construct(self):
        tit=TextMobject(r"Why is $\zeta(z)$ making sense?",
            tex_to_color_map={
                "Why":GREEN,
                "analytic":BLUE,
                "making sense":YELLOW
            }).scale(2)
        eqn=TexMobject(r"\zeta(-1)=1+2+3+\cdots=-{1\over12}^*",
            tex_to_color_map={
                r"\zeta(-1)":PURPLE
            }).scale(1.5)
        gp=VGroup(tit,eqn).arrange(DOWN)
        note=TextMobject("* Does not guarantee rigorousness").scale(0.8) \
            .to_edge(RIGHT).to_edge(DOWN)
        self.play(FadeIn(tit))
        self.play(Write(eqn))
        self.wait()
        self.play(FadeIn(note))
        self.wait()
        self.play(FadeOut(note),FadeOut(gp))
        self.wait()

table=r"""
\begin{tabular}{c|c|c|c|c|c}
$\times$& 1 & -1 & 1 & -1 & $\cdots$ \\
\hline
1 & 1 & -1 & 1 & -1 & $\cdots$ \\
\hline
-1 & -1 & 1 & -1 & $\cdots$ \\
\hline
1&1&-1&$\cdots$ \\
\hline
-1&-1&$\cdots$ \\
\hline
\end{tabular}
"""

class OneMinusOneScene(Scene):
    def construct(self):
        eqn=TexMobject(r"(1-1+1-1+1-1+\cdots)^2\\=(1-1+\cdots)" \
            r"\times(1-1+\cdots)")
        tbl=TextMobject(table).scale(1.2)
        VGroup(eqn,tbl).arrange(DOWN)
        self.play(FadeIn(eqn))
        self.play(Write(tbl))
        self.wait(2)
        eqnf=TexMobject(r"=1-2+3-4+5-6\\+7-8+9-10+\cdots").scale(1.5)
        eqnf.next_to(eqn,DOWN)
        self.play(ReplacementTransform(tbl,eqnf))
        self.wait()
        self.play(FadeOut(eqnf),FadeOut(eqn))
        self.wait()

class GeoImagination(Scene):
    def construct(self):
        eqn=TexMobject(r"{1\over1-r}=\sum_{n=0}^\infty r^n").scale(1.5)
        note=TextMobject("(Assume no limitations exist)").scale(0.7)
        note.next_to(eqn,DOWN)
        self.play(FadeIn(eqn))
        self.play(VFadeInThenOut(note))
        eqns=[
            TexMobject(r"{1\over1-(-1)}=\sum_{n=0}^\infty(-1)^n").scale(1.5),
            TexMobject(r"{1\over2}=1-1+1-1+1-1+\cdots").scale(1.5),
            TexMobject(r"{1\over4}=(1-1+1-1+1-1+\cdots)^2").scale(1.5),
            TexMobject(r"{1\over4}=\underbrace{1-2+3-4+5-6+7-8+\cdots}" \
                r"_{\text{Proved from the table}}").scale(1.5)
        ]
        for stuff in eqns:
            self.play(Transform(eqn,stuff))
            self.wait(2)
        self.play(FadeOut(eqn))
        self.wait()

class ManipulateScene(Scene):
    def construct(self):
        common_map={
            "{s}":PURPLE,
            "{2}":BLUE,"{4}":BLUE,"{6}":BLUE,"8":BLUE,"12":BLUE,"16":BLUE
        }
        eqn=TexMobject(r"{s}=1+{2}+3+{4}+5+{6}+7+8+9+\cdots",
            tex_to_color_map=common_map)
        eqn4s=TexMobject(r"4{s}={4}+8+12+16+\cdots",
            tex_to_color_map=common_map).scale(1.5)
        VGroup(eqn,eqn4s).arrange(DOWN)
        self.play(FadeIn(eqn))
        self.wait()
        self.play(Write(eqn4s))
        self.wait()
        eqnm0=TexMobject(r"{s}-4{s}=1+({2}-{4})+3+({4}-{8})+5" \
            r"+({6}-{12})+\cdots",tex_to_color_map=common_map)
        eqnm0.next_to(eqn4s,UP)
        self.play(FadeOut(eqn),ReplacementTransform(eqn4s,eqnm0))
        eqns=[
            TexMobject(r"-3{s}=1-2+3-4+5-6+7-8\cdots",
                tex_to_color_map={
                    "{s}":PURPLE,
                    "-2":GREEN,"-4":GREEN,"-6":GREEN,"-8":GREEN
            }).scale(1.5),
            TexMobject(r"-3{s}={1\over4}").scale(2),
            TexMobject(r"{s}=-{1\over12}").scale(2)
        ]
        self.wait()
        for stuff in eqns:
            self.play(Transform(eqnm0,stuff))
            self.wait()
        self.play(FadeOut(eqnm0))
        self.wait()

class ThanksScene(Scene):
    def construct(self):
        eqn=TexMobject(r"1+2+3+4+\cdots=-{1\over12}").scale(2).to_edge(UP)
        self.play(Write(eqn))
        # Now show acknowledgments
        author=TextMobject("@TravorLZH")
        author.set_color_by_gradient(RED,YELLOW)
        thanks=VGroup(TextMobject("Created by"),author).arrange(RIGHT)
        gp=VGroup(thanks,TextMobject(r"Powered by \LaTeX{} and manim",
            tex_to_color_map={
                r"\LaTeX{}":GREEN,
                "manim":BLUE
            })).arrange(DOWN).scale(1.5).to_edge(DOWN)
        self.play(FadeIn(gp))
        self.play(Write(TextMobject(r"This is why $\zeta(-1)$ is reasonable",
            tex_to_color_map={
                "This":GREEN,
                r"$\zeta(-1)$":PURPLE,
                "reasonable":YELLOW
            }).scale(1.8)))
        self.wait(10)
