from manimlib.imports import *

e_def=r"{e}=\lim_{n\to\infty}(1+{1\over n})^n"
ln_def=r"\ln(t)=\int_1^t{1\over x}dx"

class IntroScene(Scene):
    def construct(self):
        e_eqn=TexMobject(e_def,
            tex_to_color_map={
                "{e}":GREEN,
                r"_{n\to\infty}":ORANGE,
                r"{1\over n}":ORANGE,
                r"^n":ORANGE
            }).scale(1.5).to_edge(RIGHT).to_edge(DOWN)
        ln_eqn=TexMobject(ln_def,
            tex_to_color_map={
                r"\ln(t)":RED,
                r"\int":BLUE,
                r"_1^t":RED
            }).scale(1.5).to_edge(LEFT).to_edge(DOWN)
        tit=TextMobject("The story of",tex_to_color_map={"story":BLUE})
        tit2=TextMobject("natural logarithm",color=RED).scale(1.5)
        tit3=TextMobject("and")
        tit4=TexMobject("e",color=GREEN).scale(4)
        everything=VGroup(tit,tit2,tit3,tit4).arrange(DOWN).scale(1.5)
        for obj in [tit,tit2,tit3,tit4,e_eqn,ln_eqn]:
            self.play(FadeIn(obj))
            self.wait()
        self.wait()
        ln_eqn2=TexMobject(ln_def).scale(2)
        self.play(FadeOut(VGroup(tit,tit2,tit3,tit4,e_eqn)),
            Transform(ln_eqn,ln_eqn2))
        self.wait()
        self.play(FadeOut(ln_eqn))

class LnScene(GraphScene):
    CONFIG={
        "x_min":0,
        "x_max":4,
        "y_min":0,
        "y_max":3,
        "graph_origin":DOWN*3+LEFT*3
    }
    @staticmethod
    def f(x):
        return 1/x
    def construct(self):
        self.setup_axes(animate=True)
        fx=self.get_graph(self.f,color=YELLOW)
        pt0=self.coords_to_point(1,0)
        pt1=self.coords_to_point(1,1)
        pt2=self.coords_to_point(np.exp(1),0)
        pt3=self.coords_to_point(np.exp(1),np.exp(-1))
        x0=TexMobject("1",color=GREEN)
        x1=TexMobject("t",color=RED)
        dt=Dot(pt1)
        dt2=Dot(pt3)
        ln1=Line(pt1,pt0,color=GREEN)
        lnx=Line(pt3,pt2,color=RED)
        x0.next_to(ln1,DOWN)
        x1.next_to(lnx,DOWN)
        area=self.get_area(fx,1,np.exp(1))
        for obj in [fx,dt,dt2,ln1,x0,lnx,x1,area]:
            self.play(ShowCreation(obj))
            self.wait()
        ln0=TexMobject(r"\ln(t)=",color=RED)
        int0=TexMobject(r"\int_1^t",tex_to_color_map={
            r"\int":BLUE,"_1":GREEN,"^t":RED})
        fn0=TexMobject(r"1\over x",color=YELLOW)
        int1=TexMobject(r"dx",color=BLUE)
        stuff=VGroup(ln0,int0,fn0,int1).arrange(RIGHT)
        stuff.next_to(area,UP)
        br=Brace(VGroup(int0,fn0,int1),UP)
        blbl=TextMobject("The area under the curve",
            tex_to_color_map={
                "area":BLUE,
                "curve":YELLOW
            }).scale(0.8)
        br.put_at_tip(blbl)
        b=VGroup(br,blbl)
        self.play(ShowCreation(ln0))
        self.wait()
        self.play(ReplacementTransform(fx.copy(),fn0))
        self.wait()
        self.play(ReplacementTransform(area.copy(),VGroup(int0,int1)))
        self.play(FadeIn(b))
        self.wait()
        self.play(FadeOut(b))
        self.wait()
        self.play(FadeOut(VGroup(area,stuff,fx,x0,x1,self.axes,ln1,lnx,dt,dt2)))

