from manimlib.imports import *

problem_no="\scshape AMC10 2018A Problem 14"
problem_string=r"What is the greatest integer less than or equal to " \
        r"$3^{100}+2^{100}\over3^{96}+2^{96}$?"
choices_string="(A) 80\space\space\space(B) 81\space\space\space(C) " \
        r"96\space\space\space(D) 97\space\space\space(E) 625"

class Openning(Scene):
    def construct(self):
        title=TextMobject(problem_no).scale(1.5)
        problm=TextMobject(problem_string,
            tex_to_color_map={
                "greatest":GREEN,
                "integer":BLUE,
                "less":YELLOW,
                "equal":ORANGE
            })
        footer=TextMobject(choices_string)
        everything=VGroup(title,problm,footer).arrange(DOWN)
        self.play(FadeIn(title))
        self.play(Write(problm))
        self.play(FadeIn(footer))
        self.wait()
        self.play(FadeOut(everything))
        self.wait()

class DoSubstitution(Scene):
    def construct(self):
        formula_str=r"3^{100}+2^{100}\over 3^{96}+2^{96}"
        formula=TexMobject(formula_str,
            tex_to_color_map={
                "3":BLUE,"2":GREEN
            }).scale(3)
        self.play(FadeIn(formula))
        subst_x_note=TexMobject(r"x=3^{96}",
            tex_to_color_map={
                "x":RED,"3":BLUE
            }).scale(1.5).to_edge(LEFT).to_edge(UP)
        subst_y_note=TexMobject(r"y=2^{96}",
            tex_to_color_map={
                "2":GREEN,"y":ORANGE
            }).scale(1.5).to_edge(RIGHT).to_edge(DOWN)
        formula_x0=TexMobject(r"3^4\cdot3^{96}+2^{100}\over 3^{96}+2^{96}",
            tex_to_color_map={
                "3^4":BLUE,"2":GREEN,"3^{96}":RED
            }).scale(3)
        formula_x1=TexMobject(r"3^4x+2^{100}\over x+2^{96}",
            tex_to_color_map={
                "3^4":BLUE,"x":RED,"2":GREEN
            }).scale(3)
        formula_y0=TexMobject(r"3^4x+2^4\cdot2^{96}\over x+2^{96}",
            tex_to_color_map={
                "3^4":BLUE,"2^4":GREEN,"2^{96}":ORANGE,"x":RED
            }).scale(3)
        formula_y1=TexMobject(r"3^4x+2^4y\over x+y",
            tex_to_color_map={
                "3^4":BLUE,"2^4":GREEN,"x":RED,"y":ORANGE
            }).scale(3)
        self.play(Write(subst_x_note))
        self.play(Write(subst_y_note))
        self.wait()
        self.play(Transform(formula,formula_x0))
        self.play(TurnInsideOut(subst_x_note),Transform(formula,formula_x1))
        self.wait()
        self.play(Transform(formula,formula_y0))
        self.play(Flash(subst_y_note),Transform(formula,formula_y1))
        formula_expanded=TexMobject(r"81x+16y\over x+y",
            tex_to_color_map={
                "81":BLUE,"16":GREEN,"x":RED,"y":ORANGE
            }).scale(3)
        formula_split=TexMobject(r"65x+16x+16y\over x+y",
            tex_to_color_map={
                "65":BLUE,"16":GREEN,"x":RED,"y":ORANGE
            }).scale(3)
        self.play(Transform(formula,formula_expanded))
        self.play(Transform(formula,formula_split))
        factor_rule=TexMobject("ab+ac=a(b+c)") \
            .scale(1.5).to_edge(LEFT).to_edge(DOWN)
        formula_factored=TexMobject(r"65x+16(x+y)\over x+y",
            tex_to_color_map={
                "65":BLUE,"16":GREEN,"x":RED,"y":ORANGE
            }).scale(3)
        self.play(Write(factor_rule))
        self.play(TurnInsideOut(factor_rule),
                Transform(formula,formula_factored))
        simplify_rule1=TexMobject(r"\exists c\ne0",color=YELLOW)
        simplify_rule2=TexMobject(r"\therefore\frac{a+bc}c=\frac{a}c+b",
            color=YELLOW)
        simplify_gp=VGroup(simplify_rule1,simplify_rule2) \
            .arrange(RIGHT).scale(1.5).to_edge(RIGHT).to_edge(UP)
        formula_simplified=TexMobject(r"{65x\over x+y}+16",
            tex_to_color_map={
                "65":BLUE,"x":RED,"y":ORANGE,"16":GREEN
            }).scale(3)
        self.play(Write(simplify_rule1))
        self.play(Write(simplify_rule2))
        self.wait()
        self.play(Indicate(simplify_rule2),
            Transform(formula,formula_simplified))
        x_not_zero=TexMobject(r"x\ne0",tex_to_color_map={"x":RED}) \
            .scale(1.5).to_edge(LEFT).to_edge(UP)
        formula_final=TexMobject(r"{65\over 1+{y\over x}}+16",
            tex_to_color_map={
                "65":BLUE,"x":RED,"y":ORANGE,"16":GREEN
            }).scale(3)
        backup=subst_x_note.copy()
        self.play(ReplacementTransform(subst_x_note,x_not_zero))
        self.wait()
        self.play(ReplacementTransform(x_not_zero,backup),
                Transform(formula,formula_final))
        x_and_y=VGroup(backup,subst_y_note)
        y_over_x=TexMobject(r"{y\over x}={2^{96}\over3^{96}}",
            tex_to_color_map={
                "y":ORANGE,"x":RED
            }).scale(1.5).to_edge(LEFT).to_edge(UP)
        y_over_x2=TexMobject(r"{y\over x}=\left(2\over 3\right)^{96}",
            tex_to_color_map={
                "y":ORANGE,"x":RED
            }).scale(1.5).to_edge(LEFT).to_edge(UP)
        power_rule=TexMobject(r"{a^n\over b^n}=\left(a\over b\right)^n") \
            .scale(1.5).to_edge(RIGHT).to_edge(DOWN)
        self.play(ReplacementTransform(x_and_y,y_over_x))
        self.play(Write(power_rule))
        self.wait()
        self.play(TurnInsideOut(power_rule),Transform(y_over_x,y_over_x2))
        self.wait()
        formula_eval=TexMobject(r"{65\over 1+\left(2\over 3\right)^{96}}+16",
            tex_to_color_map={
                "65":BLUE,"16":GREEN
            }).scale(3)
        self.play(Transform(formula,formula_eval))
        to_hide=VGroup(simplify_gp,power_rule,factor_rule)
        approach_zero=TexMobject(r"\left(2\over3\right)^{96}>0") \
            .scale(1.5).to_edge(LEFT).to_edge(UP)
        self.play(FadeOut(to_hide),
            ReplacementTransform(y_over_x,approach_zero))
        formula_result=r"{%s}<81" % formula_str
        formula_approxes=[
            TexMobject(r"{65\over 1+>0}+16",
                tex_to_color_map={
                    "65":BLUE,"16":GREEN,r">0":MAROON
                }).scale(3),
            TexMobject(r"{65\over >1}+16",
                tex_to_color_map={
                    "65":BLUE,"16":GREEN,r">1":MAROON
                }).scale(3),
            TexMobject(r"<65+16",
                tex_to_color_map={
                    "16":GREEN,r"<65":MAROON
                }).scale(3),
            TexMobject(formula_result,
                tex_to_color_map={
                    "<81":MAROON
                }).scale(3)
        ]
        for formula_approx in formula_approxes:
            self.play(Transform(formula,formula_approx))
            self.wait()
        self.play(FadeOut(approach_zero))
        choices=TextMobject(choices_string,
            tex_to_color_map={"(A) 80":YELLOW})
        proof=TextMobject(r"$\because$ Find the greatest integer$\cdots$",
            tex_to_color_map={
                "greatest":GREEN,
                "integer":BLUE
            })
        formula_upper=TexMobject(formula_result)
        answer=VGroup(choices,proof,formula_upper).arrange(UP)
        self.play(ReplacementTransform(formula,formula_upper))
        self.play(Write(proof))
        self.play(FadeIn(choices))
        self.wait()
        self.play(FadeOut(answer))

class ThanksScene(Scene):
    def construct(self):
        problm=TextMobject(problem_string,
            tex_to_color_map={
                "greatest":GREEN,
                "integer":BLUE,
                "less":YELLOW,
                "equal":ORANGE
            })
        choices=TextMobject(choices_string,
            tex_to_color_map={"(A) 80":YELLOW})
        solution=VGroup(problm,choices).arrange(DOWN).to_edge(UP)
        self.play(FadeIn(solution))
        created_by=TextMobject("Created by")
        author=TextMobject("@TravorLZH")
        author.set_color_by_gradient(RED,YELLOW)
        line1=VGroup(created_by,author).arrange(RIGHT)
        poweredby=TextMobject(r"Powered by \LaTeX{} and manim",
            tex_to_color_map={"manim":BLUE})
        VGroup(line1,poweredby).arrange(DOWN).scale(2)
        self.play(Write(created_by))
        self.play(Write(author),Write(poweredby))
        self.wait(20)
