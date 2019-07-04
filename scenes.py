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
        func_formula=TexMobject("y=\\sin(x)")
        func_comment=TextMobject("Original Function sin(x)",
            tex_to_color_map={
                "sin":GREEN
            })
        deriv_formula=TexMobject("\\frac{dy}{dx}=\\frac{d}{dx}[\\sin(x)]",
            tex_to_color_map={
                "\\frac{dy}{dx}":YELLOW,
                "\\frac{d}{dx}[":YELLOW,
                "]":YELLOW
            })
        formulas=[
            TexMobject("\\frac{dy}{dx}=\\cos(x)",
                tex_to_color_map={
                    "\\frac{dy}{dx}":YELLOW,
                    "\\cos":BLUE
                }),
            TexMobject("\\frac{d^2y}{dx^2}=-\\sin(x)",
                tex_to_color_map={
                    "\\frac{d^2y}{dx^2}":RED,
                    "-\\sin":GREEN
                }),
            TexMobject("\\frac{d^3y}{dx^3}=-\\cos(x)",
                tex_to_color_map={
                    "\\frac{d^3y}{dx^3}":ORANGE,
                    "-\\cos":BLUE
                }),
            TexMobject("\\frac{d^4y}{dx^4}=\\sin(x)",
                tex_to_color_map={
                    "\\frac{d^4y}{dx^4}":GREEN
                })
        ]
        comments=[
            TextMobject("First derivative of sin(x)",
                tex_to_color_map={
                    "First":YELLOW,
                    "sin":PURPLE
                }),
            TextMobject("Second derivative of sin(x)",
                tex_to_color_map={
                    "Second":RED,
                    "sin":PURPLE
                }),
            TextMobject("Third derivative of sin(x)",
                tex_to_color_map={
                    "Third":ORANGE,
                    "sin":PURPLE
                }),
            TextMobject("Fourth derivative of sin(x)",
                tex_to_color_map={
                    "Fourth":GREEN,
                    "sin":PURPLE
                })
        ]
        VGroup(func_formula,func_comment).arrange(UP)
        self.play(FadeIn(func_comment),Write(func_formula))
        self.wait()
        self.play(FadeOut(func_comment),Transform(func_formula,deriv_formula))
        for formula,comment in zip(formulas,comments):
            VGroup(formula,comment).arrange(UP)
            self.play(Transform(func_formula,formula),
                Transform(func_comment,comment))
        self.play(FadeOut(func_comment),FadeOut(func_formula))
        self.wait()

class GraphStuff(GraphScene):
    CONFIG={
        "x_min": -8,
        "x_max": 8,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
    }

    @staticmethod
    def tangent_line(x):
        return np.cos(np.pi)*(x-np.pi)+np.sin(np.pi)

    @staticmethod
    def tangent_line2(x):
        return -np.sin(np.pi)*(x-np.pi)+np.cos(np.pi)

    @staticmethod
    def tangent_line3(x):
        return -np.cos(np.pi)*(x-np.pi)-np.sin(np.pi)

    @staticmethod
    def tangent_line4(x):
        return np.sin(np.pi)*(x-np.pi)-np.cos(np.pi)

    @staticmethod
    def tangent_line5(x):
        return np.exp(1)*(x-1)+np.exp(1)

    @staticmethod
    def negate_sin(x):
        return -np.sin(x)
    
    @staticmethod
    def negate_cos(x):
        return -np.cos(x)

    def construct(self):
        self.setup_axes(animate=True)
        graph=self.get_graph(np.sin,color=GREEN)
        label=self.get_graph_label(graph,label="\\sin(x)")
        self.play(ShowCreation(graph),Write(label))
        pt=Dot(self.coords_to_point(np.pi,np.sin(np.pi)))
        tangentline=self.get_graph(self.tangent_line,color=YELLOW)
        self.play(ShowCreation(tangentline),ShowCreation(pt))
        self.wait()
        # Now change sin(x) to cos(x) and the tangent line respectively
        graph2=self.get_graph(np.cos,color=BLUE)
        label2=self.get_graph_label(graph2,"\\cos(x)")
        pt2=Dot(self.coords_to_point(np.pi,np.cos(np.pi)))
        tangentline2=self.get_graph(self.tangent_line2,color=YELLOW)
        self.wait()
        self.play(Transform(graph,graph2),Transform(label,label2),
            Transform(pt,pt2),Transform(tangentline,tangentline2))
        # Now to -sin(x)
        graph3=self.get_graph(self.negate_sin,color=GREEN)
        label3=self.get_graph_label(graph3,"-\\sin(x)")
        pt3=Dot(self.coords_to_point(np.pi,-np.sin(np.pi)))
        tangentline3=self.get_graph(self.tangent_line3,color=YELLOW)
        self.wait()
        self.play(Transform(graph,graph3),Transform(label,label3),
            Transform(pt,pt3),Transform(tangentline,tangentline3))
        # Now to -cos(x)
        graph4=self.get_graph(self.negate_cos,color=BLUE)
        label4=self.get_graph_label(graph4,"-\\cos(x)")
        pt4=Dot(self.coords_to_point(np.pi,-np.cos(np.pi)))
        tangentline4=self.get_graph(self.tangent_line4,color=YELLOW)
        self.wait()
        self.play(Transform(graph,graph4),Transform(label,label4),
            Transform(pt,pt4),Transform(tangentline,tangentline4))
        self.wait()
        graph5=self.get_graph(np.exp,color=GREEN)
        label5=self.get_graph_label(graph5,"e^x")
        pt5=Dot(self.coords_to_point(1,np.exp(1)))
        tangentline5=self.get_graph(self.tangent_line5,color=YELLOW)
        self.wait()
        self.play(Transform(graph,graph5),Transform(label,label5),
            Transform(pt,pt5),Transform(tangentline,tangentline5))
        self.wait()
        self.play(FadeOut(tangentline),FadeOut(graph),
            FadeOut(label),FadeOut(self.axes),FadeOut(pt))

