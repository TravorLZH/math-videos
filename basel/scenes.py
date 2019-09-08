from manimlib.imports import *
import numpy as np
from math import factorial

class BaselIntroScene(Scene):
    def construct(self):
        tit=TextMobject("How to solve the Basel problem",
            tex_to_color_map={
                "How":YELLOW,
                "solve":BLUE,
                "Basel":ORANGE
            }).scale(1.5)
        basel_eqn=TexMobject(r"\sum_{n=1}^\infty{1\over n^2}=?",
            tex_to_color_map={
                r"?":ORANGE
            }).scale(2)
        gp=VGroup(tit,basel_eqn).arrange(DOWN)
        self.play(FadeIn(tit))
        self.play(Write(basel_eqn))
        self.wait()
        self.play(FadeOut(gp))

class ExpandSineScene(GraphScene):
    CONFIG={
        "x_min":-10,
        "x_max":10,
        "y_min":-6,
        "y_max":6,
        "graph_origin":ORIGIN
    }
    @staticmethod
    def calc_tex(n):
        result="-" if n%2 else "+"
        tmp=2*n+1
        result+=r"{x^{%d}\over%d!}" % (tmp,tmp)
        return result
    def make_label(self):
        result="y=x"
        for i in range(1,self.n):
            result+=self.calc_tex(i)
        return result
    @staticmethod
    def calc_coeff(n):
        return (-1)**n/factorial(2*n+1)
    def maclaurin_sin(self,x):
        result=0
        for i in range(self.n):
            result+=self.calc_coeff(i)*(x**(2*i+1))
        return result
    def make_func(self):
        px_graph=self.get_graph(self.maclaurin_sin,color=YELLOW)
        px_label=self.get_graph_label(px_graph,self.make_label()).to_edge(DOWN)
        return (px_graph,px_label)
    def show_maclaurin(self):
        px_graph,px_label=self.make_func()
        self.play(Write(px_label))
        self.play(ShowCreation(px_graph))
        self.wait()
        for i in range(4,8):
            self.n=i
            graph,label=self.make_func()
            self.play(Transform(px_label,label))
            self.play(Transform(px_graph,graph))
            self.wait()
        self.play(FadeOut(px_label),FadeOut(px_graph))
    def show_inf_products(self):
        self.proof=TexMobject(r"\exists {m}\in\mathbb{Z}",
            tex_to_color_map={
                r"\exists":YELLOW,
                r"{m}":RED,
                r"\mathbb{Z}":GREEN
            })
        self.proof2=TexMobject(r"\therefore\sin (m\pi)=0",
            tex_to_color_map={
                r"\sin":BLUE,
                r"m":RED
            }).to_edge(LEFT).to_edge(DOWN)
        self.proof.next_to(self.proof2,UP)
        self.dots=VGroup()
        for i in range(-3,3+1):
            self.dots.add(Dot(self.coords_to_point(i*np.pi,0)))
        self.play(FadeIn(self.proof))
        self.play(Write(self.proof2))
        self.play(FadeIn(self.dots))
        self.wait()
    @staticmethod
    def sinx_x(x):
        result=0
        for i in range(20):
            result+=ExpandSineScene.calc_coeff(i)*(x**(2*i))
        return result
    def qx(self,x):
        result=1
        for i in range(1,self.n+1):
            result*=1-x**2/(i*(np.pi**2))
        return result
    def qx_label(self):
        result="y="
        for i in range(1,self.n+1):
            result+=r"\left(1-{x^2\over%s\pi^2}\right)" \
                % ("" if i==1 else str(i**2))
        return result
    def get_qx(self):
        graph=self.get_graph(self.qx,color=YELLOW)
        label=self.get_graph_label(graph,self.qx_label()).to_edge(UP) \
            .scale(0.8)
        return (graph,label)
    def show_qx(self):
        self.n=1
        graph=self.get_graph(self.qx,color=YELLOW)
        label=self.get_graph_label(graph,r"y=(1-{x\over\pi})(1+{x\over\pi})") \
            .to_edge(UP)
        self.play(Write(label))
        self.play(ShowCreation(graph))
        for i in range(2,4+1):
            self.n=i
            g,l=self.get_qx()
            self.play(Transform(label,l))
            self.play(Transform(graph,g))
        self.wait()
        self.play(FadeOut(graph),FadeOut(label))
        self.wait()
    def construct(self):
        self.setup_axes(animate=True)
        self.n=3
        sinx_graph=self.get_graph(np.sin,color=BLUE)
        sinx_label=self.get_graph_label(sinx_graph,r"\sin(x)")
        self.play(ShowCreation(sinx_graph),FadeIn(sinx_label))
        self.wait()
        self.show_maclaurin()
        sinx_label2=self.get_graph_label(sinx_graph,
            r"\sin(x)=x-{x^3\over3!}+{x^5\over5!}-\dots").to_edge(DOWN)
        self.play(Transform(sinx_label,sinx_label2))
        self.wait()
        self.show_inf_products()
        self.wait()
        sinx_x_graph=self.get_graph(self.sinx_x,color=GREEN)
        sinx_x_label=self.get_graph_label(sinx_x_graph,
            r"{\sin(x)\over x}=1-{x^2\over3!}+{x^4\over5!}-\dots") \
                .to_edge(DOWN)
        sinx_x_label2=self.get_graph_label(sinx_x_graph,
            r"p(x)=1-{x^2\over3!}+{x^4\over5!}-\dots").to_edge(DOWN)
        self.play(ReplacementTransform(sinx_label,sinx_x_label))
        self.play(Transform(sinx_x_label,sinx_x_label2))
        self.play(ReplacementTransform(sinx_graph,sinx_x_graph))
        self.wait()
        self.play(Transform(self.proof,
            TexMobject(r"\exists{m}\in\mathbb{Z}\cap{m}\ne0",
                tex_to_color_map={
                    r"\exists":YELLOW,
                    r"{m}":RED,
                    r"\mathbb{Z}":GREEN
                }).next_to(self.proof2,UP)))
        self.play(Transform(self.proof2,
            TexMobject(r"\therefore {p}(m\pi)=0",
                tex_to_color_map={
                    "{p}":GREEN,
                    "m":RED
                }).to_edge(LEFT).to_edge(DOWN)))
        p0_1=TexMobject(r"p(0)=1").next_to(sinx_x_label,UP)
        self.play(FadeIn(p0_1),Transform(self.dots.submobjects[3],
            Dot(self.coords_to_point(0,1))))
        self.wait()
        self.show_qx()
        everything=VGroup(self.axes,sinx_x_label,sinx_x_graph,self.dots,
            p0_1,self.proof,self.proof2)
        self.play(FadeOut(everything))
        self.wait()

