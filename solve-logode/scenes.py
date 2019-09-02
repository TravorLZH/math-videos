from manimlib.imports import *

eqn_parts=[
    r"{dN\over d{t}}","=r",r"N\cdot{K-N\over K}"
]
eqn_explanations=[
    "Rate of N's change","is proportional to",
    r"$\Delta$ of N and K"
]
eqn_str="".join(eqn_parts)
func_str=r"N(t)={K\over 1+C_4e^{-rt}}"
last_str=r"N(t)={KN_0\over N_0+(K-N_0)e^{-rt}}"

class OpenningScene(Scene):
    def construct(self):
        title=TextMobject("How to solve logistic equation",
            tex_to_color_map={
                "How":YELLOW,
                "solve":GREEN,
                "logistic":ORANGE
            }).scale(2).to_edge(UP)
        eqn=TexMobject(eqn_str,
            tex_to_color_map={
                "N":ORANGE,
                "K":GREEN,
                "{t}":YELLOW
            }).scale(2.5)
        gp=VGroup(title,eqn)
        self.play(FadeIn(title))
        self.play(Write(eqn))
        self.wait()
        self.play(FadeOut(gp))
        self.wait()

class AnalyzeEqnScene(Scene):
    def construct(self):
        eqn=VGroup()
        for part in eqn_parts:
            eqn.add(TexMobject(part))
        eqn=eqn.arrange(RIGHT).scale(2)
        self.play(ShowCreation(eqn))
        for i,part in enumerate(eqn.submobjects):
            obj=TextMobject(eqn_explanations[i],color=YELLOW) \
                .next_to(part,DOWN).scale(1.5).to_edge(DOWN)
            self.add(obj)
            self.play(Indicate(part,part.copy()))
            self.remove(obj)
        self.wait()
        self.play(FadeOut(eqn))
        self.wait()

class SeparateEqnScene(Scene):
    def construct(self):
        eqn=TexMobject(eqn_str,
            tex_to_color_map={
                "N":ORANGE,
                "K":GREEN,
                "{t}":YELLOW,
            }).scale(2).to_edge(UP)
        self.play(Write(eqn))
        eqn_transformed=[
            r"{d}N=rN\cdot{K-N\over K}{d}{t}",
            r"{K\over N(K-N)}{d}N=r{d}{t}",
            r"\int {K\over N(K-N)}{d}N=\int r{d}{t}",
            r"\int {K\over N(K-N)}{d}N=r{t}+C_0"
        ]
        transfm_explan=[
            "Move $dt$ to the right",
            "Move all $N$ rid of the left",
            "Now we can integrate",
            "Right part is easier than the left"
        ]
        for i,txt in enumerate(eqn_transformed):
            eqn_new=TexMobject(txt,
                tex_to_color_map={
                    "{d}":PURPLE,
                    "N":ORANGE,
                    "K":GREEN,
                    "{t}":YELLOW,
                    r"\int":PURPLE
                }).scale(2).to_edge(UP)
            explan=TextMobject(transfm_explan[i],
                tex_to_color_map={
                    "left":BLUE,
                    "right":GREEN,"Right":GREEN,
                    "integrate":PURPLE
                }).scale(1.5)
            self.play(VFadeInThenOut(explan))
            self.play(Transform(eqn,eqn_new))
            self.wait()
        self.play(FadeOut(eqn))
        self.wait()

class IntegrateLeftScene(Scene):
    def construct(self):
        eqn=TexMobject("\int {K\over N(K-N)}{d}N",
            tex_to_color_map={
                "{d}":PURPLE,
                "N":ORANGE,
                "K":GREEN,
                "{t}":YELLOW,
                r"\int":PURPLE
            }).scale(1.5)
        self.play(FadeIn(eqn))
        partial_frac=TexMobject(r"{K\over N(K-N)}={1\over N}+{1\over K-N}") \
            .to_edge(LEFT).to_edge(TOP)
        ln_rule=TexMobject(r"\int{dx\over x}=\ln\lvert x\rvert+C") \
            .to_edge(RIGHT).to_edge(DOWN)
        eqn_new=[
            r"\int{{d}N\over N}+\int{{d}N\over K-N}",
            r"\ln\lvert N\rvert-\ln\lvert K-N\rvert+C_1",
            r"\ln\lvert{N\over K-N}\rvert+C_1"
        ]
        self.play(FadeIn(partial_frac))
        self.play(FadeIn(ln_rule))
        for stuff in eqn_new:
            new=TexMobject(stuff,
                tex_to_color_map={
                    "{d}":PURPLE,
                    "N":ORANGE,
                    "K":GREEN,
                    "{t}":YELLOW,
                    r"\int":PURPLE
                }).scale(1.5)
            self.play(Transform(eqn,new))
        no_neg1=TexMobject(r"\because 0<N<K")
        no_neg2=TexMobject(r"\lvert{N\over K-N}\rvert={N\over K-N}")
        noneg_gp=VGroup(no_neg1,no_neg2).arrange(DOWN).to_edge(LEFT) \
            .to_edge(DOWN)
        self.play(FadeIn(no_neg1))
        self.play(Write(no_neg2))
        eqn_final=TexMobject(r"\ln\left(N\over K-N\right)+C_1",
            tex_to_color_map={
                "N":ORANGE,
                "K":GREEN
            }).scale(1.5)
        everything=VGroup(partial_frac,ln_rule,noneg_gp,eqn)
        self.play(Transform(eqn,eqn_final))
        self.wait()
        self.play(FadeOut(everything))