class LimitScene(GraphScene):
    CONFIG={
        "x_min": -2,
        "x_max": 1,
        "y_min": -1,
        "y_max": 4,
        "graph_origin": 2*DOWN,
    }

    @staticmethod
    def func(x):
        return (1+x**3)/(1+x)

    def construct(self):
        title=TextMobject(
                "Limit of $\\frac{x^3+1}{x+1}$ at $x=-1$")
        formula="\\frac{(%f)^3+1}{%f+1}= %f"
        y=self.func(-0.9)
        str_y="%f" % y
        formula_orig=TexMobject(formula % (-0.9,-0.9,y),
            tex_to_color_map={str_y:RED})
        VGroup(formula_orig,title).arrange(UP)
        self.play(Write(title))
        self.play(ShowCreation(formula_orig))
        dx=0.01
        formatted=""
        for i in range(5):
            self.wait()
            x=-1.0+dx
            y=self.func(x)
            str_y="%f" % y
            formatted=formula % (x,x,y)
            formula_obj=TexMobject(formatted,
                tex_to_color_map={str_y:RED})
            VGroup(formula_obj,title).arrange(UP)
            self.play(Transform(formula_orig,formula_obj))
            dx/=10
        self.wait()
        to_append="\\approx 3"
        formula_approx=TexMobject(formatted+to_append,
            tex_to_color_map={str_y:RED,to_append:YELLOW})
        VGroup(formula_approx,title).arrange(UP)
        self.play(Transform(formula_orig,formula_approx))
        self.wait()
        newtitle=TextMobject(
            "Limit of $f(x)$ at $x=-1$",
            tex_to_color_map={"$f(x)$":BLUE}).to_edge(UP).to_edge(RIGHT)
        self.play(Transform(title,newtitle),FadeOut(formula_orig))
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func,color=BLUE)
        func_lbl=self.get_graph_label(func_graph,
                "f(x)=\\frac{x^3+1}{x+1} \\ (x \\ne -1)").to_edge(DOWN)
        self.play(ShowCreation(func_graph),ShowCreation(func_lbl))
        newformula="f(%f)=%f"
        y=self.func(-0.9)
        str_x="%f" % -0.9
        str_y="%f" % y
        newformula_orig=TexMobject(newformula
            % (-0.9,y),
            tex_to_color_map={
                str_x:GREEN,
                str_y:RED
            }).to_edge(RIGHT)
        pt_orig=Dot(self.coords_to_point(-0.9,y))
        vline_orig=self.get_vertical_line_to_graph(-0.9,func_graph,
                color=GREEN)
        a=self.coords_to_point(0,y)
        b=self.coords_to_point(-0.9,y)
        hline_orig=Line(a,b,color=RED)
        self.play(Write(newformula_orig),ShowCreation(vline_orig),
                ShowCreation(hline_orig),ShowCreation(pt_orig))
        dx=0.01
        for i in range(5):
            self.wait()
            x=-1.0+dx
            y=self.func(x)
            str_x="%f" % x
            str_y="%f" % y
            formatted=newformula % (x,y)
            pt_obj=Dot(self.coords_to_point(x,y))
            vline_obj=self.get_vertical_line_to_graph(x,func_graph,
                    color=GREEN)
            a=self.coords_to_point(0,y)
            b=self.coords_to_point(x,y)
            hline_obj=Line(a,b,color=RED)
            newformula_obj=TexMobject(formatted,
                tex_to_color_map={
                    str_x:GREEN,
                    str_y:RED
                }).to_edge(RIGHT)
            self.play(Transform(newformula_orig,newformula_obj),
                    Transform(vline_orig,vline_obj),
                    Transform(hline_orig,hline_obj),Transform(pt_orig,pt_obj))
            dx/=10
        self.wait()
        newformula_approx=TexMobject(formatted+to_append,
            tex_to_color_map={
                str_x:GREEN,
                str_y:RED,
                to_append:YELLOW
            }).to_edge(RIGHT)
        self.play(Transform(newformula_orig,newformula_approx))
        self.wait()
        newformula_lim=TexMobject("\\lim_{x \\to -1}f(x)=3",
            tex_to_color_map={
                "_{x \\to -1}":GREEN,
                "f(x)":BLUE,
                "3":YELLOW
            }).to_edge(RIGHT)
        self.play(Transform(newformula_orig,newformula_lim))
        self.wait()
        self.play(FadeOut(func_graph),FadeOut(func_lbl),FadeOut(title),
            FadeOut(newformula_orig),FadeOut(pt_orig),FadeOut(hline_orig),
            FadeOut(vline_orig),FadeOut(self.axes))
        self.wait()
        summary=TexMobject("\\therefore \\lim_{x \\to -1}\\frac{x^3+1}{x+1}=3")
        self.play(Write(summary))
        self.wait()
        self.play(FadeOut(summary))

