from manim import *
from manim_slides import Slide
from confused_robot import ConfusedRobot

# =====================================
# PRESENTATION SETTINGS
# =====================================

config.background_color = "#1C1C1C"


class DigiFest(Slide):
    skip_reversing = True

    def construct(self):

        # =====================================
        # SLIDE 1 — TITLE
        # =====================================

        title_top = Text(
            "How Much Mathematics Do We Actually Need",
            font_size=36,
            color=WHITE
        )

        title_bottom = Text(
            "to Understand AI?",
            font_size=48,
            color=YELLOW
        )

        title = VGroup(title_top, title_bottom)
        title.arrange(DOWN, buff=0.3)
        title.move_to(ORIGIN)

        subtitle = Text(
            "DigiTech Fest 2026",
            font_size=24,
            color=GREY_B
        )

        subtitle.next_to(title, DOWN, buff=0.8)

        self.play(Write(title_top), run_time=2)
        self.play(Write(title_bottom), run_time=1.5)
        self.play(FadeIn(subtitle))

        self.next_slide()

        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )

        # =====================================
        # SLIDE 2 — UNDERSTANDING AI
        # =====================================

        heading = Text(
            "Understanding AI",
            font_size=48,
            color=YELLOW
        )

        heading.to_edge(UP, buff=0.7)

        # Mathematical expressions
        equation_1 = MathTex(
            r"z = wx + b",
            font_size=48,
            color=BLUE
        )

        equation_2 = MathTex(
            r"\sigma(z) = \frac{1}{1+e^{-z}}",
            font_size=48,
            color=GREEN
        )

        equation_3 = MathTex(
            r"\frac{\partial L}{\partial w}",
            font_size=48,
            color=ORANGE
        )

        equations = VGroup(
            equation_1,
            equation_2,
            equation_3
        )

        equations.arrange(
            DOWN,
            buff=0.7
        )

        equations.move_to(ORIGIN)

        self.play(Write(heading))
        self.play(Write(equation_1))
        self.play(Write(equation_2))
        self.play(Write(equation_3))

        self.next_slide()

        # Main message
        message = Text(
            "Why do our models behave\n"
            "the way they do?",
            font_size=46,
            color=YELLOW,
            line_spacing=1.2
        )

        self.play(
            FadeOut(equations),
            FadeOut(heading)
        )

        self.play(
            Write(message),
            run_time=2
        )

        self.next_slide()

        self.play(FadeOut(message))

        # =====================================
        # SLIDE 3 — MODERN AI TOOLS
        # =====================================

        heading = Text(
            "The Power of Modern AI Tools",
            font_size=42,
            color=YELLOW
        )

        heading.to_edge(UP, buff=0.7)

        code = Code(
            code_string=(
                "from sklearn.neural_network import MLPClassifier\n\n"
                "model = MLPClassifier()\n"
                "model.fit(X_train, y_train)"
            ),
            language="python",
            background="window",
            paragraph_config={
                "font_size": 22
            }
        )

        code.scale(0.85)
        code.shift(LEFT * 2.5)

        arrow = Arrow(
            LEFT,
            RIGHT,
            color=WHITE
        )

        arrow.move_to(ORIGIN)

        # Simple network diagram
        network_layers = VGroup()

        for n in [4, 3, 3, 2]:

            layer = VGroup(
                *[
                    Circle(
                        radius=0.12,
                        color=BLUE
                    )
                    for _ in range(n)
                ]
            )

            layer.arrange(DOWN, buff=0.25)
            network_layers.add(layer)

        network_layers.arrange(RIGHT, buff=0.65)
        network_layers.scale(0.85)
        network_layers.shift(RIGHT * 3.5)

        self.play(Write(heading))
        self.play(FadeIn(code))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(network_layers))

        self.next_slide()

        accessibility = Text(
            "AI has never been more accessible.",
            font_size=40,
            color=GREEN
        )

        self.play(
            FadeOut(code),
            FadeOut(arrow),
            FadeOut(network_layers),
            FadeOut(heading)
        )

        self.play(Write(accessibility))

        self.next_slide()

        self.play(FadeOut(accessibility))

        # =====================================
        # SLIDE 4 — BUILDING VS UNDERSTANDING
        # =====================================

        build = Text(
            "Knowing how to BUILD AI",
            font_size=42,
            color=BLUE
        )

        understand = Text(
            "Understanding how AI WORKS",
            font_size=42,
            color=YELLOW
        )

        build.shift(UP * 1.2)
        understand.shift(DOWN * 1.2)

        arrow = Arrow(
            build.get_bottom(),
            understand.get_top(),
            buff=0.3,
            color=WHITE
        )

        self.play(Write(build))
        self.play(GrowArrow(arrow))
        self.play(Write(understand))

        self.next_slide()

        # =====================================
        # SLIDE 5 — THE CENTRAL QUESTION
        # =====================================

        question = Text(
            "Are they the same thing?",
            font_size=46,
            color=WHITE
        )

        self.play(
            FadeOut(build),
            FadeOut(understand),
            FadeOut(arrow)
        )

        self.play(Write(question))

        self.next_slide()

        self.play(FadeOut(question))

        # =====================================
        # SLIDE 6 — INTRODUCING A NEURAL NETWORK
        # =====================================

        heading = Text(
            "Our Example: A Neural Network",
            font_size=40,
            color=YELLOW
        )

        heading.to_edge(UP, buff=0.7)

        input_layer = VGroup(
            *[
                Circle(radius=0.15, color=BLUE)
                for _ in range(5)
            ]
        )

        hidden_layer_1 = VGroup(
            *[
                Circle(radius=0.15, color=WHITE)
                for _ in range(4)
            ]
        )

        hidden_layer_2 = VGroup(
            *[
                Circle(radius=0.15, color=WHITE)
                for _ in range(4)
            ]
        )

        output_layer = VGroup(
            *[
                Circle(radius=0.15, color=GREEN)
                for _ in range(3)
            ]
        )

        input_layer.arrange(DOWN, buff=0.3)
        hidden_layer_1.arrange(DOWN, buff=0.3)
        hidden_layer_2.arrange(DOWN, buff=0.3)
        output_layer.arrange(DOWN, buff=0.3)

        layers = VGroup(
            input_layer,
            hidden_layer_1,
            hidden_layer_2,
            output_layer
        )

        layers.arrange(RIGHT, buff=1.5)
        layers.move_to(ORIGIN)

        connections = VGroup()

        for layer_a, layer_b in zip(layers[:-1], layers[1:]):

            for neuron_a in layer_a:
                for neuron_b in layer_b:

                    line = Line(
                        neuron_a.get_center(),
                        neuron_b.get_center(),
                        color=GREY_B,
                        stroke_width=1
                    )

                    connections.add(line)

        network = VGroup(connections, layers)

        self.play(Write(heading))
        self.play(Create(connections), run_time=2)
        self.play(FadeIn(layers))

        self.next_slide()

        self.play(
            FadeOut(heading),
            FadeOut(network)
        )

        # =====================================
        # SLIDE 7 — THREE QUESTIONS
        # =====================================

        heading = Text(
            "Three Questions",
            font_size=48,
            color=YELLOW
        )

        heading.to_edge(UP, buff=0.8)

        questions = VGroup(

            Text(
                "1. What exactly is going on inside a neural network?",
                font_size=29
            ),

            Text(
                "2. How does it actually learn?",
                font_size=29
            ),

            Text(
                "3. Why should we care?",
                font_size=29
            )

        )

        questions.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.6
        )

        questions.move_to(ORIGIN)

        self.play(Write(heading))
        self.play(FadeIn(questions[0], shift=RIGHT))
        self.play(FadeIn(questions[1], shift=RIGHT))
        self.play(FadeIn(questions[2], shift=RIGHT))

        self.next_slide()
                # =====================================
        # QUESTION 1 — WHAT IS GOING ON?
        # =====================================

        self.play(
            FadeOut(heading),
            FadeOut(questions)
        )

        section_title = Text(
            "Question 1",
            font_size=32,
            color=GREY_B
        )

        section_question = Text(
            "What exactly is going on\ninside a neural network?",
            font_size=44,
            color=YELLOW,
            line_spacing=1.2
        )

        section_group = VGroup(
            section_title,
            section_question
        )

        section_group.arrange(DOWN, buff=0.5)
        section_group.move_to(ORIGIN)

        self.play(Write(section_title))
        self.play(Write(section_question))

        self.next_slide()

        self.play(FadeOut(section_group))

        # =====================================
        # THE HANDWRITTEN DIGIT
        # =====================================

        digit = Text(
            "3",
            font="Segoe Print",
            font_size=180,
            color=WHITE
        )

        self.play(
            Write(digit),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # THREE DIFFERENT HANDWRITTEN 3s
        # =====================================

        digit_left = Text(
            "3",
            font="Segoe Print",
            font_size=150,
            color=WHITE
        )

        digit_middle = Text(
            "3",
            font="Comic Sans MS",
            font_size=150,
            color=WHITE
        )

        digit_right = Text(
            "3",
            font="Segoe Script",
            font_size=150,
            color=WHITE
        )

        digit_group = VGroup(
            digit_left,
            digit_middle,
            digit_right
        )

        digit_group.arrange(RIGHT, buff=1.5)
        digit_group.move_to(ORIGIN)

        self.play(
            ReplacementTransform(digit, digit_middle)
        )

        self.play(
            FadeIn(digit_left, shift=LEFT),
            FadeIn(digit_right, shift=RIGHT)
        )

        self.next_slide()

        # =====================================
        # THE CENTRAL CHALLENGE
        # =====================================

        challenge = Text(
            "How can a machine recognise something\n"
            "when no two examples look exactly alike?",
            font_size=36,
            color=YELLOW,
            line_spacing=1.2
        )

        self.play(
            FadeOut(digit_group)
        )

        self.play(
            Write(challenge),
            run_time=2
        )

        self.next_slide()
        
                # =====================================
        # THE PIXEL GRID — 28 x 28
        # =====================================

        self.play(FadeOut(challenge))

        pixel_heading = Text(
            "What does the neural network actually see?",
            font_size=36,
            color=YELLOW
        )

        pixel_heading.to_edge(UP, buff=0.5)

        self.play(Write(pixel_heading))

        # Create a 28 x 28 pixel representation of a 3
        # This is a stylised example, not an actual MNIST image.

        pixel_grid = VGroup()

        for row in range(28):
            for col in range(28):

                # Normalised coordinates
                x = (col - 13.5) / 13.5
                y = (13.5 - row) / 13.5

                # Create a stylised digit 3 using curved bands
                upper_curve = (
                    abs((x / 0.55) ** 2 + ((y - 0.45) / 0.35) ** 2 - 1)
                    < 0.28
                    and x > -0.25
                )

                lower_curve = (
                    abs((x / 0.55) ** 2 + ((y + 0.45) / 0.35) ** 2 - 1)
                    < 0.28
                    and x > -0.25
                )

                middle_bar = (
                    abs(y) < 0.10
                    and -0.1 < x < 0.45
                )

                brightness = (
                    1.0
                    if upper_curve or lower_curve or middle_bar
                    else 0.0
                )

                pixel = Square(
                    side_length=0.14,
                    stroke_color=GREY_D,
                    stroke_width=0.35
                )

                pixel.set_fill(
                    interpolate_color(BLACK, WHITE, brightness),
                    opacity=1
                )

                pixel_grid.add(pixel)

        pixel_grid.arrange_in_grid(
            rows=28,
            cols=28,
            buff=0
        )

        pixel_grid.move_to(ORIGIN)

        self.play(
            FadeIn(pixel_grid),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # SHOW THE PIXEL DIMENSIONS
        # =====================================

        dimensions = MathTex(
            r"28 \times 28 = 784",
            font_size=44,
            color=YELLOW
        )

        dimensions.next_to(
            pixel_grid,
            RIGHT,
            buff=0.8
        )

        self.play(
            pixel_grid.animate.shift(LEFT * 1.5),
            FadeIn(dimensions)
        )

        self.next_slide()

        # =====================================
        # ZOOM IN ON THE PIXELS
        # =====================================

        self.play(
            FadeOut(dimensions),
            FadeOut(pixel_heading),
            pixel_grid.animate.scale(1.6).move_to(ORIGIN),
            run_time=2
        )

        pixel_label = Text(
            "Each square represents one pixel",
            font_size=30,
            color=YELLOW
        )

        pixel_label.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(pixel_label))

        self.next_slide()

        # =====================================
        # HIGHLIGHT A PIXEL
        # =====================================

        # Select a pixel near the centre of the grid
        selected_pixel = pixel_grid[14 * 28 + 18]

        highlight = SurroundingRectangle(
            selected_pixel,
            color=YELLOW,
            buff=0.02,
            stroke_width=4
        )

        self.play(Create(highlight))

        value_label = Text(
            "Pixel brightness: 0 to 1",
            font_size=30,
            color=WHITE
        )

        value_label.to_edge(UP, buff=0.4)

        self.play(Write(value_label))

        self.next_slide()

        # =====================================
        # INTRODUCING THE INPUT LAYER
        # =====================================

        self.play(
            FadeOut(highlight),
            FadeOut(pixel_label),
            FadeOut(value_label),
            pixel_grid.animate.scale(1 / 1.6).shift(LEFT * 2),
            run_time=1.5
        )

        # A visual summary of the input layer.
        # We show a few neurons and an ellipsis rather than
        # trying to fit all 784 circles on the screen.

        input_neurons = VGroup(
            *[
                Circle(
                    radius=0.16,
                    color=BLUE,
                    stroke_width=2
                )
                for _ in range(6)
            ]
        )

        input_neurons.arrange(
            DOWN,
            buff=0.22
        )

        input_neurons.shift(RIGHT * 3)

        ellipsis = Text(
            "...",
            font_size=32,
            color=WHITE
        )

        ellipsis.rotate(PI / 2)
        ellipsis.move_to(input_neurons.get_center())

        neuron_label = Text(
            "784 Input Neurons",
            font_size=30,
            color=YELLOW
        )

        neuron_label.next_to(
            input_neurons,
            DOWN,
            buff=0.4
        )

        arrow = Arrow(
            pixel_grid.get_right(),
            input_neurons.get_left(),
            buff=0.3,
            color=WHITE
        )

        self.play(GrowArrow(arrow))

        self.play(
            FadeIn(input_neurons),
            Write(neuron_label)
        )

        self.next_slide()
        
            # =====================================
        # FULL NEURAL NETWORK ARCHITECTURE
        # =====================================

        # Clear the previous pixel-grid animation
        self.play(
            FadeOut(pixel_grid),
            FadeOut(input_neurons),
            FadeOut(neuron_label),
            FadeOut(arrow)
        )

        heading = Text(
            "Inside Our Neural Network",
            font_size=40,
            color=YELLOW
        )
        heading.to_edge(UP, buff=0.45)

        self.play(Write(heading))

        # Helper function for drawing layers
        def make_layer(n, color, radius=0.11):
            neurons = VGroup(
                *[
                    Circle(
                        radius=radius,
                        stroke_color=color,
                        stroke_width=2,
                        fill_color=color,
                        fill_opacity=0.15
                    )
                    for _ in range(n)
                ]
            )

            neurons.arrange(DOWN, buff=0.12)
            return neurons

        # Input layer is visually compressed
        input_layer = make_layer(8, BLUE)

        hidden_1 = make_layer(16, WHITE)
        hidden_2 = make_layer(16, WHITE)
        output_layer = make_layer(10, GREEN)

        layers = VGroup(
            input_layer,
            hidden_1,
            hidden_2,
            output_layer
        )

        layers.arrange(RIGHT, buff=1.35)
        layers.move_to(DOWN * 0.15)

        # Labels
        input_label = Text(
            "784 Inputs",
            font_size=23,
            color=BLUE
        )

        hidden_1_label = Text(
            "16 Neurons",
            font_size=23
        )

        hidden_2_label = Text(
            "16 Neurons",
            font_size=23
        )

        output_label = Text(
            "10 Outputs",
            font_size=23,
            color=GREEN
        )

        labels = VGroup(
            input_label,
            hidden_1_label,
            hidden_2_label,
            output_label
        )

        for label, layer in zip(labels, layers):
            label.next_to(layer, DOWN, buff=0.35)

        # =====================================
        # ANIMATE LAYERS ONE AT A TIME
        # =====================================

        self.play(
            FadeIn(input_layer),
            Write(input_label)
        )

        self.next_slide()

        self.play(
            FadeIn(hidden_1),
            Write(hidden_1_label)
        )

        self.next_slide()

        self.play(
            FadeIn(hidden_2),
            Write(hidden_2_label)
        )

        self.next_slide()

        self.play(
            FadeIn(output_layer),
            Write(output_label)
        )

        self.next_slide()

        # =====================================
        # DRAW CONNECTIONS
        # =====================================

        connections = VGroup()

        for layer_a, layer_b in zip(layers[:-1], layers[1:]):

            for neuron_a in layer_a:
                for neuron_b in layer_b:

                    connection = Line(
                        neuron_a.get_center(),
                        neuron_b.get_center(),
                        color=GREY_B,
                        stroke_width=0.6,
                        stroke_opacity=0.3
                    )

                    connections.add(connection)

        # Connections behind neurons
        connections.set_z_index(-1)

        self.play(
            Create(connections),
            run_time=3
        )

        self.next_slide()

        # =====================================
        # HIGHLIGHT THE OUTPUT FOR DIGIT 3
        # =====================================

        digit_labels = VGroup()

        for i, neuron in enumerate(output_layer):

            digit_label = Text(
                str(i),
                font_size=15,
                color=WHITE
            )

            digit_label.next_to(
                neuron,
                RIGHT,
                buff=0.15
            )

            digit_labels.add(digit_label)

        self.play(FadeIn(digit_labels))

        self.next_slide()

        # Highlight neuron corresponding to digit 3
        chosen_neuron = output_layer[3]

        self.play(
            chosen_neuron.animate.set_fill(
                YELLOW,
                opacity=1
            ).set_stroke(YELLOW, width=3),
            digit_labels[3].animate.set_color(YELLOW),
            run_time=1.5
        )

        prediction = Text(
            "Predicted Digit: 3",
            font_size=32,
            color=YELLOW
        )

        prediction.to_edge(DOWN, buff=0.2)

        self.play(Write(prediction))

        self.next_slide()
        
                # =====================================
        # ZOOM INTO A SINGLE NEURON
        # =====================================

        self.play(
            FadeOut(heading),
            FadeOut(layers),
            FadeOut(labels),
            FadeOut(connections),
            FadeOut(digit_labels),
            FadeOut(prediction)
        )

        title = Text(
            "What Happens Inside a Neuron?",
            font_size=40,
            color=YELLOW
        )
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Three input neurons
        inputs = VGroup(
            *[
                Circle(
                    radius=0.25,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.2
                )
                for _ in range(3)
            ]
        )

        inputs.arrange(DOWN, buff=0.8)
        inputs.shift(LEFT * 4)

        # One output neuron
        neuron = Circle(
            radius=0.5,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.1
        )

        neuron.shift(RIGHT * 2)

        # Input values
        values = [0.5, 1.0, 0.2]

        input_labels = VGroup()

        for circle, value in zip(inputs, values):
            label = Text(
                str(value),
                font_size=26
            )
            label.move_to(circle)
            input_labels.add(label)

        # Connections
        weights = [0.8, -0.5, 1.0]

        arrows = VGroup()
        weight_labels = VGroup()

        for input_circle, weight in zip(inputs, weights):

            arrow = Arrow(
                input_circle.get_right(),
                neuron.get_left(),
                buff=0.1,
                stroke_width=3,
                color=GREY_B
            )

            arrows.add(arrow)

            weight_label = MathTex(
                f"{weight:g}",
                font_size=28,
                color=ORANGE
            )

            weight_label.move_to(
                arrow.get_center() + UP * 0.3
            )

            weight_labels.add(weight_label)

        # Animate inputs
        self.play(
            FadeIn(inputs),
            FadeIn(input_labels)
        )

        self.next_slide()

        # Animate neuron
        self.play(FadeIn(neuron))

        self.next_slide()

        # Animate weighted connections
        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            run_time=2
        )

        self.play(FadeIn(weight_labels))

        self.next_slide()

        # =====================================
        # WEIGHTED SUM
        # =====================================

        equation = MathTex(
            r"z = w_1x_1 + w_2x_2 + w_3x_3 + b",
            font_size=36
        )

        equation.to_edge(DOWN, buff=0.5)

        self.play(Write(equation))

        self.next_slide()

        substituted = MathTex(
            r"z = (0.8)(0.5) + (-0.5)(1) + (1)(0.2) + 0.4",
            font_size=32
        )

        substituted.move_to(equation)

        self.play(
            TransformMatchingTex(equation, substituted)
        )

        self.next_slide()

        result = MathTex(
            r"z = 0.5",
            font_size=44,
            color=YELLOW
        )

        result.move_to(substituted)

        self.play(
            ReplacementTransform(substituted, result)
        )

        self.next_slide()

        # =====================================
        # SIGMOID ACTIVATION
        # =====================================

        sigmoid = MathTex(
            r"\sigma(z) = \frac{1}{1+e^{-z}}",
            font_size=42
        )

        sigmoid.move_to(result)

        self.play(
            ReplacementTransform(result, sigmoid)
        )

        self.next_slide()

        activation = MathTex(
            r"\sigma(0.5) \approx 0.62",
            font_size=44,
            color=GREEN
        )

        activation.move_to(sigmoid)

        self.play(
            ReplacementTransform(sigmoid, activation)
        )

        self.play(
            neuron.animate.set_fill(
                GREEN,
                opacity=0.8
            ).set_stroke(GREEN)
        )

        self.next_slide()
            # =====================================
        # SIGMOID FUNCTION VISUALISATION
        # =====================================

        self.play(
            FadeOut(title),
            FadeOut(inputs),
            FadeOut(input_labels),
            FadeOut(neuron),
            FadeOut(arrows),
            FadeOut(weight_labels),
            FadeOut(activation)
        )

        sigmoid_title = Text(
            "The Sigmoid Activation Function",
            font_size=40,
            color=YELLOW
        )

        sigmoid_title.to_edge(UP, buff=0.4)

        axes = Axes(
            x_range=[-6, 6, 2],
            y_range=[0, 1, 0.2],
            x_length=9,
            y_length=4.5,
            axis_config={"include_numbers": True},
            tips=False
        )

        axes.shift(DOWN * 0.3)

        sigmoid_curve = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=BLUE,
            stroke_width=5
        )

        formula = MathTex(
            r"\sigma(z)=\frac{1}{1+e^{-z}}",
            font_size=36,
            color=YELLOW
        )

        formula.to_corner(UR, buff=0.4)

        self.play(Write(sigmoid_title))

        self.play(Create(axes))

        self.play(
            Create(sigmoid_curve),
            Write(formula),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # MOVING ALONG THE SIGMOID CURVE
        # =====================================

        def sigmoid_fn(x):
            return 1 / (1 + np.exp(-x))

        tracker = ValueTracker(-3)

        dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    sigmoid_fn(tracker.get_value())
                ),
                color=YELLOW,
                radius=0.1
            )
        )

        vertical_line = always_redraw(
            lambda: DashedLine(
                axes.c2p(tracker.get_value(), 0),
                axes.c2p(
                    tracker.get_value(),
                    sigmoid_fn(tracker.get_value())
                ),
                color=YELLOW
            )
        )

        # =====================================
        # LIVE SIGMOID VALUES — FIXED
        # =====================================

        input_text = Text(
            "Input:",
            font_size=24
        )

        input_number = DecimalNumber(
            tracker.get_value(),
            num_decimal_places=2,
            font_size=24
        )

        output_text = Text(
            "Output:",
            font_size=24
        )

        output_number = DecimalNumber(
            sigmoid_fn(tracker.get_value()),
            num_decimal_places=2,
            font_size=24,
            color=GREEN
        )

        # Update only the numbers, not the text
        input_number.add_updater(
            lambda m: m.set_value(tracker.get_value())
        )

        output_number.add_updater(
            lambda m: m.set_value(
                sigmoid_fn(tracker.get_value())
            )
        )

        value_display = VGroup(
            input_text,
            input_number,
            output_text,
            output_number
        )

        value_display.arrange(
            RIGHT,
            buff=0.2
        )

        value_display.to_edge(
            DOWN,
            buff=0.2
        )
        value_display.arrange(RIGHT, buff=0.2).to_edge(DOWN, buff=0.2)

        self.add(dot, vertical_line, value_display)

        self.next_slide()

        # Input = 0
        self.play(
            tracker.animate.set_value(0),
            run_time=2
        )

        self.next_slide()

        # Input = 3
        self.play(
            tracker.animate.set_value(3),
            run_time=2
        )

        self.next_slide()

        # Return to our example: z = 0.5
        self.play(
            tracker.animate.set_value(0.5),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # HIGHLIGHT THE RESULT
        # =====================================

        result_text = MathTex(
            r"\sigma(0.5)\approx0.62",
            font_size=42,
            color=GREEN
        )

        result_text.to_edge(DOWN, buff=0.8)

        self.play(
            FadeOut(value_display),
            Write(result_text)
        )

        self.next_slide()
            # =====================================
        # FORWARD PROPAGATION
        # =====================================

        # Clear sigmoid graph
        self.play(
            FadeOut(sigmoid_title),
            FadeOut(axes),
            FadeOut(sigmoid_curve),
            FadeOut(formula),
            FadeOut(dot),
            FadeOut(vertical_line),
            FadeOut(result_text)
        )

        heading = Text(
            "Forward Propagation",
            font_size=42,
            color=YELLOW
        )
        heading.to_edge(UP, buff=0.4)

        self.play(Write(heading))

        # =====================================
        # CREATE NETWORK
        # =====================================

        def create_neuron_layer(n, color):
            neurons = VGroup(
                *[
                    Circle(
                        radius=0.105,
                        stroke_color=color,
                        stroke_width=2,
                        fill_color=color,
                        fill_opacity=0.1
                    )
                    for _ in range(n)
                ]
            )
            neurons.arrange(DOWN, buff=0.13)
            return neurons

        input_layer = create_neuron_layer(8, BLUE)
        hidden_1 = create_neuron_layer(16, WHITE)
        hidden_2 = create_neuron_layer(16, WHITE)
        output_layer = create_neuron_layer(10, GREEN)

        layers = VGroup(
            input_layer,
            hidden_1,
            hidden_2,
            output_layer
        )

        layers.arrange(RIGHT, buff=1.5)
        layers.move_to(DOWN * 0.15)

        # Connections
        connections = VGroup()

        for layer_a, layer_b in zip(layers[:-1], layers[1:]):
            for neuron_a in layer_a:
                for neuron_b in layer_b:

                    line = Line(
                        neuron_a.get_center(),
                        neuron_b.get_center(),
                        stroke_color=GREY_B,
                        stroke_width=0.6,
                        stroke_opacity=0.2
                    )

                    connections.add(line)

        connections.set_z_index(-1)

        # Labels
        layer_labels = VGroup(
            Text("784 Inputs", font_size=22, color=BLUE),
            Text("16 Neurons", font_size=22),
            Text("16 Neurons", font_size=22),
            Text("10 Outputs", font_size=22, color=GREEN)
        )

        for label, layer in zip(layer_labels, layers):
            label.next_to(layer, DOWN, buff=0.35)

        self.play(
            FadeIn(connections),
            FadeIn(layers),
            FadeIn(layer_labels),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # ANIMATE ACTIVATIONS
        # =====================================

        # Input layer activates
        self.play(
            *[
                neuron.animate.set_fill(BLUE, opacity=0.85)
                for neuron in input_layer
            ],
            run_time=1
        )

        self.next_slide()

        # First hidden layer activates
        self.play(
            *[
                neuron.animate.set_fill(YELLOW, opacity=0.75)
                for neuron in hidden_1
            ],
            run_time=1
        )

        self.next_slide()

        # Second hidden layer activates
        self.play(
            *[
                neuron.animate.set_fill(ORANGE, opacity=0.75)
                for neuron in hidden_2
            ],
            run_time=1
        )

        self.next_slide()

        # Output layer activates
        self.play(
            *[
                neuron.animate.set_fill(GREEN, opacity=0.4)
                for neuron in output_layer
            ],
            run_time=1
        )

        self.next_slide()

        # =====================================
        # OUTPUT PROBABILITIES
        # =====================================

        probabilities = [
            0.01, 0.01, 0.02, 0.87, 0.01,
            0.02, 0.01, 0.02, 0.02, 0.01
        ]

        probability_labels = VGroup()

        for i, (neuron, prob) in enumerate(
            zip(output_layer, probabilities)
        ):
            label = Text(
                f"{i}: {prob:.2f}",
                font_size=16,
                color=YELLOW if i == 3 else WHITE
            )

            label.next_to(
                neuron,
                RIGHT,
                buff=0.2
            )

            probability_labels.add(label)

        self.play(FadeIn(probability_labels))

        # Highlight digit 3
        self.play(
            output_layer[3].animate.set_fill(
                YELLOW,
                opacity=1
            ).set_stroke(YELLOW, width=3),
            run_time=1.5
        )

        self.next_slide()

        # =====================================
        # FINAL PREDICTION
        # =====================================

        prediction = Text(
            "Prediction: 3",
            font_size=38,
            color=YELLOW
        )

        prediction.to_edge(DOWN, buff=0.15)

        self.play(Write(prediction))

        self.next_slide()
        
            # =====================================
        # TRANSITION TO QUESTION 2
        # =====================================

        # Clear forward propagation animation
        self.play(
            FadeOut(heading),
            FadeOut(connections),
            FadeOut(layers),
            FadeOut(layer_labels),
            FadeOut(probability_labels),
            FadeOut(prediction),
            run_time=1.5
        )

        # =====================================
        # THE BIG QUESTION
        # =====================================

        question = Text(
            "Who decided what all those\n"
            "weights and biases should be?",
            font_size=44,
            color=YELLOW,
            line_spacing=1.2
        )

        question.move_to(ORIGIN)

        self.play(
            Write(question),
            run_time=2.5
        )

        self.next_slide()

        # =====================================
        # THE INITIAL WEIGHTS
        # =====================================

        self.play(FadeOut(question))

        initial_title = Text(
            "Where Do the Weights Come From?",
            font_size=40,
            color=YELLOW
        )

        initial_title.to_edge(UP, buff=0.6)

        weights = VGroup(
            MathTex(r"w_1 = 0.24", font_size=40),
            MathTex(r"w_2 = -0.71", font_size=40),
            MathTex(r"w_3 = 0.13", font_size=40),
            MathTex(r"b = 0.05", font_size=40)
        )

        weights.arrange(DOWN, buff=0.45)
        weights.move_to(ORIGIN)

        self.play(Write(initial_title))

        self.play(
            LaggedStart(
                *[FadeIn(w, shift=UP * 0.2) for w in weights],
                lag_ratio=0.3
            )
        )

        self.next_slide()

        # Reveal
        random_text = Text(
            "We typically start with random weights.",
            font_size=34,
            color=GREEN
        )

        random_text.to_edge(DOWN, buff=0.5)

        self.play(Write(random_text))

        self.next_slide()

        # =====================================
        # QUESTION 2 TITLE
        # =====================================

        self.play(
            FadeOut(initial_title),
            FadeOut(weights),
            FadeOut(random_text)
        )

        section_number = Text(
            "QUESTION 2",
            font_size=34,
            color=GREY_B
        )

        section_title = Text(
            "How Does a Neural Network\nActually Learn?",
            font_size=46,
            color=YELLOW,
            line_spacing=1.2
        )

        section_group = VGroup(
            section_number,
            section_title
        )

        section_group.arrange(DOWN, buff=0.5)
        section_group.move_to(ORIGIN)

        self.play(
            Write(section_number),
            run_time=1
        )

        self.play(
            Write(section_title),
            run_time=2
        )

        self.next_slide()
        
                # =====================================
        # QUESTION 2 — THE NETWORK GETS IT WRONG
        # =====================================

        self.play(FadeOut(section_group))

        heading = Text(
            "What Happens When the Network Gets It Wrong?",
            font_size=36,
            color=YELLOW
        )
        heading.to_edge(UP, buff=0.5)

        self.play(Write(heading))

        # Handwritten digit
        digit = Text(
            "3",
            font="Segoe Print",
            font_size=180,
            color=WHITE
        )

        digit.shift(LEFT * 4)

        self.play(Write(digit), run_time=1.5)

        self.next_slide()

        # =====================================
        # OUTPUT PROBABILITIES
        # =====================================

        probabilities = [
            0.01, 0.01, 0.02, 0.15, 0.01,
            0.02, 0.01, 0.02, 0.74, 0.01
        ]

        bars = VGroup()
        labels = VGroup()

        for i, probability in enumerate(probabilities):

            bar = Rectangle(
                width=probability * 5,
                height=0.32,
                fill_color=RED if i == 8 else BLUE,
                fill_opacity=0.8,
                stroke_width=0
            )

            bar.move_to(
                RIGHT * 0.5 + DOWN * (i - 4.5) * 0.5,
                aligned_edge=LEFT
            )

            label = Text(
                str(i),
                font_size=22,
                color=WHITE
            )

            label.next_to(bar, LEFT, buff=0.25)

            value = Text(
                f"{probability:.0%}",
                font_size=18
            )

            value.next_to(bar, RIGHT, buff=0.15)

            bars.add(bar)
            labels.add(label, value)

        self.play(
            LaggedStart(
                *[GrowFromEdge(bar, LEFT) for bar in bars],
                lag_ratio=0.1
            ),
            FadeIn(labels),
            run_time=2.5
        )

        self.next_slide()

        # =====================================
        # WRONG PREDICTION
        # =====================================

        prediction = Text(
            "Prediction: 8",
            font_size=36,
            color=RED
        )

        prediction.to_edge(DOWN, buff=0.3)

        self.play(Write(prediction))

        self.next_slide()

        # =====================================
        # REVEAL CORRECT ANSWER
        # =====================================

        correct = Text(
            "Correct Answer: 3",
            font_size=32,
            color=GREEN
        )

        correct.next_to(
            prediction,
            UP,
            buff=0.3
        )

        self.play(Write(correct))

        self.next_slide()

        # =====================================
        # INTRODUCE LOSS
        # =====================================

        self.play(
            FadeOut(heading),
            FadeOut(digit),
            FadeOut(bars),
            FadeOut(labels),
            FadeOut(prediction),
            FadeOut(correct)
        )

        question = Text(
            "How wrong was our prediction?",
            font_size=44,
            color=YELLOW
        )

        self.play(Write(question))

        self.next_slide()
        
                # =====================================
        # CROSS-ENTROPY LOSS
        # =====================================

        self.play(FadeOut(question))

        loss_title = Text(
            "Measuring Our Mistakes",
            font_size=42,
            color=YELLOW
        )

        loss_title.to_edge(UP, buff=0.5)

        self.play(Write(loss_title))

        # Introduce the loss function
        loss_equation = MathTex(
            r"L=-\log(p_{\text{correct}})",
            font_size=60
        )

        loss_equation.move_to(ORIGIN)

        self.play(
            Write(loss_equation),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # SUBSTITUTE THE PROBABILITY
        # =====================================

        substitution = MathTex(
            r"L=-\log(0.15)",
            font_size=60
        )

        substitution.move_to(loss_equation)

        self.play(
            ReplacementTransform(
                loss_equation,
                substitution
            )
        )

        self.next_slide()

        # Calculate loss
        loss_result = MathTex(
            r"L\approx1.90",
            font_size=64,
            color=RED
        )

        loss_result.move_to(substitution)

        self.play(
            ReplacementTransform(
                substitution,
                loss_result
            )
        )

        self.next_slide()

        # =====================================
        # LOSS FUNCTION GRAPH
        # =====================================

        self.play(FadeOut(loss_result))

        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 4, 1],
            x_length=9,
            y_length=4.5,
            tips=False,
            axis_config={
                "include_numbers": True
            }
        )

        axes.shift(DOWN * 0.3)

        x_label = Text(
            "Probability of Correct Answer",
            font_size=24
        )

        x_label.next_to(
            axes,
            DOWN,
            buff=0.5
        )

        y_label = Text(
            "Loss",
            font_size=26
        )

        y_label.next_to(
            axes,
            LEFT,
            buff=0.4
        )

        loss_curve = axes.plot(
            lambda p: -np.log(p),
            x_range=[0.02, 1],
            color=BLUE,
            stroke_width=5,
            use_smoothing=False
        )

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label)
        )

        self.play(
            Create(loss_curve),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # SHOW ORIGINAL PREDICTION
        # =====================================

        original_p = 0.15
        original_loss = -np.log(original_p)

        original_dot = Dot(
            axes.c2p(original_p, original_loss),
            color=RED,
            radius=0.12
        )

        original_label = MathTex(
            r"p=0.15,\quad L\approx1.90",
            font_size=30,
            color=RED
        )

        original_label.to_corner(UR, buff=0.5)
        original_label.shift(DOWN * 0.8)

        self.play(
            FadeIn(original_dot),
            Write(original_label)
        )

        self.next_slide()

        # =====================================
        # IMPROVED PREDICTION
        # =====================================

        improved_p = 0.90
        improved_loss = -np.log(improved_p)

        improved_dot = Dot(
            axes.c2p(improved_p, improved_loss),
            color=GREEN,
            radius=0.12
        )

        improved_label = MathTex(
            r"p=0.90,\quad L\approx0.105",
            font_size=30,
            color=GREEN
        )

        improved_label.next_to(
            original_label,
            DOWN,
            buff=0.35
        )

        self.play(
            TransformFromCopy(
                original_dot,
                improved_dot
            ),
            Write(improved_label),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # THE KEY IDEA
        # =====================================

        takeaway = Text(
            "Better predictions = Lower loss",
            font_size=34,
            color=YELLOW
        )

        takeaway.to_edge(DOWN, buff=0.15)

        self.play(Write(takeaway))

        self.next_slide()
        
                # =====================================
        # GRADIENT DESCENT — PROFESSOR ROBOT
        # =====================================

        # Clear the previous loss graph
        self.play(
            FadeOut(loss_title),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(loss_curve),
            FadeOut(original_dot),
            FadeOut(original_label),
            FadeOut(improved_dot),
            FadeOut(improved_label),
            FadeOut(takeaway)
        )

        gd_title = Text(
            "How Do We Reduce the Loss?",
            font_size=40,
            color=YELLOW
        )
        gd_title.to_edge(UP, buff=0.4)

        self.play(Write(gd_title))

        # =====================================
        # CREATE LOSS LANDSCAPE
        # =====================================

        gd_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 5, 1],
            x_length=10,
            y_length=4.5,
            tips=False,
            axis_config={
                "include_numbers": False
            }
        )

        gd_axes.shift(DOWN * 0.4)

        def loss_function(w):
            return 0.25 * w**2 + 0.5

        loss_landscape = gd_axes.plot(
            loss_function,
            x_range=[-4, 4],
            color=BLUE,
            stroke_width=5
        )

        weight_label = Text(
            "Weight",
            font_size=25
        )
        weight_label.next_to(gd_axes, DOWN, buff=0.25)

        loss_axis_label = Text(
            "Loss",
            font_size=25
        )
        loss_axis_label.next_to(gd_axes, LEFT, buff=0.2)

        self.play(
            Create(gd_axes),
            Write(weight_label),
            Write(loss_axis_label)
        )

        self.play(
            Create(loss_landscape),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # INTRODUCE PROFESSOR ROBOT
        # =====================================

        robot = ConfusedRobot(
            body_color=PURPLE_B,
            scale_factor=0.45
        )

        # Start on the right side of the curve
        start_weight = 3.5

        robot.move_to(
            gd_axes.c2p(
                start_weight,
                loss_function(start_weight)
            ) + UP * 0.65
        )

        self.play(
            FadeIn(robot, shift=UP * 0.3)
        )

        self.play(robot.confused_face())

        self.next_slide()

        # =====================================
        # WHAT IS OUR GOAL?
        # =====================================

        goal_text = Text(
            "Goal: Find the lowest loss!",
            font_size=30,
            color=GREEN
        )

        goal_text.to_corner(UR, buff=0.5)
        goal_text.shift(DOWN * 0.6)

        minimum_dot = Dot(
            gd_axes.c2p(0, loss_function(0)),
            color=GREEN,
            radius=0.12
        )

        self.play(
            Write(goal_text),
            FadeIn(minimum_dot)
        )

        self.next_slide()

        # =====================================
        # ROBOT WALKS DOWNHILL
        # =====================================

        # Gradient descent update:
        # w_new = w_old - learning_rate * gradient

        learning_rate = 0.8
        current_weight = start_weight

        for step in range(8):

            gradient = 0.5 * current_weight

            new_weight = (
                current_weight
                - learning_rate * gradient
            )

            target_position = (
                gd_axes.c2p(
                    new_weight,
                    loss_function(new_weight)
                )
                + UP * 0.65
            )

            self.play(
                robot.animate.move_to(target_position),
                run_time=0.7
            )

            current_weight = new_weight

        self.next_slide()

        # =====================================
        # ROBOT CELEBRATES
        # =====================================

        self.play(robot.happy_face())

        success_text = Text(
            "Lower Loss!",
            font_size=36,
            color=GREEN
        )

        success_text.next_to(
            robot,
            RIGHT,
            buff=0.5
        )

        self.play(
            Write(success_text),
            robot.small_bounce()
        )

        self.next_slide()
        
        
                # =====================================
        # THE MATHEMATICS OF GRADIENT DESCENT
        # =====================================

        # Update the title
        new_title = Text(
            "The Mathematics of Gradient Descent",
            font_size=38,
            color=YELLOW
        )
        new_title.to_edge(UP, buff=0.4)

        self.play(
            ReplacementTransform(gd_title, new_title),
            FadeOut(goal_text),
            FadeOut(success_text)
        )

        self.next_slide()

        # =====================================
        # 1. WHAT IS THE GRADIENT?
        # =====================================

        gradient_question = Text(
            "1. Which direction is uphill?",
            font_size=28,
            color=YELLOW
        )
        gradient_question.to_corner(UL, buff=0.5)
        gradient_question.shift(DOWN * 0.65)

        self.play(Write(gradient_question))

        # Show a tangent line at a point on the curve
        example_weight = 2.5

        tangent_point = gd_axes.c2p(
            example_weight,
            loss_function(example_weight)
        )

        gradient_value = 0.5 * example_weight

        # Construct a tangent line in graph coordinates
        tangent_line = Line(
            gd_axes.c2p(
                example_weight - 0.7,
                loss_function(example_weight)
                - gradient_value * 0.7
            ),
            gd_axes.c2p(
                example_weight + 0.7,
                loss_function(example_weight)
                + gradient_value * 0.7
            ),
            color=RED,
            stroke_width=4
        )

        tangent_dot = Dot(
            tangent_point,
            color=RED,
            radius=0.1
        )

        self.play(
            Create(tangent_line),
            FadeIn(tangent_dot)
        )

        gradient_label = MathTex(
            r"\frac{dL}{dw}=1.25",
            font_size=34,
            color=RED
        )
        gradient_label.to_corner(UR, buff=0.5)
        gradient_label.shift(DOWN * 0.7)

        self.play(Write(gradient_label))

        self.next_slide()

        # =====================================
        # 2. THE LEARNING RATE
        # =====================================

        self.play(
            FadeOut(gradient_question),
            FadeOut(tangent_line),
            FadeOut(tangent_dot),
            FadeOut(gradient_label)
        )

        learning_question = Text(
            "2. How big should our step be?",
            font_size=28,
            color=YELLOW
        )
        learning_question.to_corner(UL, buff=0.5)
        learning_question.shift(DOWN * 0.65)

        self.play(Write(learning_question))

        learning_equation = MathTex(
            r"\eta=0.8",
            font_size=44,
            color=GREEN
        )

        learning_equation.to_corner(UR, buff=0.5)
        learning_equation.shift(DOWN * 0.7)

        self.play(Write(learning_equation))

        self.next_slide()

        # =====================================
        # 3. THE UPDATE RULE
        # =====================================

        self.play(
            FadeOut(learning_question),
            FadeOut(learning_equation),
            FadeOut(gd_axes),
            FadeOut(loss_landscape),
            FadeOut(weight_label),
            FadeOut(loss_axis_label),
            FadeOut(minimum_dot),
            FadeOut(robot)
        )

        update_title = Text(
            "Putting It All Together",
            font_size=36,
            color=YELLOW
        )
        update_title.move_to(UP * 2)

        self.play(
            ReplacementTransform(new_title, update_title)
        )

        # The gradient descent equation
        update_equation = MathTex(
            r"w_{\text{new}}",
            r"=",
            r"w_{\text{old}}",
            r"-",
            r"\eta",
            r"\frac{\partial L}{\partial w}",
            font_size=60
        )

        update_equation.move_to(ORIGIN)

        # Colour the components
        update_equation[0].set_color(GREEN)
        update_equation[2].set_color(BLUE)
        update_equation[4].set_color(YELLOW)
        update_equation[5].set_color(RED)

        self.play(
            LaggedStart(
                *[
                    Write(part)
                    for part in update_equation
                ],
                lag_ratio=0.25
            ),
            run_time=3
        )

        self.next_slide()

        # =====================================
        # EXPLAIN EACH COMPONENT
        # =====================================

        explanation = VGroup(
            Text(
                "Current weight",
                font_size=24,
                color=BLUE
            ),
            Text(
                "Learning rate",
                font_size=24,
                color=YELLOW
            ),
            Text(
                "Gradient (slope)",
                font_size=24,
                color=RED
            )
        )

        explanation.arrange(DOWN, buff=0.25)
        explanation.to_edge(DOWN, buff=0.5)

        self.play(
            Write(explanation[0]),
            Indicate(update_equation[2], color=BLUE)
        )

        self.next_slide()

        self.play(
            Write(explanation[1]),
            Indicate(update_equation[4], color=YELLOW)
        )

        self.next_slide()

        self.play(
            Write(explanation[2]),
            Indicate(update_equation[5], color=RED)
        )

        self.next_slide()

        # =====================================
        # NUMERICAL EXAMPLE
        # =====================================

        self.play(
            FadeOut(explanation),
            FadeOut(update_equation)
        )

        example_title = Text(
            "One Step of Gradient Descent",
            font_size=36,
            color=YELLOW
        )
        example_title.move_to(UP * 2)

        self.play(
            ReplacementTransform(update_title, example_title)
        )

        numerical_example = VGroup(
            MathTex(
                r"w_{\text{old}}=2.5",
                font_size=42
            ),
            MathTex(
                r"\frac{dL}{dw}=1.25",
                font_size=42
            ),
            MathTex(
                r"\eta=0.8",
                font_size=42
            )
        )

        numerical_example.arrange(DOWN, buff=0.4)
        numerical_example.move_to(UP * 0.4)

        self.play(
            LaggedStart(
                *[Write(item) for item in numerical_example],
                lag_ratio=0.3
            )
        )

        self.next_slide()

        calculation = MathTex(
            r"w_{\text{new}}=2.5-0.8(1.25)",
            font_size=46
        )
        calculation.move_to(DOWN * 1.2)

        self.play(Write(calculation))

        self.next_slide()

        answer = MathTex(
            r"w_{\text{new}}=1.5",
            font_size=54,
            color=GREEN
        )
        answer.move_to(calculation)

        self.play(
            ReplacementTransform(calculation, answer)
        )

        self.next_slide()
        
                # =====================================
        # BACKPROPAGATION
        # =====================================

        # Clear previous gradient descent example
        self.play(
            FadeOut(example_title),
            FadeOut(numerical_example),
            FadeOut(answer)
        )

        backprop_title = Text(
            "How Does the Network Learn?",
            font_size=42,
            color=YELLOW
        )

        backprop_title.to_edge(UP, buff=0.4)

        self.play(Write(backprop_title))

        # =====================================
        # BUILD THE NETWORK
        # =====================================

        def make_layer(n, color):
            neurons = VGroup(
                *[
                    Circle(
                        radius=0.11,
                        stroke_color=color,
                        stroke_width=2,
                        fill_color=color,
                        fill_opacity=0.15
                    )
                    for _ in range(n)
                ]
            )

            neurons.arrange(DOWN, buff=0.18)

            return neurons

        bp_input = make_layer(8, BLUE)
        bp_hidden1 = make_layer(12, WHITE)
        bp_hidden2 = make_layer(12, WHITE)
        bp_output = make_layer(10, GREEN)

        bp_layers = VGroup(
            bp_input,
            bp_hidden1,
            bp_hidden2,
            bp_output
        )

        bp_layers.arrange(RIGHT, buff=1.6)
        bp_layers.move_to(DOWN * 0.2)

        # Create connections
        bp_connections = VGroup()

        for layer_a, layer_b in zip(
            bp_layers[:-1],
            bp_layers[1:]
        ):
            for neuron_a in layer_a:
                for neuron_b in layer_b:

                    connection = Line(
                        neuron_a.get_center(),
                        neuron_b.get_center(),
                        color=GREY_B,
                        stroke_width=0.6,
                        stroke_opacity=0.2
                    )

                    bp_connections.add(connection)

        bp_connections.set_z_index(-1)

        # Layer labels
        bp_labels = VGroup(
            Text("Input", font_size=23, color=BLUE),
            Text("Hidden 1", font_size=23),
            Text("Hidden 2", font_size=23),
            Text("Output", font_size=23, color=GREEN)
        )

        for label, layer in zip(bp_labels, bp_layers):
            label.next_to(layer, DOWN, buff=0.3)

        self.play(
            FadeIn(bp_connections),
            FadeIn(bp_layers),
            FadeIn(bp_labels),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # FORWARD PROPAGATION
        # =====================================

        forward_text = Text(
            "Forward Propagation",
            font_size=30,
            color=GREEN
        )

        forward_text.to_edge(DOWN, buff=0.25)

        self.play(Write(forward_text))

        # Animate layers from left to right
        for layer in bp_layers:

            self.play(
                *[
                    neuron.animate.set_fill(
                        GREEN,
                        opacity=0.85
                    )
                    for neuron in layer
                ],
                run_time=0.55
            )

        self.next_slide()

        # =====================================
        # CALCULATE LOSS
        # =====================================

        loss_text = MathTex(
            r"L=-\log(p_{\text{correct}})",
            font_size=35,
            color=RED
        )

        loss_text.next_to(
            bp_output,
            RIGHT,
            buff=0.5
        )

        self.play(
            FadeOut(forward_text),
            Write(loss_text)
        )

        self.next_slide()

        # =====================================
        # BACKPROPAGATION
        # =====================================

        backward_text = Text(
            "Backpropagation",
            font_size=32,
            color=RED
        )

        backward_text.to_edge(DOWN, buff=0.25)

        self.play(Write(backward_text))

        # Animate layers in reverse
        for layer in reversed(bp_layers):

            self.play(
                *[
                    neuron.animate.set_fill(
                        RED,
                        opacity=0.85
                    )
                    for neuron in layer
                ],
                run_time=0.55
            )

        self.next_slide()

        # =====================================
        # THE CHAIN RULE
        # =====================================

        self.play(
            FadeOut(bp_connections),
            FadeOut(bp_layers),
            FadeOut(bp_labels),
            FadeOut(loss_text),
            FadeOut(backward_text)
        )

        chain_title = Text(
            "The Mathematics Behind Backpropagation",
            font_size=38,
            color=YELLOW
        )

        self.play(
            ReplacementTransform(
                backprop_title,
                chain_title
            )
        )

        chain_rule = MathTex(
            r"\frac{\partial L}{\partial w}"
            r"="
            r"\frac{\partial L}{\partial a}"
            r"\cdot"
            r"\frac{\partial a}{\partial w}",
            font_size=58
        )

        chain_rule.move_to(ORIGIN)

        self.play(
            Write(chain_rule),
            run_time=2.5
        )

        self.next_slide()

        # =====================================
        # EXPLAIN THE CHAIN RULE
        # =====================================
        self.play(
            FadeOut(chain_title)
        )

        explanation = VGroup(
            Text(
                "How does the activation affect loss?",
                font_size=28,
                color=BLUE
            ),
            Text(
                "How does the weight affect activation?",
                font_size=28,
                color=GREEN
            )
        )

        explanation.arrange(DOWN, buff=0.4)
        explanation.to_edge(DOWN, buff=0.5)

        self.play(Write(explanation[0]))
        self.next_slide()

        self.play(Write(explanation[1]))
        self.next_slide()

        # =====================================
        # CONNECT BACK TO GRADIENT DESCENT
        # =====================================

        self.play(
            FadeOut(explanation),
            FadeOut(chain_rule)
        )

        final_equation = MathTex(
            r"w_{\text{new}}"
            r"="
            r"w_{\text{old}}"
            r"-"
            r"\eta"
            r"\frac{\partial L}{\partial w}",
            font_size=56
        )

        final_equation.move_to(ORIGIN)

        self.play(Write(final_equation))

        takeaway = Text(
            "Backpropagation calculates the gradients.",
            font_size=29,
            color=BLUE
        )

        takeaway2 = Text(
            "Gradient descent updates the weights.",
            font_size=29,
            color=GREEN
        )

        takeaway_group = VGroup(
            takeaway,
            takeaway2
        )

        takeaway_group.arrange(DOWN, buff=0.3)
        takeaway_group.to_edge(DOWN, buff=0.45)

        self.play(Write(takeaway))
        self.next_slide()

        self.play(Write(takeaway2))
        self.next_slide()
        
                # =====================================
        # THE COMPLETE TRAINING CYCLE
        # =====================================

        # Clear backpropagation explanation
        self.play(
            FadeOut(chain_title),
            FadeOut(final_equation),
            FadeOut(takeaway_group)
        )

        cycle_title = Text(
            "How a Neural Network Learns",
            font_size=42,
            color=YELLOW
        )
        cycle_title.to_edge(UP, buff=0.4)

        self.play(Write(cycle_title))

        # =====================================
        # CREATE TRAINING PIPELINE
        # =====================================

        stages = [
            "Input",
            "Prediction",
            "Loss",
            "Gradients",
            "Update"
        ]

        stage_boxes = VGroup()

        for stage in stages:

            box = RoundedRectangle(
                width=1.8,
                height=0.85,
                corner_radius=0.15,
                stroke_color=WHITE,
                stroke_width=2,
                fill_color=BLUE_E,
                fill_opacity=0.35
            )

            label = Text(
                stage,
                font_size=22,
                color=WHITE
            )

            label.move_to(box)

            stage_boxes.add(
                VGroup(box, label)
            )

        stage_boxes.arrange(RIGHT, buff=0.55)
        stage_boxes.move_to(UP * 1.25)

        # Arrows connecting the stages
        stage_arrows = VGroup()

        for i in range(len(stage_boxes) - 1):

            arrow = Arrow(
                stage_boxes[i].get_right(),
                stage_boxes[i + 1].get_left(),
                buff=0.08,
                stroke_width=3,
                color=GREY_B,
                max_tip_length_to_length_ratio=0.3
            )

            stage_arrows.add(arrow)

        self.play(
            LaggedStart(
                *[FadeIn(box) for box in stage_boxes],
                lag_ratio=0.15
            ),
            run_time=2
        )

        self.play(
            Create(stage_arrows),
            run_time=1.5
        )

        self.next_slide()

        # =====================================
        # CREATE LOSS GRAPH
        # =====================================

        train_axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 2.5, 0.5],
            x_length=8,
            y_length=3,
            tips=False,
            axis_config={
                "include_numbers": True,
                "font_size": 20
            }
        )

        train_axes.move_to(DOWN * 1.45)

        iteration_label = Text(
            "Training Iteration",
            font_size=22
        )
        iteration_label.next_to(
            train_axes,
            DOWN,
            buff=0.3
        )

        loss_label = Text(
            "Loss",
            font_size=22
        )
        loss_label.next_to(
            train_axes,
            LEFT,
            buff=0.25
        )

        self.play(
            Create(train_axes),
            Write(iteration_label),
            Write(loss_label)
        )

        self.next_slide()

        # =====================================
        # ANIMATE TRAINING
        # =====================================

        # Illustrative decreasing loss values
        losses = [
            2.2,
            1.85,
            1.55,
            1.3,
            1.05,
            0.85,
            0.68,
            0.55,
            0.43,
            0.35,
            0.28
        ]

        loss_points = [
            train_axes.c2p(i, loss)
            for i, loss in enumerate(losses)
        ]

        training_curve = VMobject(
            color=GREEN,
            stroke_width=5
        )

        training_curve.set_points_as_corners(
            [loss_points[0], loss_points[0]]
        )

        training_dot = Dot(
            loss_points[0],
            color=YELLOW,
            radius=0.09
        )

        self.add(training_curve, training_dot)

        # Animate the first training iteration
        for stage in stage_boxes:

            self.play(
                stage[0].animate.set_fill(
                    YELLOW,
                    opacity=0.6
                ),
                run_time=0.2
            )

            self.play(
                stage[0].animate.set_fill(
                    BLUE_E,
                    opacity=0.35
                ),
                run_time=0.15
            )

        self.next_slide()

        # =====================================
        # LOSS DECREASES
        # =====================================

        for i in range(1, len(loss_points)):

            new_curve = VMobject(
                color=GREEN,
                stroke_width=5
            )

            new_curve.set_points_as_corners(
                loss_points[:i + 1]
            )

            self.play(
                Transform(
                    training_curve,
                    new_curve
                ),
                training_dot.animate.move_to(
                    loss_points[i]
                ),
                run_time=0.35
            )

        self.next_slide()

        # =====================================
        # FINAL MESSAGE
        # =====================================

        learning_text = Text(
            "The Network Is Learning!",
            font_size=38,
            color=GREEN
        )

        learning_text.to_edge(DOWN, buff=0.15)

        self.play(
            Write(learning_text),
            run_time=1.5
        )

        self.next_slide()
        
                # =====================================
        # QUESTION 3 — ACCURACY VS ROBUSTNESS
        # =====================================

        # Clear Question 3 title
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

        # =====================================
        # 98% ACCURACY
        # =====================================

        accuracy_title = Text(
            "Our Neural Network",
            font_size=38,
            color=WHITE
        )

        accuracy_number = Text(
            "98%",
            font_size=110,
            color=GREEN
        )

        accuracy_label = Text(
            "Accuracy",
            font_size=38,
            color=GREEN
        )

        accuracy_group = VGroup(
            accuracy_title,
            accuracy_number,
            accuracy_label
        )

        accuracy_group.arrange(DOWN, buff=0.3)
        accuracy_group.move_to(ORIGIN)

        self.play(Write(accuracy_title))

        self.play(
            FadeIn(accuracy_number, scale=1.5),
            run_time=1.5
        )

        self.play(Write(accuracy_label))

        self.next_slide()

        # =====================================
        # INTRODUCE HANDWRITTEN DIGIT
        # =====================================

        self.play(
            accuracy_group.animate.scale(0.45).to_corner(
                UL,
                buff=0.5
            )
        )

        digit_title = Text(
            "Let's Test It",
            font_size=38,
            color=YELLOW
        )

        digit_title.to_edge(UP, buff=0.4)

        digit = Text(
            "3",
            font="Segoe Print",
            font_size=190,
            color=WHITE
        )

        digit.move_to(LEFT * 2)

        digit_box = RoundedRectangle(
            width=3,
            height=3.5,
            corner_radius=0.2,
            stroke_color=BLUE,
            stroke_width=3
        )

        digit_box.move_to(digit)

        self.play(
            Write(digit_title),
            Create(digit_box),
            Write(digit),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # CORRECT PREDICTION
        # =====================================

        prediction_label = Text(
            "Network Prediction",
            font_size=28,
            color=WHITE
        )

        prediction_label.move_to(
            RIGHT * 3 + UP * 0.6
        )

        prediction_number = Text(
            "3",
            font_size=100,
            color=GREEN
        )

        prediction_number.next_to(
            prediction_label,
            DOWN,
            buff=0.3
        )

        correct_symbol = Text(
            "Correct!",
            font_size=30,
            color=GREEN
        )

        correct_symbol.next_to(
            prediction_number,
            DOWN,
            buff=0.2
        )

        self.play(
            Write(prediction_label),
            FadeIn(prediction_number, scale=1.2),
            Write(correct_symbol)
        )

        self.next_slide()

        # =====================================
        # ROTATE THE DIGIT
        # =====================================

        rotate_text = Text(
            "What if we rotate the image?",
            font_size=30,
            color=YELLOW
        )

        rotate_text.to_edge(DOWN, buff=0.4)

        self.play(Write(rotate_text))

        self.next_slide()

        # Rotate the digit, not the box
        self.play(
            Rotate(
                digit,
                angle=35 * DEGREES,
                about_point=digit.get_center()
            ),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # WRONG PREDICTION
        # =====================================

        wrong_prediction = Text(
            "8",
            font_size=100,
            color=RED
        )

        wrong_prediction.move_to(
            prediction_number
        )

        wrong_symbol = Text(
            "Incorrect!",
            font_size=30,
            color=RED
        )

        wrong_symbol.move_to(
            correct_symbol
        )

        self.play(
            ReplacementTransform(
                prediction_number,
                wrong_prediction
            ),
            ReplacementTransform(
                correct_symbol,
                wrong_symbol
            ),
            run_time=1.5
        )

        self.next_slide()

        # =====================================
        # THE IMPORTANT QUESTION
        # =====================================

        self.play(
            FadeOut(accuracy_group),
            FadeOut(digit_title),
            FadeOut(digit),
            FadeOut(digit_box),
            FadeOut(prediction_label),
            FadeOut(wrong_prediction),
            FadeOut(wrong_symbol),
            FadeOut(rotate_text)
        )

        challenge_text = Text(
            "What did our accuracy score\nactually tell us?",
            font_size=46,
            color=YELLOW,
            line_spacing=1.2
        )

        challenge_text.move_to(ORIGIN)

        self.play(
            Write(challenge_text),
            run_time=2
        )

        self.next_slide()
        
                # =====================================
        # QUESTION 3 — MEDICAL AI EXAMPLE
        # =====================================

        # Clear the previous slide
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

        medical_title = Text(
            "A Medical AI With 99% Accuracy",
            font_size=40,
            color=YELLOW
        )
        medical_title.to_edge(UP, buff=0.35)

        self.play(Write(medical_title))

        # =====================================
        # INTRODUCE THE PATIENTS
        # =====================================

        patient_count = Text(
            "1,000 Patients",
            font_size=34,
            color=WHITE
        )
        patient_count.next_to(medical_title, DOWN, buff=0.25)

        self.play(Write(patient_count))

        # Create 1,000 dots: 40 columns x 25 rows
        patient_dots = VGroup()

        for i in range(1000):
            dot = Dot(
                radius=0.035,
                color=BLUE
            )
            patient_dots.add(dot)

        patient_dots.arrange_in_grid(
            rows=25,
            cols=40,
            buff=0.09
        )

        patient_dots.set_width(10.5)
        patient_dots.move_to(DOWN * 0.3)

        self.play(
            LaggedStart(
                *[
                    FadeIn(dot, scale=0.5)
                    for dot in patient_dots
                ],
                lag_ratio=0.001
            ),
            run_time=3
        )

        self.next_slide()

        # =====================================
        # HIGHLIGHT THE 10 PATIENTS
        # =====================================

        condition_dots = patient_dots[-10:]

        self.play(
            *[
                dot.animate.set_color(RED)
                for dot in condition_dots
            ],
            run_time=1.5
        )

        healthy_label = Text(
            "990 Without the Condition",
            font_size=27,
            color=BLUE
        )

        condition_label = Text(
            "10 With the Condition",
            font_size=27,
            color=RED
        )

        population_labels = VGroup(
            healthy_label,
            condition_label
        )

        population_labels.arrange(RIGHT, buff=0.7)
        population_labels.to_edge(DOWN, buff=0.25)

        self.play(
            Write(healthy_label),
            Write(condition_label)
        )

        self.next_slide()

        # =====================================
        # THE AI PREDICTS EVERYONE IS HEALTHY
        # =====================================

        self.play(FadeOut(population_labels))

        prediction_text = Text(
            "AI Prediction: Everyone Is Healthy",
            font_size=32,
            color=YELLOW
        )

        prediction_text.to_edge(DOWN, buff=0.25)

        self.play(Write(prediction_text))

        # Highlight the missed patients
        self.play(
            *[
                Indicate(dot, color=RED, scale_factor=1.8)
                for dot in condition_dots
            ],
            run_time=2
        )

        self.next_slide()

        # =====================================
        # CALCULATE ACCURACY
        # =====================================

        self.play(
            FadeOut(patient_dots),
            FadeOut(patient_count),
            FadeOut(prediction_text)
        )

        accuracy_heading = Text(
            "Accuracy",
            font_size=36,
            color=WHITE
        )

        accuracy_heading.move_to(UP * 1.2)

        accuracy_equation = MathTex(
            r"\frac{990}{1000}\times100",
            font_size=56
        )

        accuracy_equation.move_to(ORIGIN)

        self.play(Write(accuracy_heading))
        self.play(Write(accuracy_equation))

        self.next_slide()

        accuracy_result = MathTex(
            r"99\%",
            font_size=90,
            color=GREEN
        )

        accuracy_result.move_to(accuracy_equation)

        self.play(
            ReplacementTransform(
                accuracy_equation,
                accuracy_result
            )
        )

        self.next_slide()

        # =====================================
        # CALCULATE RECALL
        # =====================================

        self.play(
            accuracy_heading.animate.shift(LEFT * 3),
            accuracy_result.animate.shift(LEFT * 3)
        )

        recall_heading = Text(
            "Recall",
            font_size=36,
            color=WHITE
        )

        recall_heading.move_to(
            RIGHT * 3 + UP * 1.2
        )

        recall_equation = MathTex(
            r"\frac{0}{10}\times100",
            font_size=56
        )

        recall_equation.move_to(RIGHT * 3)

        self.play(Write(recall_heading))
        self.play(Write(recall_equation))

        self.next_slide()

        recall_result = MathTex(
            r"0\%",
            font_size=90,
            color=RED
        )

        recall_result.move_to(recall_equation)

        self.play(
            ReplacementTransform(
                recall_equation,
                recall_result
            )
        )

        self.next_slide()

        # =====================================
        # FINAL COMPARISON
        # =====================================

        comparison_text = Text(
            "Same Model. Two Very Different Stories.",
            font_size=34,
            color=YELLOW
        )

        comparison_text.to_edge(DOWN, buff=0.55)

        self.play(
            Write(comparison_text),
            run_time=2
        )

        self.next_slide()
        
                # =====================================
        # QUESTION 3 — HOW MUCH MATHS?
        # =====================================

        # Clear previous medical example
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

        # =====================================
        # BRING BACK THE CENTRAL QUESTION
        # =====================================

        maths_question = Text(
            "How Much Mathematics Do We\nActually Need to Understand AI?",
            font_size=43,
            color=YELLOW,
            line_spacing=1.2
        )

        maths_question.move_to(ORIGIN)

        self.play(
            Write(maths_question),
            run_time=2.5
        )

        self.next_slide()

        # Move question to top
        self.play(
            maths_question.animate.scale(0.65).to_edge(
                UP,
                buff=0.35
            ),
            run_time=1.2
        )

        # =====================================
        # APPLICATION 1 — MOVIE RECOMMENDATIONS
        # =====================================

        movie_box = RoundedRectangle(
            width=5.3,
            height=3.5,
            corner_radius=0.25,
            stroke_color=BLUE,
            stroke_width=3,
            fill_color=BLUE_E,
            fill_opacity=0.18
        )

        movie_box.move_to(LEFT * 3.15 + DOWN * 0.4)

        movie_icon = Text(
            "MOVIES",
            font_size=42,
            color=BLUE_B
        )

        movie_title = Text(
            "Recommendation AI",
            font_size=28,
            color=WHITE
        )

        movie_description = Text(
            "Suggests the wrong film",
            font_size=23,
            color=GREY_B
        )

        movie_content = VGroup(
            movie_icon,
            movie_title,
            movie_description
        )

        movie_content.arrange(DOWN, buff=0.35)
        movie_content.move_to(movie_box)

        self.play(
            Create(movie_box),
            FadeIn(movie_content, shift=UP * 0.3),
            run_time=1.5
        )

        self.next_slide()

        # =====================================
        # APPLICATION 2 — MEDICAL SCREENING
        # =====================================

        medical_box = RoundedRectangle(
            width=5.3,
            height=3.5,
            corner_radius=0.25,
            stroke_color=RED,
            stroke_width=3,
            fill_color=RED_E,
            fill_opacity=0.18
        )

        medical_box.move_to(RIGHT * 3.15 + DOWN * 0.4)

        medical_icon = Text(
            "HEALTHCARE",
            font_size=42,
            color=RED_B
        )

        medical_title_2 = Text(
            "Medical Screening AI",
            font_size=28,
            color=WHITE
        )

        medical_description = Text(
            "Misses a serious condition",
            font_size=23,
            color=GREY_B
        )

        medical_content = VGroup(
            medical_icon,
            medical_title_2,
            medical_description
        )

        medical_content.arrange(DOWN, buff=0.35)
        medical_content.move_to(medical_box)

        self.play(
            Create(medical_box),
            FadeIn(medical_content, shift=UP * 0.3),
            run_time=1.5
        )

        self.next_slide()

        # =====================================
        # COMPARE THE CONSEQUENCES
        # =====================================

        movie_consequence = Text(
            "Inconvenience",
            font_size=26,
            color=BLUE_B
        )

        medical_consequence = Text(
            "Potentially serious harm",
            font_size=26,
            color=RED_B
        )

        movie_consequence.next_to(
            movie_box,
            DOWN,
            buff=0.25
        )

        medical_consequence.next_to(
            medical_box,
            DOWN,
            buff=0.25
        )

        self.play(
            Write(movie_consequence),
            Write(medical_consequence)
        )

        self.next_slide()

        # =====================================
        # PROFESSOR ROBOT ENTERS
        # =====================================

        # Move cards upwards to make space
        left_application = VGroup(
            movie_box,
            movie_content,
            movie_consequence
        )

        right_application = VGroup(
            medical_box,
            medical_content,
            medical_consequence
        )

        self.play(
            left_application.animate.scale(0.78).shift(
                UP * 0.45
            ),
            right_application.animate.scale(0.78).shift(
                UP * 0.45
            ),
            run_time=1.2
        )

        professor_robot = ConfusedRobot(
            scale_factor=0.42
        )

        professor_robot.move_to(DOWN * 2.35)

        self.play(
            FadeIn(
                professor_robot,
                shift=UP * 0.4
            ),
            run_time=1.2
        )

        self.play(
            professor_robot.animate.look_left(),
            run_time=0.7
        )

        self.play(
            professor_robot.animate.look_right(),
            run_time=0.7
        )

        self.next_slide()

        # =====================================
        # THE CENTRAL TAKEAWAY
        # =====================================

        self.play(
            FadeOut(maths_question),
            FadeOut(left_application),
            FadeOut(right_application),
            FadeOut(professor_robot),
            run_time=1.2
        )

        takeaway_line_1 = Text(
            "The Higher the Stakes,",
            font_size=47,
            color=WHITE
        )

        takeaway_line_2 = Text(
            "The Deeper Our Understanding Must Be.",
            font_size=40,
            color=YELLOW
        )

        takeaway_group = VGroup(
            takeaway_line_1,
            takeaway_line_2
        )

        takeaway_group.arrange(DOWN, buff=0.5)
        takeaway_group.move_to(ORIGIN)

        self.play(
            Write(takeaway_line_1),
            run_time=1.5
        )

        self.next_slide()

        self.play(
            Write(takeaway_line_2),
            run_time=2
        )

        self.next_slide()
        
                # =====================================
        # GRAND FINALE — THREE QUESTIONS
        # =====================================

        # Clear previous slide
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

        finale_title = Text(
            "Three Questions. One Answer.",
            font_size=46,
            color=YELLOW
        )

        finale_title.to_edge(UP, buff=0.55)

        self.play(
            Write(finale_title),
            run_time=1.5
        )

        # =====================================
        # QUESTION CARDS
        # =====================================

        finale_questions = [
            (
                "01",
                "Architecture",
                "How does AI make predictions?",
                BLUE
            ),
            (
                "02",
                "Learning",
                "How does AI improve?",
                GREEN
            ),
            (
                "03",
                "Responsibility",
                "Why does understanding matter?",
                YELLOW
            )
        ]

        finale_cards = VGroup()

        for number, heading, description, colour in finale_questions:

            card = RoundedRectangle(
                width=3.9,
                height=3.0,
                corner_radius=0.2,
                stroke_color=colour,
                stroke_width=3,
                fill_color=colour,
                fill_opacity=0.1
            )

            number_text = Text(
                number,
                font_size=52,
                color=colour
            )

            heading_text = Text(
                heading,
                font_size=29,
                color=WHITE
            )

            description_text = Text(
                description,
                font_size=19,
                color=GREY_B
            )

            card_content = VGroup(
                number_text,
                heading_text,
                description_text
            )

            card_content.arrange(
                DOWN,
                buff=0.3
            )

            card_content.move_to(card)

            finale_cards.add(
                VGroup(card, card_content)
            )

        finale_cards.arrange(
            RIGHT,
            buff=0.35
        )

        finale_cards.move_to(DOWN * 0.3)

        for card in finale_cards:

            self.play(
                FadeIn(
                    card,
                    shift=UP * 0.3
                ),
                run_time=0.9
            )

            self.next_slide()

        # =====================================
        # TRANSITION TO FINAL ANSWER
        # =====================================

        self.play(
            FadeOut(finale_title),
            FadeOut(finale_cards),
            run_time=1.2
        )

        final_question = Text(
            "How Much Mathematics Do We\nActually Need to Understand AI?",
            font_size=43,
            color=YELLOW,
            line_spacing=1.2
        )

        final_question.move_to(ORIGIN)

        self.play(
            Write(final_question),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # THE ANSWER
        # =====================================

        self.play(
            final_question.animate.scale(0.65).to_edge(
                UP,
                buff=0.5
            ),
            run_time=1.2
        )

        answer_line_1 = Text(
            "Enough to understand",
            font_size=38,
            color=WHITE
        )

        answer_line_2 = Text(
            "what our models are doing,",
            font_size=42,
            color=BLUE_B
        )

        answer_line_3 = Text(
            "where they might fail,",
            font_size=42,
            color=RED_B
        )

        answer_line_4 = Text(
            "and when we should trust them.",
            font_size=42,
            color=GREEN_B
        )

        final_answer = VGroup(
            answer_line_1,
            answer_line_2,
            answer_line_3,
            answer_line_4
        )

        final_answer.arrange(
            DOWN,
            buff=0.3
        )

        final_answer.move_to(DOWN * 0.45)

        for line in final_answer:
            self.play(
                Write(line),
                run_time=1.1
            )

        self.next_slide()

        # =====================================
        # FINAL TAKEAWAY
        # =====================================

        self.play(
            FadeOut(final_question),
            FadeOut(final_answer),
            run_time=1
        )

        powerful_text = Text(
            "Building AI is powerful.",
            font_size=47,
            color=WHITE
        )

        responsible_text = Text(
            "Understanding AI is responsible.",
            font_size=43,
            color=YELLOW
        )

        final_message = VGroup(
            powerful_text,
            responsible_text
        )

        final_message.arrange(
            DOWN,
            buff=0.55
        )

        final_message.move_to(UP * 0.5)

        self.play(
            Write(powerful_text),
            run_time=2
        )

        self.next_slide()

        self.play(
            Write(responsible_text),
            run_time=2
        )

        self.next_slide()

        # =====================================
        # PROFESSOR ROBOT RETURNS
        # =====================================

        finale_robot = ConfusedRobot(
            scale_factor=0.55
        )

        finale_robot.move_to(DOWN * 2.2)

        finale_robot.happy_face()

        self.play(
            FadeIn(
                finale_robot,
                shift=UP * 0.4
            ),
            run_time=1.2
        )

        self.play(
            finale_robot.animate.shift(UP * 0.15),
            rate_func=there_and_back,
            run_time=0.8
        )

        self.next_slide()

        # =====================================
        # THANK YOU
        # =====================================

        self.play(
            FadeOut(final_message),
            FadeOut(finale_robot),
            run_time=1
        )

        thank_you = Text(
            "Thank You!",
            font_size=74,
            color=YELLOW
        )

        questions_text = Text(
            "Any Questions?",
            font_size=36,
            color=WHITE
        )

        thank_you_group = VGroup(
            thank_you,
            questions_text
        )

        thank_you_group.arrange(
            DOWN,
            buff=0.5
        )

        thank_you_group.move_to(UP * 0.8)

        final_robot = ConfusedRobot(
            scale_factor=0.65
        )

        final_robot.happy_face()
        final_robot.move_to(DOWN * 2.0)

        self.play(
            Write(thank_you),
            run_time=1.5
        )

        self.play(
            Write(questions_text),
            FadeIn(final_robot, shift=UP * 0.3),
            run_time=1.5
        )

        # Robot waves
        final_robot.raise_right_hand()

        self.play(
            final_robot.animate.rotate(
                5 * DEGREES
            ),
            rate_func=there_and_back,
            run_time=0.7
        )

        self.next_slide()