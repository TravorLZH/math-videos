""" scenes.py: Source code of every scene is stored here """
from manimlib.imports import *
import numpy as np

class Openning(Scene):
    def construct(self):
        title=TextMobject("Collections of Calculus knowledge",
                tex_to_color_map={
                    "Collections":GREEN,
                    "Calculus":BLUE
                })
        comment=TextMobject("By @TravorLZH",
                tex_to_color_map={
                    "@TravorLZH":YELLOW
                })
        VGroup(comment,title).arrange(UP)
        self.play(ShowCreation(title))
        self.wait()
        self.play(Write(comment))
        self.wait()
        self.play(FadeOut(title),FadeOut(comment))
        self.wait()

class ShowFormula(Scene):
    def construct(self):
        formula=TexMobject("y=\\sin(x)")
        formula2=TexMobject("\\frac{dy}{dx}=\\frac{d}{dx}[\\sin(x)]",
                tex_to_color_map={
                    "\\frac{dy}{dx}":YELLOW,
                    "\\frac{d}{dx}[":YELLOW,
                    "]":YELLOW
                    })
        formula3=TexMobject("\\frac{dy}{dx}=\\cos(x)",
                tex_to_color_map={
                    "\\frac{dy}{dx}":YELLOW,
                    "\\cos":BLUE
                })
        formula4=TexMobject("\\frac{d^2y}{dx^2}=-\\sin(x)",
                tex_to_color_map={
                    "\\frac{d^2y}{dx^2}":RED,
                    "-\\sin":GREEN
                })
        self.play(Write(formula))
        self.wait()
        self.play(Transform(formula,formula2))
        self.wait()
        self.play(Transform(formula,formula3))
        self.wait()
        self.play(Transform(formula,formula4))
        self.wait()
        self.play(FadeOut(formula))
        self.wait()

class GraphStuff(GraphScene):
    CONFIG={
        "x_min": -10,
        "x_max": 10,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN,
    }

    def tangent_line(self,x):
        return np.cos(3)*(x-3)+np.sin(3)

    def tangent_line2(self,x):
        return -np.sin(3)*(x-3)+np.cos(3)

    def construct(self):
        self.setup_axes(animate=True)
        graph=self.get_graph(np.sin)
        label=self.get_graph_label(graph,label="\\sin(x)")
        self.play(ShowCreation(graph),Write(label))
        pt=Dot(self.coords_to_point(3,np.sin(3)))
        tangentline=self.get_graph(self.tangent_line)
        self.play(ShowCreation(tangentline))
        self.play(ShowCreation(pt))
        self.wait()
        # Now change sin(x) to cos(x) and the tangent line respectively
        graph2=self.get_graph(np.cos)
        label2=self.get_graph_label(graph2,"\\cos(x)")
        self.wait()
        pt2=Dot(self.coords_to_point(3,np.cos(3)))
        tangentline2=self.get_graph(self.tangent_line2)
        self.play(Transform(graph,graph2),Transform(label,label2),
                Transform(pt,pt2),Transform(tangentline,tangentline2))
        poweredby=TextMobject("Powered by \\LaTeX\\ and manim",
                tex_to_color_map={"manim":BLUE})
        author=TextMobject("Created by @TravorLZH",
                tex_to_color_map={"@TravorLZH":YELLOW})
        self.wait()
        VGroup(poweredby,author).arrange(UP)
        self.play(FadeOut(tangentline),FadeOut(graph),
                FadeOut(label),FadeOut(self.axes),FadeOut(pt))
        self.play(FadeIn(poweredby),Write(author))
        self.wait()
