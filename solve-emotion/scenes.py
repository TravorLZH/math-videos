from manimlib.imports import *

eqn_str=r"\lim_{x\to 0}{x^2\over" \
        r"\text{ln}(\int_0^{\sqrt[3]{x^2}}e^{\frac12t^2}dt+1" \
        r"-x^{\frac23})}"

eqn_str2=r"\lim_{x\to 0}{x^2\over" \
        r"\text{ln}(\int_0^{\sqrt[3]{x^2}}(1+\frac12t^2)dt+1" \
        r"-x^{\frac23})}"

eqn_str3=r"\lim_{x\to 0}{x^2\over" \
        r"\text{ln}[(x^{\frac23}+\frac16x^2)+1-x^{\frac23}]}"

class OpenningEmotion(Scene):
    def construct(self):
        tit=TextMobject("Solve")
        emo=ImageMobject("666.jpg").scale(2)
        gp=Group(tit,emo).arrange(DOWN)
        self.play(Write(tit))
        self.wait()
        self.play(FadeIn(emo))
        self.wait()
        self.play(FadeOut(gp))

class ExpandFuncScene(GraphScene):
    CONFIG={
        "x_min":-2,
        "x_max":2,
        "y_min":-1,
        "y_max":3,
        "graph_origin":ORIGIN
    }
    @staticmethod
    def func(x):
        return np.exp(0.5*x**2)
    @staticmethod
    def func_approx(x):
        return 1+0.5*x**2
    @staticmethod
    def func_diff(x):
        return ExpandFuncScene.func(x)/ExpandFuncScene.func_approx(x)
    def construct(self):
        eqn=TexMobject(eqn_str)
        eqn2=TexMobject(eqn_str,
            tex_to_color_map={
                r"e^{\frac12t^2}":YELLOW
            }).to_edge(LEFT).to_edge(DOWN)
        self.play(Write(eqn))
        self.play(Transform(eqn,eqn2))
        self.setup_axes(animate=True)
        f_graph=self.get_graph(self.func,color=YELLOW)
        f_label=self.get_graph_label(f_graph,r"y_1=e^{\frac12x^2}")
        fa_graph=self.get_graph(self.func_approx,color=BLUE)
        fa_label=self.get_graph_label(fa_graph,r"y_2=1+\frac12x^2")
        VGroup(f_label,fa_label).arrange(DOWN).to_edge(RIGHT).to_edge(UP)
        self.play(ShowCreation(f_graph),Write(f_label))
        self.wait()
        self.play(ShowCreation(fa_graph),Write(fa_label))
        self.wait()
        graph_gp=VGroup(self.axes,f_graph,f_label,fa_graph,
            fa_label)
        # Now show the difference of functions
        x=1.5
        y=self.func_diff(x)
        diff_format= \
                r"x=%f \\ {y_1 \over y_2}=%f"
        diff_func=TexMobject(diff_format % (x,y),
            tex_to_color_map={
                "%f" % x:RED,
                "y_1":YELLOW,
                "y_2":BLUE,
                "%f" % y:GREEN
            }).to_edge(RIGHT).to_edge(DOWN)
        self.play(FadeIn(diff_func))
        for x in reversed(np.arange(0.25,1.5,0.25)):
            y=self.func_diff(x)
            diff_func_new=TexMobject(diff_format % (x,y),
                tex_to_color_map={
                    "%f" % x:RED,
                    "y_1":YELLOW,
                    "y_2":BLUE,
                    "%f" % y:GREEN
                }).to_edge(RIGHT).to_edge(DOWN)
            self.play(Transform(diff_func,diff_func_new))
        diff_func_new=TexMobject(r"x\to 0 \\ {y_1 \over y_2} \to 1",
            tex_to_color_map={
                r"\to 0":RED,
                "y_1":YELLOW,
                "y_2":BLUE,
                r"\to 1":GREEN
            }).to_edge(RIGHT).to_edge(DOWN)
        self.play(Transform(diff_func,diff_func_new))
        # Show the prove of equivalent infinitesimal
        limit_eqn=TexMobject(
            r"\because \lim_{x\to 0}{e^{\frac12x^2}\over 1+\frac12x^2}=1",
            tex_to_color_map={
                r"_{x\to 0}":RED,
                r"e^{\frac12x^2}":YELLOW,
                r"1+\frac12x^2":BLUE
            })
        equiv_infsimal=TexMobject(r"\therefore e^{\frac12x^2} \sim 1+\frac12x^2",
            tex_to_color_map={
                r"e^{\frac12x^2}":YELLOW,
                r"1+\frac12x^2":BLUE
            })
        proof_gp=VGroup(limit_eqn,equiv_infsimal).arrange(DOWN).to_edge(RIGHT) \
            .to_edge(DOWN)
        self.play(ReplacementTransform(diff_func,limit_eqn))
        self.wait()
        self.play(Write(equiv_infsimal))
        # Now hide the graph and change the integral
        self.wait()
        self.play(FadeOut(graph_gp),FadeOut(proof_gp))
        eqn_new=TexMobject(eqn_str2,
            tex_to_color_map={
                r"(1+\frac12t^2)":BLUE
            })
        self.play(Transform(eqn,eqn_new))
        self.wait()
        self.play(FadeOut(eqn))
        self.wait()

