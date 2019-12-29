from manimlib.imports import *

def gauss_f(x):
    return np.exp(-x**2)

class IntIntroScene(GraphScene):
    CONFIG={
        "x_min":-4,
        "x_max":4,
        "y_min":-1,
        "y_max":2,
        "graph_origin":LEFT+DOWN
    }
    def construct(self):
        self.setup_axes(animate=True)
        func=self.get_graph(gauss_f,color=GREEN)
        self.play(ShowCreation(func))
        self.wait()
        intgp=VGroup(
            TexMobject(r"\int_{-\infty}^\infty",color=BLUE),
            TexMobject("e^{-x^2}",color=GREEN),
            TexMobject("dx",color=BLUE)).arrange(RIGHT).scale(1.5)
        intgp.to_edge(RIGHT).to_edge(UP)
        area=self.get_riemann_rectangles(func,-4,4,0.05,"right")
        self.play(ShowCreation(area))
        intg=VGroup(intgp.submobjects[0],intgp.submobjects[2])
        self.play(ReplacementTransform(func.copy(),intgp.submobjects[1]))
        self.wait()
        self.play(ReplacementTransform(area,intg))
        self.wait()
        self.play(FadeOut(VGroup(intgp,area,self.axes,func)))
        self.wait()

class SquareIntScene(Scene):
    def construct(self):
        tmap={"\mathbf{I}":GREEN_C,r"{\int_{-\infty}^\infty}":PINK,"dy":PINK,
            "dx":ORANGE,
            r"\int_{-\infty}^{\infty}":ORANGE}
        eqn=TexMobject(r"\mathbf{I}=\int_{-\infty}^{\infty} e^{-x^2}dx",
            tex_to_color_map=tmap)
        eqns=[
            r"\mathbf{I}^2=\left(\int_{-\infty}^{\infty} e^{-x^2}dx\right)^2",
            r"\mathbf{I}^2=\int_{-\infty}^{\infty} e^{-x^2}dx" \
                r"{\int_{-\infty}^\infty} e^{-y^2}dy",
            r"\mathbf{I}^2={\int_{-\infty}^\infty}" \
                r"\int_{-\infty}^{\infty} e^{-(x^2+y^2)}dxdy"
        ]
        self.play(Write(eqn))
        self.wait()
        for obj in eqns:
            self.play(Transform(eqn,TexMobject(obj,
                tex_to_color_map=tmap)))
            self.wait()
        self.play(eqn.to_edge,UP)
        self.wait()
        # Convert to polar form
        fml=TexMobject("x","=",r"r\cos",r"\theta",
            tex_to_color_map={
                "x":RED,"r":ORANGE,r"\theta":YELLOW
            })
        fml2=TexMobject("y","=","r",r"\sin",r"\theta",
            tex_to_color_map={
                "y":GREEN_C,"r":ORANGE,r"\theta":YELLOW
            })
        gp=VGroup(fml,fml2).arrange(DOWN)
        self.play(Write(gp))
        self.wait()
        self.play(gp.next_to,eqn,DOWN)
        self.wait()
        # Show the Jacobian matrix
        lt=TexMobject(r"\cos\theta",color=RED)
        rt=TexMobject(r"-r\sin\theta",color=YELLOW)
        lb=TexMobject(r"\sin\theta",color=BLUE)
        rb=TexMobject(r"r\cos\theta",color=GREEN_C)
        stuff=VGroup(VGroup(lt,lb).arrange(DOWN),VGroup(rt,rb).arrange(DOWN)) \
            .arrange(RIGHT)
        lbr=TexMobject(r"\big[").scale(2)
        rbr=TexMobject(r"\big]").scale(2)
        lbv=TexMobject(r"\big|").scale(2)
        rbv=TexMobject(r"\big|").scale(2)
        lbr.next_to(stuff,LEFT)
        rbr.next_to(stuff,RIGHT)
        lbv.next_to(stuff,LEFT)
        rbv.next_to(stuff,RIGHT)
        pts=[
            [fml[0],fml[2],RED],
            [fml[0],fml[4],YELLOW],
            [fml2[0],fml2[2],BLUE],
            [fml2[0],fml2[4],GREEN]
        ]
        jeq=TexMobject("J=",tex_to_color_map={"J":ORANGE})
        jeq.next_to(lbr,LEFT)
        jeq2=TexMobject(r"\text{det}(J)=",tex_to_color_map={"J":ORANGE})
        jeq2.next_to(lbr,LEFT)
        self.play(Write(jeq))
        self.play(FadeIn(VGroup(lbr,rbr)))
        for i,obj in enumerate([lt,rt,lb,rb]):
            rect1=SurroundingRectangle(pts[i][0],color=pts[i][2])
            rect2=SurroundingRectangle(pts[i][1],color=pts[i][2])
            gtmp=VGroup(rect1,rect2)
            self.play(FadeIn(rect1))
            self.play(FadeIn(rect2))
            self.wait()
            self.play(ReplacementTransform(gtmp,obj))
        self.wait()
        self.play(Transform(jeq,jeq2),Transform(lbr,lbv),Transform(rbr,rbv))
        self.wait()
        jres=TexMobject(r"r\cos^2\theta+r\sin^2\theta",
            tex_to_color_map={
                "r":ORANGE,r"\theta":YELLOW})
        jres.next_to(jeq,RIGHT)
        self.play(ReplacementTransform(VGroup(lbr,rbr,stuff),jres))
        self.wait()
        jfnl=TexMobject(r"\det(J)=r",tex_to_color_map={
            r"\det(J)":PURPLE,"r":ORANGE}).scale(1.5)
        self.play(ReplacementTransform(VGroup(jres,jeq),jfnl))
        self.wait()
        eqnf=TexMobject(r"\mathbf{I}^2=\int_0^{2\pi}\int_0^\infty" \
            r"e^{-r^2}rdrd\theta",
            tex_to_color_map={
                r"\mathbf{I}":GREEN_C,r"\int_0^{2\pi}":YELLOW,r"\int_0^\infty":ORANGE,
                "dr":ORANGE,r"d\theta":YELLOW
            })
        eqnf.to_edge(UP)
        self.play(ReplacementTransform(VGroup(jfnl,eqn),eqnf))
        self.play(FadeOut(gp))
        self.wait(20)
        self.play(FadeOut(eqnf))
        self.wait()

