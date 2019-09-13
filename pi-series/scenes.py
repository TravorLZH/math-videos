from manimlib.imports import *

class PiSeriesIntro(Scene):
    def construct(self):
        pi_logo=TexMobject(r"\pi",color=BLUE).scale(10)
        pi_title=TextMobject(r"How to create a series for",
            tex_to_color_map={
                "Create":GREEN,
                "series":YELLOW,
            }).scale(2)
        pi_gp=VGroup(pi_title,pi_logo).arrange(DOWN)
        self.play(Write(pi_title))
        self.play(FadeIn(pi_logo))
        self.wait()
        self.play(FadeOut(pi_gp))
        self.wait()

class ContentsScene(Scene):
    def construct(self):
        tit=Title("Contents")
        contents=VGroup(
            TextMobject("1. What is a series",
                tex_to_color_map={
                    "series":YELLOW
                }),
            TextMobject("2. What is a geometric series",
                tex_to_color_map={
                    "series":YELLOW
                }),
            TextMobject(r"3. Use series to represent $\arctan(x)$",
                tex_to_color_map={
                    "geometric":RED,
                    "series":YELLOW,
                    r"$\arctan(x)$":GREEN
                }),
            TextMobject(r"4. Represent $\pi$ by series",
                tex_to_color_map={
                    r"$\pi$":BLUE,
                    "series":YELLOW
                })).arrange(DOWN).scale(1.5)
        self.play(Write(tit))
        for obj in contents.submobjects:
            self.play(ShowCreation(obj))
            self.wait()
        self.play(FadeOut(contents),FadeOut(tit))
        self.wait()

class WhatIsSeries(Scene):
    def introduce_sequence(self):
        seq=TextMobject("Consider a sequence",
            tex_to_color_map={"sequence":ORANGE})
        seq_eqn=TexMobject(r"\{a_n\}").scale(2)
        seq_eqn2=TexMobject(r"\{a_0,a_1,a_2,a_3,\dots,a_n\}").scale(2)
        seq_gp=VGroup(seq,seq_eqn).arrange(DOWN).scale(1.5)
        self.play(Write(seq))
        self.play(FadeIn(seq_eqn))
        self.play(Transform(seq_eqn,seq_eqn2))
        self.wait()
        seq2=TextMobject("Now find the sum of it",
            tex_to_color_map={
                "sum":BLUE,"find":YELLOW
            })
        sum_eqn1=TexMobject("s_n")
        sum_eqn2=TexMobject(r"=a_0+a_1+a_2+a_2+\dots+a_n")
        sum_eqn=VGroup(sum_eqn1,sum_eqn2).arrange(RIGHT)
        sum_expln=TexMobject(r"\underbrace{}_\text{Partial sum}",
            tex_to_color_map={
                r"_\text{Partial":ORANGE,
                "sum}":BLUE
            }).scale(1.5)
        VGroup(seq2,sum_eqn).arrange(DOWN).scale(1.5)
        sum_expln.next_to(sum_eqn1,DOWN)
        self.play(Transform(seq,seq2))
        self.play(Transform(seq_eqn,sum_eqn))
        self.play(VFadeInThenOut(sum_expln))
        self.wait()
        # Show partial sum form
        ps_txt=TextMobject("Partial sum can be written as",
            tex_to_color_map={
                "Partial":ORANGE,
                "sum":BLUE,
                "written":GREEN
            })
        ps_eqn=TexMobject(r"s_n=\sum_{i=0}^na_n")
        ps=VGroup(ps_txt,ps_eqn).arrange(DOWN).scale(1.5)
        self.play(ReplacementTransform(seq,ps_txt))
        self.play(ReplacementTransform(seq_eqn,ps_eqn))
        self.wait()
        self.play(FadeOut(ps))
    def construct(self):
        tit=Title("What is a series")
        self.play(ShowCreation(tit))
        self.introduce_sequence()
        series_txt=TextMobject(r"It becomes a series if $n\to\infty$",
            tex_to_color_map={
                "becomes":RED,
                "series":YELLOW
            })
        series_eqn=TexMobject(r"s=\lim_{n\to\infty}s_n")
        series_eqn2=TexMobject(r"s=\sum_{i=0}^\infty a_n").scale(1.5)
        gp=VGroup(series_txt,series_eqn).arrange(DOWN).scale(1.5)
        series_eqn2.next_to(series_txt,DOWN)
        self.play(ShowCreation(gp))
        self.wait()
        self.play(Transform(series_eqn,series_eqn2))
        self.wait(2)
        self.play(FadeOut(gp),FadeOut(series_eqn2))
        self.play(FadeOut(tit))
        self.wait()