class ExpandIntegralScene(Scene):
    def construct(self):
        integral_fml=TexMobject(r"\int^{\sqrt[3]{x^2}}_0(1+\frac12{t}^2)dt",
            tex_to_color_map={
                r"^{\sqrt[3]{x^2}}_0":YELLOW,
                "{t}":GREEN,
                "dt":GREEN
            })
        integral_steps=[
            r"\left[{t}+\frac16{t}^3\right]^{\sqrt[3]{x^2}}_0",
            r"{x}^{\frac23}+\frac16{x}^2"
        ]
        self.play(Write(integral_fml))
        for step in integral_steps:
            integral_fml_new=TexMobject(step,
                tex_to_color_map={
                    "{t}":GREEN,
                    r"^{\sqrt[3]{x^2}}_0":YELLOW,
                    "{x}":YELLOW
                })
            self.play(Transform(integral_fml,integral_fml_new))
        self.play(FadeOut(integral_fml))
        self.wait()

class SolveEverythingScene(Scene):
    def construct(self):
        eqn=TexMobject(eqn_str3).scale(1.2)
        self.play(Write(eqn))
        self.wait()
        eqn_simp=TexMobject(r"\lim_{x\to 0}{x^2\over" \
            r" \text{ln}(1+\frac16x^2)}").scale(1.2)
        self.play(Transform(eqn,eqn_simp))
        self.wait()
        # Now show the proof of indeterminate form
        numer_zero=TexMobject(r"\because\lim_{x\to 0}x^2={0}",
            tex_to_color_map={"{0}":RED})
        denom_zero=TexMobject(r"\because\lim_{x\to 0}\ln(1+\frac16x^2)={0}",
            tex_to_color_map={"{0}":RED})
        indeterm=TexMobject(r"\therefore \text{Indeterminate }\frac00\text{!}",
            tex_to_color_map={r"\frac00":RED})
        indet_gp=VGroup(numer_zero,denom_zero,indeterm).arrange(DOWN) \
            .to_edge(RIGHT).to_edge(DOWN).scale(0.7)
        self.play(FadeIn(numer_zero))
        self.play(FadeIn(denom_zero))
        self.play(FadeIn(indeterm))
        self.wait()
        # Show the statements of L'Hopital's Rule
        lhop=TextMobject("Apply L'Hopital's Rule:",
            tex_to_color_map={"L'Hopital's":ORANGE,"Rule":GREEN})
        lhop_def=TexMobject(r"\exists\lim_{x\to c}{f(x)\over g(x)}=\frac00",
            tex_to_color_map={"f(x)":ORANGE,"g(x)":BLUE,r"\frac00":RED})
        lhop_def2=TexMobject(r"\therefore \lim_{x\to c}{f(x)\over g(x)}" \
            r"=\lim_{x\to c}{f'(x)\over g'(x)}",
            tex_to_color_map={
                "{f(x)":ORANGE,"g(x)}":BLUE,"{f'(x)":YELLOW,"g'(x)}":GREEN
            })
        lhop_gp=VGroup(lhop,lhop_def,lhop_def2).arrange(DOWN) \
            .to_edge(LEFT).to_edge(UP).scale(0.7)
        self.play(FadeIn(lhop))
        self.play(FadeIn(lhop_def))
        self.play(FadeIn(lhop_def2))
        self.wait()
        # Now differentiate x^2
        d_x2=TexMobject(r"\frac{d}{dx}x^2=2x",
            tex_to_color_map={
                r"\frac{d}{dx}":YELLOW,
                "2x":PURPLE
            }).to_edge(0.5*RIGHT).to_edge(0.5*UP)
        self.play(ShowCreation(d_x2))
        # Also differentiate ln(1+x^2/6)
        d_lnx=TexMobject(r"\frac{d}{dx}\ln(1+\frac16x^2)=",
            tex_to_color_map={r"\frac{d}{dx}":YELLOW})
        d_lnx2=TexMobject(r"{\frac{d}{dx}[1+\frac16x^2]\over 1+\frac16x^2}=",
            tex_to_color_map={r"{\frac{d}{dx}":YELLOW})
        d_lnx3=TexMobject(r"\frac13x\over 1+\frac16x^2",color=GREEN)
        d_lnx_gp=VGroup(d_lnx,d_lnx2,d_lnx3).arrange(DOWN).scale(0.7) \
            .to_edge(LEFT).to_edge(DOWN)
        self.play(ShowCreation(d_lnx))
        self.play(ShowCreation(d_lnx2))
        self.play(ShowCreation(d_lnx3))
        self.wait()
        # Create this group to make fading everything out possible
        all_gp=VGroup(d_lnx_gp,d_x2,lhop_gp,indet_gp)
        # Now plug the derivatives in
        eqn_lhop=TexMobject(r"\lim_{x\to 0}{2x\over" \
            r"{\frac13x\over 1+\frac16x^2}}",
            tex_to_color_map={
                r"{\frac13x\over 1+\frac16x^2}}":GREEN,
                "2x":PURPLE
            })
        eqn_lhop2=TexMobject(r"\lim_{x\to 0}{{2}\over" \
            r"{\frac13\over 1+\frac16x^2}}",
            tex_to_color_map={
                "{2}":PURPLE,
                r"{\frac13\over 1+\frac16x^2}":GREEN
            })
        eqn_final=TexMobject(r"6\over {1\over 1+\frac160^2}",
            tex_to_color_map={
                "0":RED,
            })
        eqn_answer=TexMobject("6",color=YELLOW).scale(2)
        self.play(Transform(eqn,eqn_lhop))
        self.play(Transform(eqn,eqn_lhop2))
        self.play(Transform(eqn,eqn_final))
        self.play(Transform(eqn,eqn_answer),FadeOut(all_gp))
        self.wait()
        self.play(FadeOut(eqn_answer))

class ThanksScene(Scene):
    def construct(self):
        # Now show the hint in the picture
        hint_pic=ImageMobject("666_thuglife.png").scale(2)
        self.play(FadeIn(hint_pic))
        # Also show my name
        author=TextMobject("Created by @TravorLZH").to_edge(UP)
        author.set_color_by_gradient(RED,GREEN)
        poweredby=TextMobject("Powered by \\LaTeX{} and manim",
            tex_to_color_map={
                "\\LaTeX{}":GREEN,
                "manim":BLUE
            }).to_edge(DOWN)
        gp=VGroup(author,poweredby)
        self.play(FadeIn(gp))
        self.wait(10)