class EvalIntScene(Scene):
    def construct(self):
        intg=TexMobject(r"\mathbf{I}^2=\int_0^{2\pi}\int_0^\infty " \
            r"e^{-r^2}rdrd\theta")
        intg2=TexMobject(r"\mathbf{I}","^2=",r"\int_0^{2\pi}d\theta",
            r"\int_0^\infty e^{-r^2}rdr").to_edge(UP)
        intg2[0].set_color(GREEN_C)
        intg2[2].set_color(YELLOW)
        intg2[3].set_color(ORANGE)
        self.play(Write(intg))
        self.wait()
        self.play(ReplacementTransform(intg,intg2))
        self.wait()
        # Now perform u substitution for the latter integral
        br=Brace(intg[3],DOWN)
        sub=TexMobject(r"u=-{r}^2,du=-2{r}dr",tex_to_color_map={"{r}":RED})
        br.put_at_tip(sub)
        self.play(FadeIn(br))
        self.play(FadeIn(sub))
        eqn=TexMobject(r"-{1\over2}",r"\int_0^{-\infty}e^udu")
        eqn[1].set_color(GREEN)
        self.play(ReplacementTransform(VGroup(sub,intg[3].copy()),eqn))
        eqns=[
            r"\left.e^u\right|_0^{-\infty}",r"(0-1)",r"(-1)"
        ]
        for txt in eqns:
            obj=TexMobject(txt).next_to(eqn[0],RIGHT)
            self.play(Transform(eqn[1],obj))
            self.wait()
        eqnf=TexMobject(r"{1\over2}")
        self.play(ReplacementTransform(eqn,eqnf))
        self.play(eqnf.next_to,br,DOWN,rate_func=smooth)
        self.wait()
        twopi=TexMobject(r"2\pi",color=YELLOW)
        twopi.next_to(intg2[1],RIGHT)
        self.play(ReplacementTransform(intg2[2],twopi))
        self.wait()
        self.play(FadeOut(intg2[3]),FadeOut(br),eqnf.next_to,twopi,RIGHT)
        self.wait()
        intgf=TexMobject(r"\left(",r"\int_{-\infty}^\infty e^{-x^2}dx",
            r"\right)^2","=",r"\pi")
        intgf[1].set_color(GREEN)
        intgf[4].set_color(BLUE)
        self.play(ReplacementTransform(VGroup(intg2[0],intg2[1],twopi,eqnf),intgf))
        self.wait()
        pg=VGroup(intgf[0],intgf[2],intgf[4])
        sqrtpi=TexMobject(r"\sqrt\pi",tex_to_color_map={r"\pi":BLUE})
        sqrtpi.next_to(intgf[3],RIGHT)
        self.play(ReplacementTransform(pg,sqrtpi))
        self.wait()
        self.play(FadeOut(VGroup(intgf[1],intgf[3],sqrtpi)))
        self.wait()

class ThanksScene(Scene):
    def construct(self):
        poweredby=TextMobject(r"Powered by \LaTeX{} and manim",
            tex_to_color_map={r"\LaTeX{}":YELLOW,"manim":BLUE}).scale(1.2)
        author=TextMobject("Created"," by ","@TravorLZH").scale(1.2)
        author[0].set_color(BLUE)
        author[2].set_color_by_gradient(RED,YELLOW)
        eqn=TexMobject(r"\int_{-\infty}^\infty e^{-x^2}dx=","\sqrt\pi",
            tex_to_color_map={
                r"\int_{-\infty}^\infty":GREEN,"dx":GREEN,r"\pi":BLUE}).scale(2.5)
        poweredby.next_to(eqn,DOWN)
        author.next_to(eqn,UP)
        eqn.scale(1.5/2.5)
        self.play(FadeIn(poweredby),Write(author))
        self.play(FadeIn(eqn))
        self.wait(20)
