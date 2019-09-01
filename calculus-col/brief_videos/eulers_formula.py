from manimlib.imports import *
import numpy as np
import math

class EulersFormulaScene(GraphScene):
    CONFIG={
        "x_min":-8,
        "x_max":8,
        "y_min":-5,
        "y_max":5,
        "graph_origin":ORIGIN,
        "n":1
    }
    def polynomial_exp(self,x):
        y=0.0
        for i in range(self.n+1):
            y+=np.power(x,i)/math.factorial(i)
        return y
    def do_title(self):
        title=TextMobject("Algebraic proof of Euler's formula",
            tex_to_color_map={
                "Algebraic":BLUE,
                "Euler's":GREEN
            }).scale(1.5)
        formula=TexMobject("e^{i\\pi}+1=0",
            tex_to_color_map={
                "^{i":RED,
                "\\pi}":YELLOW,
                "+1":BLUE,
                "0":GREEN
            }).scale(2.0)
        VGroup(formula,title).arrange(UP)
        self.play(FadeIn(title))
        self.play(Write(formula))
        self.wait()
        self.play(FadeOut(title),FadeOut(formula))
    def update_graph(self):
        graph=self.get_graph(self.polynomial_exp,color=YELLOW)
        label=self.get_graph_label(graph,
            "p(x)=\\sum_{n=0}^{%d}\\frac{x^n}{n!}" % self.n)
        gp=VGroup(self.func_label.copy(),label).arrange(DOWN).to_edge(RIGHT) \
            .to_edge(DOWN)
        self.play(Transform(self.polynomial_graph,graph),
            Transform(self.gp,gp))

    def maclaurin_expand_exp(self):
        self.setup_axes(animate=True)
        self.func_graph=self.get_graph(np.exp,color=GREEN)
        self.func_label=self.get_graph_label(self.func_graph,"f(x)=e^x")
        self.polynomial_graph=self.get_graph(self.polynomial_exp,color=YELLOW)
        self.polynomial_label=self.get_graph_label(self.polynomial_graph,
            "p(x)=x")
        self.gp=VGroup(self.func_label,self.polynomial_label).arrange(DOWN) \
            .to_edge(RIGHT).to_edge(DOWN)
        self.play(ShowCreation(self.func_graph))
        self.wait()
        self.play(ShowCreation(self.polynomial_graph))
        self.play(ShowCreation(self.gp))
        for i in range(4+1):
            self.wait()
            self.n+=3
            self.update_graph()
        self.wait()
        self.play(FadeOut(self.gp),FadeOut(self.func_graph),
            FadeOut(self.polynomial_graph),FadeOut(self.axes))
        self.wait()
        summary=TexMobject("{e}^x=\\sum_{n=0}^\\infty{{x}^n\\over n!}",
            tex_to_color_map={"^x":YELLOW,"{x}":YELLOW})
        summary2=TexMobject("{e}^x=1+{x}+{x^2\\over 2!}+{x^3\\over 3!}" \
            "+{x^4\\over 4!}+\\dots",
            tex_to_color_map={"^x":YELLOW,"{x":YELLOW})
        self.play(Write(summary))
        self.wait()
        self.play(Transform(summary,summary2))
        self.wait()
        self.play(FadeOut(summary))
        self.wait()
    def maclaurin_sin_cos(self):
        title=TextMobject("Similarly, there also exists:",
            tex_to_color_map={
                "also":YELLOW
            })
        sin_formula=TexMobject("\\sin(x)=x-{x^3\\over 3!}+{x^5\\over 5!}" \
            "-{x^7\\over 7!}+{x^9\\over 9!}-\\dots",color=GREEN)
        cos_formula=TexMobject("\\cos(x)=1-{x^2\\over 2!}+{x^4\\over 4!}" \
            "-{x^6\\over 6!}+{x^8\\over 8!}-\\dots",color=BLUE)
        VGroup(cos_formula,sin_formula,title).arrange(UP)
        self.play(FadeIn(title))
        self.wait()
        self.play(Write(sin_formula),Write(cos_formula))
        self.wait()
        self.play(FadeOut(title),FadeOut(sin_formula),FadeOut(cos_formula))
        self.wait()
    def plug_in_exp_ix(self):
        exp_ix=TexMobject("\\therefore e^{ix}=1+ix-{x^2\\over 2!}" \
            "-{ix\\over x^3}+{x^4\\over 4!}+{ix^5\\over 5!}-\\dots",
            tex_to_color_map={
                "1":BLUE,
                "^{i":RED,
                "+ix":GREEN,
                "-{x^2\\over 2!}":BLUE,
                "-{ix\\over x^3}":GREEN,
                "+{x^4\\over 4!}":BLUE,
                "+{ix^5\\over 5!}":GREEN,
            })
        exp_ix2=TexMobject("\\therefore e^{ix}=(1-{x^2\\over 2!}" \
            "+{x^4\\over 4!}-\\dots)+{i}\\cdot(x-{x^3\\over 3!}" \
            "+{x^5\\over 5!}-\\dots)",
            tex_to_color_map={
                "(1-{x^2\\over 2!}+{x^4\\over 4!}-\\dots)":BLUE,
                "(x-{x^3\\over 3!}+{x^5\\over 5!}-\\dots)":GREEN,
                "^i":RED,
                "i":RED
            })
        exp_ix3=TexMobject("\\therefore e^{ix}=\\cos(x)+{i}\\sin(x)",
            tex_to_color_map={
                "^{i":RED,
                "{i}":RED,
                "\\cos":BLUE,
                "\\sin":GREEN,
                "x":WHITE
            })
        x_is_pi=TexMobject("\\because x=\\pi",tex_to_color_map={"\\pi":YELLOW})
        exp_ipi=TexMobject("\\therefore e^{i\\pi}=\\cos(\\pi)+{i}\\sin(\\pi)",
            tex_to_color_map={
                "^{i":RED,
                "{i}":RED,
                "\\cos":BLUE,
                "\\sin":GREEN,
                "\\pi":YELLOW
            })
        exp_ipi2=TexMobject("\\therefore e^{i\\pi}=-1+0",
            tex_to_color_map={
                "^{i":RED,
                "-1":BLUE,
                "0":GREEN,
                "\\pi}":YELLOW
            })
        exp_ipi3=TexMobject("\\therefore e^{i\\pi}+1=0",
            tex_to_color_map={
                "^{i":RED,
                "\\pi}":YELLOW,
                "+1":BLUE,
                "0":GREEN
            })
        self.gp=VGroup(exp_ipi3,exp_ipi,x_is_pi).arrange(UP)
        self.play(Write(exp_ix))
        self.wait()
        self.play(Transform(exp_ix,exp_ix2))
        self.wait()
        self.play(Transform(exp_ix,exp_ix3))
        self.wait()
        self.play(FadeOut(exp_ix))
        self.wait()
        self.play(Write(x_is_pi),Write(exp_ipi))
        self.wait()
        self.play(Transform(exp_ipi,exp_ipi2))
        self.play(Write(exp_ipi3))
        self.wait()
    def thanks(self):
        thanks=TextMobject("Created by @TravorLZH",
            tex_to_color_map={
                "@TravorLZH":YELLOW
            })
        poweredby=TextMobject("Powered by \\LaTeX{} and manim",
            tex_to_color_map={
                "manim":BLUE
            })
        VGroup(poweredby,thanks).arrange(UP).to_edge(RIGHT)
        self.play(Transform(self.gp,self.gp.copy().to_edge(LEFT)),
            Write(thanks),FadeIn(poweredby))
        self.wait()
    def construct(self):
        self.do_title()
        self.maclaurin_expand_exp()
        self.maclaurin_sin_cos()
        self.plug_in_exp_ix()
        self.thanks()
        self.wait(5)
