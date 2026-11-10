from manim import *
from manim_slides import Slide
import numpy as np


def backprop_nudge(scene):
    """One output neuron; fixed input and bias. Click through the dependency chain."""
    colors = [BLUE_B, GREEN_B, WHITE, RED_C]
    title = Text("How does one weight change the error?", font_size=32).to_edge(UP, buff=.3)
    x, b = .48, .18  # Binary classification example with correct label y=1.
    tracker = ValueTracker(1.0)
    def values():
        w = tracker.get_value()
        z = w*x+b
        a = 1/(1+np.exp(-z))
        return [w,z,a,float(np.logaddexp(0.0, -z))]  # -log(sigmoid(z)), stably evaluated.
    baseline = values()
    neuron = VGroup(Circle(radius=.32),Circle(radius=.32)).arrange(RIGHT,buff=1.7).move_to([-2,2.05,0])
    edge = Line(neuron[0].get_right(),neuron[1].get_left(),color=BLUE_B)
    inputs = MathTex(r"a_{\rm in}=0.48",font_size=25).next_to(neuron[0],DOWN,buff=.15)
    weight = MathTex("w",color=BLUE_B,font_size=30).next_to(edge,UP,buff=.1)
    output = always_redraw(lambda: DecimalNumber(values()[2],num_decimal_places=2,font_size=23).move_to(neuron[1]))
    input_number = DecimalNumber(x,num_decimal_places=2,font_size=23).move_to(neuron[0])
    desired = MathTex("y=1",color=YELLOW,font_size=30).move_to([3,2.05,0])
    desired_label=Text("Correct label",font_size=20,color=YELLOW).next_to(desired,DOWN,buff=.15)
    scene.play(Write(title),Create(neuron),Create(edge),Write(inputs),Write(weight),FadeIn(output),FadeIn(input_number),Write(desired),Write(desired_label))
    scene.next_slide()
    equations=VGroup(MathTex(r"z=w a_{\rm in}+b",font_size=28),MathTex(r"a=\sigma(z)",font_size=28),MathTex(r"L=-\log(a)",font_size=28)).arrange(RIGHT,buff=.8).move_to([0,.95,0])
    scene.play(Write(equations))
    scene.next_slide()
    axes=VGroup()
    labels=VGroup()
    dots=VGroup()
    numbers=VGroup()
    for i,(symbol,caption,span) in enumerate(zip(['w','z','a','L'],['Weight','Weighted input','P(correct)','Loss'],[(.7,1.4),(.45,.9),(.55,.8),(.30,.50)])):
        pos=-4.7+i*3.1
        axis=NumberLine(x_range=[span[0],span[1],(span[1]-span[0])/6],length=2.15,include_numbers=False,color=GREY_B).move_to([pos,-.65,0])
        label=VGroup(MathTex(symbol,color=colors[i],font_size=36),Text(caption,font_size=18)).arrange(DOWN,buff=.12).move_to([pos,.1,0])
        dot=always_redraw(lambda i=i,axis=axis: Dot(axis.n2p(values()[i]),radius=.065,color=colors[i]))
        number=always_redraw(lambda i=i,pos=pos: DecimalNumber(values()[i],num_decimal_places=3,font_size=23,color=colors[i]).move_to([pos,-1.15,0]))
        axes.add(axis);labels.add(label);dots.add(dot);numbers.add(number)
    arrows=VGroup(*[Arrow(labels[i].get_right()+RIGHT*.1,labels[i+1].get_left()-RIGHT*.1,buff=.15,stroke_width=2,max_tip_length_to_length_ratio=.2) for i in range(3)])
    scene.play(Create(axes),Write(labels),FadeIn(dots),FadeIn(numbers),Create(arrows))
    scene.next_slide()
    note=Text("Nudge the weight: follow the change through each value",font_size=23,color=YELLOW).move_to([0,-1.8,0])
    ghosts=VGroup(*[Dot(axes[i].n2p(baseline[i]),radius=.045,color=GREY).set_opacity(.55) for i in range(4)])
    scene.play(Write(note),FadeIn(ghosts))
    scene.play(tracker.animate.set_value(1.2),run_time=3,rate_func=smooth)
    scene.next_slide()
    # The visible nudge is illustrative; derivatives below are analytic, not finite differences.
    formula=MathTex(r"\frac{\partial L}{\partial w}","=",r"\frac{\partial L}{\partial a}",r"\cdot",r"\frac{\partial a}{\partial z}",r"\cdot",r"\frac{\partial z}{\partial w}",font_size=37).move_to([0,-2.45,0])
    formula[0].set_color(BLUE_B);formula[2].set_color(RED_C);formula[4].set_color(WHITE);formula[6].set_color(GREEN_B)
    scene.play(FadeOut(note),Write(formula[0]),Write(formula[1]))
    for term,index in [(2,3),(4,2),(6,1)]:
        scene.play(Indicate(labels[index],color=YELLOW),Write(formula[term]),**{'run_time':.8})
        if term>2: scene.play(Write(formula[term-1]),run_time=.25)
        scene.next_slide()
    end=Text("Backprop computes these sensitivities. Gradient descent uses them.",font_size=21).to_edge(DOWN,buff=.25)
    scene.play(Write(end))
    scene.next_slide()
    output.clear_updaters()
    for item in [*dots,*numbers]: item.clear_updaters()
    return VGroup(title,neuron,edge,inputs,weight,output,input_number,desired,desired_label,equations,axes,labels,dots,numbers,arrows,ghosts,formula,end)


class BackpropPreview(Slide):
    skip_reversing = True
    def construct(self):
        self.camera.background_color='#1C1C1C'
        backprop_nudge(self)