class GeoSeriesScene(Scene):
    def construct(self):
        tit=Title("Geometric Series")
        self.play(ShowCreation(tit))
        gs_tit=TextMobject("Geometric series is defined by",
            tex_to_color_map={
                "series":YELLOW,
                "defined":GREEN
            })
        gs_eqn=TexMobject(r"s=\sum_{i=0}^\infty{a}x^i")
        VGroup(gs_tit,gs_eqn).arrange(DOWN).scale(1.5)
        self.play(Write(gs_tit))
        self.play(FadeIn(gs_eqn))
        gs_eqn_new=[
            r"s_n=a+ax+ax^2+ax^3+\dots+ax^n",
            r"xs_n=ax+ax^2+ax^3+\dots+ax^{n+1}",
            r"xs_n=\underbrace{a+ax+ax^2+\dots+ax^n}" \
                r"_{\text{This is basically }s_n}+ax^{n+1}-a",
            r"xs_n=s_n+ax^{n+1}-a",
            r"(x-1)s_n=a(x^{n+1}-1)",
            r"s_n={a(x^{n+1}-1)\over x-1}"
        ]
        gs_instructions=[
            "Expand the whole thing",
            "Multiply everything by $x$",
            "Fabricate $s_n$ in the expression",
            "Simplify them with $s_n$",
            "Move $s_n$ to the left",
            "Now eliminate the factor"
        ]
        ps_tit=TextMobject("Now find the partial sums",
            tex_to_color_map={
                "find":BLUE,
                "partial":ORANGE
            }).scale(1.5)
        ps_tit.next_to(gs_eqn,UP)
        inst=TextMobject(gs_instructions[0]).to_edge(DOWN)
        self.play(ReplacementTransform(gs_tit,ps_tit))
        self.wait(2)
        self.play(ShowCreation(inst))
        for i,eqn in enumerate(gs_eqn_new):
            if i>0:
                inst_new=TextMobject(gs_instructions[i]).to_edge(DOWN)
                self.play(Transform(inst,inst_new))
            txt=TexMobject(eqn).scale(1.3)
            txt.next_to(ps_tit,DOWN)
            self.wait(2)
            self.play(Transform(gs_eqn,txt))
        self.play(FadeOut(inst))
        self.wait()
        inf_tit=TextMobject(r"Geometric series is when $n\to\infty$",
            tex_to_color_map={"series":YELLOW}).scale(1.5)
        inf_tit.next_to(gs_eqn,UP)
        self.play(Transform(ps_tit,inf_tit))
        inf_eqn=TexMobject(r"s=\lim_{n\to\infty}{a(1-x^{n+1})\over 1-x}") \
            .scale(1.5)
        inf_eqn.next_to(inf_tit,DOWN)
        note=TextMobject("Only true if $|x|<1$").scale(2).to_edge(DOWN)
        self.play(Transform(gs_eqn,inf_eqn))
        self.wait()
        self.play(VFadeInThenOut(note))
        final_eqn=TexMobject(r"s={a\over1-x}").scale(2)
        final_eqn.next_to(ps_tit,DOWN)
        self.play(Transform(gs_eqn,final_eqn))
        self.wait()
        self.play(FadeOut(gs_eqn),FadeOut(tit),FadeOut(ps_tit))
        self.wait()

class ArctanSeriesScene(Scene):
    def arctan_deriv(self):
        eqn=TexMobject(r"y=\arctan(x)").scale(2)
        d_tit=TextMobject(r"Differentiate $\arctan(x)$",
            tex_to_color_map={
                "Differentiate":YELLOW
            }).scale(1.5)
        VGroup(d_tit,eqn).arrange(DOWN)
        self.play(Write(d_tit))
        self.play(FadeIn(eqn))
        eqn_new=[
            r"\tan(y)=x",
            r"{d\over dx}\tan(y)={d\over dx}x",
            r"{1\over\cos^2(y)}{dy\over dx}=1",
            r"{dy\over dx}=\cos^2(y)",
            r"{dy\over dx}={\cos^2(y)\over1}",
            r"{dy\over dx}={\cos^2(y)\over\sin^2(y)+\cos^2(y)}",
            r"{dy\over dx}={1\over{\sin^2(y)\over\cos^2(y)}+1}",
            r"{dy\over dx}={1\over\tan^2(y)+1}",
            r"{dy\over dx}={1\over x^2+1}"
        ]
        for new in eqn_new:
            new_eqn=TexMobject(new,
                tex_to_color_map={
                    r"{d\over dx}":YELLOW,
                    r"{dy\over dx}":GREEN
                }).scale(2)
            new_eqn.next_to(d_tit,DOWN)
            self.wait()
            self.play(Transform(eqn,new_eqn))
    def construct(self):
        tit=Title(r"Use series to represent arc tangent")
        self.play(ShowCreation(tit))
        self.arctan_deriv()