class LnPropScene(Scene):
    def product_prop(self):
        equal=TexMobject("=").scale(1.5)
        el0=TexMobject(r"\ln(ab)").scale(1.5)
        er0=TexMobject(r"\int_1^{ab}{dx\over x}").scale(1.5)
        el0.next_to(equal,LEFT)
        er0.next_to(equal,RIGHT)
        self.play(FadeIn(VGroup(el0,equal,er0)))
        self.wait()
        els=[
            TexMobject(r"\int_1^a{dx\over x}+\int_1^b{du\over u}",
                tex_to_color_map={
                    "u":BLUE
                }).scale(1.5),
            TexMobject(r"\text{ln}(ab)",tex_to_color_map={
                "a":RED,"b":YELLOW}).scale(1.5)
        ]
        ers=[
            TexMobject(r"\int_1^a{dx\over x}+\int_a^{ab}{{a}dx\over {a}x}",
                tex_to_color_map={
                    "{a}":RED
                }).scale(1.5),
            TexMobject(r"\ln(a)+\ln(b)",tex_to_color_map={
                r"\ln(a)":RED,r"\ln(b)":YELLOW}).scale(1.5)
        ]
        [el.next_to(equal,LEFT) for el in els]
        [er.next_to(equal,RIGHT) for er in ers]
        el1=TexMobject(r"\int_1^a{dx\over x}+\int_a^{ab}{dx\over x}") \
            .scale(1.5)
        el1.next_to(equal,LEFT)
        self.play(Transform(el0,el1))
        self.wait()
        tmp=TexMobject("u=ax,du=ada",
            tex_to_color_map={
                "u":BLUE,"a":RED,"da":RED
            })
        tmp.next_to(el0,DOWN)
        for i,(er,el) in enumerate(zip(ers,els)):
            self.play(Transform(er0,er))
            self.wait()
            if i==0:
                self.play(FadeIn(tmp))
            self.play(Transform(el0,el))
            if i==0:
                self.play(FadeOut(tmp))
            self.wait()
        self.wait()
        self.play(FadeOut(VGroup(el0,equal,er0)))
    def power_prop(self):
        inteqn=TexMobject(r"n\int_1^a{dt\over t}")
        inteqn.next_to(self.tit,DOWN).to_edge(LEFT)
        self.play(Write(inteqn))
        inteqnr=TexMobject(r"=n\ln(a)")
        inteqnr.next_to(inteqn,RIGHT)
        self.play(FadeIn(inteqnr))
        self.wait()
        self.play(FadeOut(inteqnr))
        eqns=[
            r"=\int_1^a{n\over t}dt",
            r"=\int_1^a{n\cdot t^{n-1}\over t\cdot t^{n-1}}dt",
            r"=\int_1^a{nt^{n-1}\over t^n}dt"
        ]
        objs=VGroup(*[TexMobject(eqn) for eqn in eqns]).arrange(RIGHT)
        objs.next_to(inteqn)
        for obj in objs.submobjects:
            self.play(Write(obj))
            self.wait()
        usub=TexMobject("u=t^n,du=nt^{n-1}dt",
            tex_to_color_map={
                "u":BLUE,
                "t":RED
            }).to_edge(LEFT).to_edge(DOWN)
        self.play(FadeIn(usub))
        eqnn=TexMobject(r"\int_1^{a^n}{du\over u}",
            tex_to_color_map={"u":BLUE,r"\int_1^{a^n}":RED}).scale(1.5)
        self.play(ShowCreation(eqnn))
        self.wait()
        eqnn2=TexMobject(r"\ln(a^n)",color=RED).scale(1.5)
        self.play(Transform(eqnn,eqnn2))
        self.wait()
        self.play(Transform(eqnn,TexMobject(r"n\ln(a)=\ln(a^n)").scale(1.5)))
        self.wait()
        self.play(FadeOut(VGroup(usub,objs,inteqn)))
        self.play(FadeOut(eqnn))
    def quotient_prop(self):
        eqn0=TexMobject(r"\ln\left(a\over b\right)").scale(2)
        eqns=[
            r"\ln(ab^{-1})",r"\ln(a)+\ln(b^{-1})"
        ]
        for eqn in eqns:
            self.play(Transform(eqn0,TexMobject(eqn).scale(2)))
            self.wait()
        pwr=TexMobject(r"\ln(x^n)=n\ln(x)").to_edge(DOWN)
        self.play(VFadeInThenOut(pwr))
        eqns2=[
            r"\ln(a)+(-1)\ln(b)",r"\ln(a)-\ln(b)"
        ]
        for eqn in eqns2:
            self.play(Transform(eqn0,TexMobject(eqn).scale(2)))
            self.wait()
        self.play(Transform(eqn0,TexMobject(
            r"\text{ln}\left({a}\over {b}\right)=\ln(a)-\ln(b)",
            tex_to_color_map={
                "{a}":GREEN,"{b}":YELLOW,r"\ln(a)":GREEN,r"\ln(b)":YELLOW}) \
            .scale(2)))
        self.wait()
        self.play(FadeOut(eqn0))
    def construct(self):
        self.tit=Title("Product rule of natural log")
        self.play(ShowCreation(self.tit))
        self.product_prop()
        self.play(Transform(self.tit,Title("Power rule of natural log")))
        self.power_prop()
        self.play(Transform(self.tit,Title("Quotient rule of natural log")))
        self.quotient_prop()
        self.play(FadeOut(self.tit))