class DerivativeScene(GraphScene):
    CONFIG={
        "x_min":-1,
        "x_max":2,
        "y_min":-1,
        "y_max":2,
        "graph_origin":4*LEFT+1.8*DOWN
    }
    @staticmethod
    def func(x):
        return np.cos(3*x)+2*np.sin(x)
    @staticmethod
    def dfunc(x):
        return -3*np.sin(3*x)+2*np.cos(x)
    def secant_line(self,x):
        return self.slope*(x-self.x0)+self.y0
    def update_secant(self,x,y):
        self.slope=(y-self.y0)/(x-self.x0)
        return (Dot(self.coords_to_point(x,y)),
                self.get_graph(self.secant_line,color=YELLOW))
    def update_text(self,dx):
        str_dx="%f" % dx
        str_slope="%f" % self.slope
        formula="\\frac{\\Delta y}{\\Delta x}={f(%f+%f)-f(%f)\\over%f}=%f"
        return TexMobject(formula % (self.x0,dx,self.x0,dx,self.slope),
            tex_to_color_map={
                self.str_x0:GREEN,
                str_dx:RED,
                str_slope:YELLOW
            }).to_edge(RIGHT).to_edge(DOWN).scale(0.7)
    def construct(self):
        title=TextMobject("Differential Calculus",
            tex_to_color_map={"Differential":YELLOW})
        self.play(FadeIn(title))
        self.wait()
        self.play(FadeOut(title))
        self.setup_axes(animate=True)
        graph=self.get_graph(self.func,color=GREEN)
        label=self.get_graph_label(graph,"f(x)")
        self.play(ShowCreation(graph),Write(label))
        self.wait()
        # Now draw a secant line
        self.x0=0.2
        self.y0=self.func(self.x0)
        self.str_x0="%f" % self.x0
        pt1=Dot(self.coords_to_point(self.x0,self.y0))
        self.play(ShowCreation(pt1))
        x=1.2
        y=self.func(x)
        pt2_orig,line_orig=self.update_secant(x,y)
        self.play(ShowCreation(pt2_orig))
        self.wait()
        self.play(ShowCreation(line_orig))
        dx=0.1
        formula_orig=self.update_text(dx)
        self.play(ShowCreation(formula_orig))
        for i in range(6):
            x=self.x0+dx
            (pt2,line)=self.update_secant(x,self.func(x))
            self.play(Transform(formula_orig,self.update_text(dx)))
            self.play(Transform(pt2_orig,pt2),Transform(line_orig,line))
            dx/=10
        self.wait()
        # Now show the limit expression
        str_dfunc="%f" % self.dfunc(self.x0)
        formula_lim=TexMobject(
            "\\frac{dy}{dx}=\\lim_{\\Delta x \\to 0}{f(%f+\\Delta x)-f(%f)" \
            "\\over \\Delta x}=%f" % (self.x0,self.x0,self.dfunc(self.x0)),
            tex_to_color_map={
                self.str_x0:GREEN,
                "_{\\Delta x \\to 0}":RED,
                "\\Delta x":RED,
                str_dfunc:YELLOW
            })
        formula_lim_orig= \
            deepcopy(formula_lim).to_edge(RIGHT).to_edge(DOWN).scale(0.7)
        self.play(Transform(formula_orig,formula_lim_orig))
        self.wait()
        self.play(FadeOut(pt1),FadeOut(pt2_orig),FadeOut(line_orig),
            FadeOut(graph),FadeOut(label),FadeOut(self.axes),
            Transform(formula_orig,formula_lim))
        self.wait()
        formula_simplified=TexMobject("\\because\\space \\frac{dy}{dx}=" \
                "%f" % self.dfunc(self.x0),
                tex_to_color_map={str_dfunc:YELLOW})
        summary=TextMobject( \
            "$\\therefore$ The slope to the tangent line is %f"
            % self.dfunc(self.x0),
            tex_to_color_map={
                str_dfunc:YELLOW
            })
        group=VGroup(summary,formula_simplified).arrange(UP)
        self.play(Transform(formula_orig,group))
        self.wait()
        self.play(FadeOut(formula_orig))
        self.wait()

class ThanksScene(Scene):
    def construct(self):
        poweredby=TextMobject("Powered by \\LaTeX\\ and manim",
            tex_to_color_map={"manim":BLUE})
        author=TextMobject("Created by @TravorLZH",
            tex_to_color_map={"@TravorLZH":YELLOW})
        VGroup(poweredby,author).arrange(UP)
        self.play(FadeIn(poweredby),Write(author))
        self.wait()