class FindFuncScene(Scene):
    def construct(self):
        eqn=TexMobject(r"\ln\big({N\over K-N}\big)+C_1=rt+C_0",
            tex_to_color_map={
                "C_0":BLUE,
                "C_1":GREEN
            }).scale(2)
        self.play(FadeIn(eqn))
        eqn_new=[
            r"\ln\big({N\over K-N}\big)=rt+{C_2}",
            r"{N\over K-N}=e^{rt+C_2}",
            r"{N\over K-N}=C_3e^{rt}",
            "N=(K-N)C_3e^{rt}",
            "(1+C_3e^{rt})N=KC_3e^{rt}",
            r"N={KC_3e^{rt}\over 1+C_3e^{rt}}",
            r"N={K\over 1+{1\over C_3}e^{-rt}}",
            r"N={K\over 1+C_4e^{-rt}}"
        ]
        for stuff in eqn_new:
            new=TexMobject(stuff,
                tex_to_color_map={
                    "C_2}":YELLOW,
                    "C_3":ORANGE,
                    "C_4":PURPLE
                }).scale(2)
            self.play(Transform(eqn,new))
            self.wait()
        eqn_func=TexMobject(func_str,
            tex_to_color_map={
                "N":ORANGE,
                "K":GREEN
            }).scale(2)
        self.play(Transform(eqn,eqn_func))
        self.wait()
        self.play(FadeOut(eqn))
        self.wait()

class SolveC4Scene(Scene):
    def construct(self):
        func=TexMobject(func_str).scale(2)
        self.play(Write(func))
        becz_n0=TextMobject("Initial condition $N(0)=N_0$") \
            .to_edge(DOWN).scale(1.3)
        self.play(FadeIn(becz_n0))
        func_new=[
            r"N(0)={K\over 1+C_4}",
            r"N_0={K\over 1+C_4}",
            "N_0(1+C_4)=K",
            "N_0C_4=K-N_0",
            r"\therefore C_4={K-N_0\over N_0}"
        ]
        for f in func_new:
            new=TexMobject(f,
                tex_to_color_map={
                    "C_4":PURPLE,
                    "K":GREEN,
                    "N_0":ORANGE
                }).scale(2)
            self.play(Transform(func,new))
            self.wait()
        self.play(FadeOut(becz_n0))
        func_finals=[
            r"N(t)={K\over 1+C_4e^{-rt}}",
            r"N(t)={K\over 1+\left(K-N_0\over N_0\right)e^{-rt}}"
        ]
        for final in func_finals:
            f=TexMobject(final,
                tex_to_color_map={
                    "C_4":PURPLE
                }).scale(2)
            self.play(Transform(func,f))
            self.wait()
        last=TexMobject(last_str,
            tex_to_color_map={
                "N_0":ORANGE,
                "K":GREEN,
                "t":YELLOW
            }).scale(2)
        self.play(Transform(func,last))
        self.wait()
        self.play(Transform(func,last.copy().to_edge(DOWN)))
        # Now show the thanks messages
        created_by=TextMobject("Created by")
        author=TextMobject("@TravorLZH")
        author.set_color_by_gradient(RED,YELLOW)
        poweredby=TextMobject(r"Powered by \LaTeX{} and manim",
            tex_to_color_map={
                r"\LaTeX{}":GREEN,
                "manim":BLUE
            })
        thanks=VGroup(created_by,author).arrange(RIGHT)
        gp=VGroup(thanks,poweredby).arrange(DOWN).scale(1.8).to_edge(UP)
        self.play(ShowCreation(gp))
        eqn_name=TextMobject("The Logistic function",
            tex_to_color_map={
                "Logistic":ORANGE
            }).scale(1.5)
        self.play(Write(eqn_name))
        self.wait(20)