class AnalyzeProductScene(Scene):
    def construct(self):
        product_str=r"p(x)=(1-{x^2\over\pi^2})(1-{x^2\over4\pi^2})\dots"
        product_eqn=TexMobject(product_str,
            tex_to_color_map={
                "{x^2":YELLOW
            }).scale(2)
        sum_eqn=TexMobject(r"p(x)=1-{x^2\over3!}+{x^4\over5!}-\dots",
            tex_to_color_map={
                r"{x^2\over3!}":YELLOW},color=GREEN).scale(2)
        sum_eqn.next_to(product_eqn,DOWN)
        self.play(Write(sum_eqn))
        self.wait()
        self.play(FadeIn(product_eqn))
        self.wait()
        prod_eqn2=TexMobject(
            r"p(x)=1-\left({1\over\pi^2}+{1\over4\pi^2}+" \
                r"{1\over9\pi^2}+\dots\right)x^2+(\cdots)x^4+\cdots",
            tex_to_color_map={
                "p(x)=1-":WHITE,
                r"+(\cdots)x^4+\cdots":WHITE
            },color=YELLOW)
        self.play(Transform(product_eqn,prod_eqn2))
        self.wait()
        self.play(FadeOut(product_eqn),FadeOut(sum_eqn))
        self.wait()

class DerivationScene(Scene):
    def construct(self):
        eqn=TexMobject(r"{1\over3!}={1\over\pi^2}+{1\over4\pi^2}+" \
            r"{1\over9\pi^2}+\cdots").scale(1.8)
        eqn_deriv=[
            r"{1\over3!}={1\over\pi^2}\left(1+\frac14+\frac19+\frac1{16}" \
                r"+\cdots\right)",
            r"\frac16={1\over\pi^2}\left(1+\frac14+\frac19+\frac1{16}" \
                r"+\cdots\right)",
            r"{\pi^2\over6}=1+\frac14+\frac19+\frac1{16}+\cdots",
        ]
        self.play(Write(eqn))
        for stuff in eqn_deriv:
            self.play(Transform(eqn,TexMobject(stuff).scale(1.8)))
            self.wait()
        eqn_last=TexMobject(r"\sum_{n=1}^\infty{1\over n^2}={\pi^2\over6}") \
            .scale(2).to_edge(UP)
        self.play(Transform(eqn,eqn_last))
        self.wait()
        created_by=TextMobject("Created by")
        author=TextMobject("@TravorLZH")
        author.set_color_by_gradient(RED,YELLOW)
        poweredby=TextMobject(r"Powered by \LaTeX{} and manim",
            tex_to_color_map={
                r"\LaTeX{}":GREEN,
                "manim":BLUE
            })
        thanks=VGroup(created_by,author).arrange(RIGHT)
        gp=VGroup(thanks,poweredby).arrange(DOWN).scale(1.8).to_edge(DOWN)
        self.play(ShowCreation(gp))
        solution=TextMobject("The solution to the Basel problem",
            tex_to_color_map={
                "solution":GREEN,
                "Basel":ORANGE
            }).scale(1.5)
        self.play(Write(solution))
        self.wait(20)
