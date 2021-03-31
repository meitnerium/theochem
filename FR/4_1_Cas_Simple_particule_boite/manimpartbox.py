from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

#  C:\users\francois\appdata\local\packages\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\localcache\local-packages\python38\Scripts\manimgl.exe -f example_scenes.py Partinabox -w


class Partinabox(Scene):
    def construct(self):
        axes = Axes((0, 10), (-1, 1))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01)) #, run_time=1

        # Axes.get_graph will return the graph of a function
        psi1 = axes.get_graph(
            lambda x: self.getpsi(1,x,10),
            color=BLUE,
        )
        prob1 = axes.get_graph(
            lambda x: self.getprob(1,x,10),
            color=RED,
        )
        psi2 = axes.get_graph(
            lambda x: self.getpsi(2,x,10),
            color=BLUE,
        )
        prob2 = axes.get_graph(
            lambda x: self.getprob(2,x,10),
            color=RED,
        )
        psi3 = axes.get_graph(
            lambda x: self.getpsi(3,x,10),
            color=BLUE,
        )
        prob3 = axes.get_graph(
            lambda x: self.getprob(3,x,10),
            color=RED,
        )        

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        psi1_label = axes.get_graph_label(psi1, "\\psi_1(x)")
        prob1_label = axes.get_graph_label(prob1, "|\\psi_1(x)|^2")
        psi2_label = axes.get_graph_label(psi2, "\\psi_2(x)")
        prob2_label = axes.get_graph_label(prob2, "|\\psi_2(x)|^2")
        psi3_label = axes.get_graph_label(psi2, "\\psi_3(x)")
        prob3_label = axes.get_graph_label(prob2, "|\\psi_3(x)|^2")        
        self.play(
            ShowCreation(psi1),
            FadeIn(psi1_label, RIGHT),
        )
        self.play(
            ShowCreation(prob1),
            FadeIn(prob1_label, LEFT),
        )
        self.wait(5)
        self.play(
            ReplacementTransform(psi1, psi2),
            FadeTransform(psi1_label, psi2_label),
            ReplacementTransform(prob1, prob2),
            FadeTransform(prob1_label, prob2_label),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(psi2, psi3),
            FadeTransform(psi2_label, psi3_label),
            ReplacementTransform(prob2, prob3),
            FadeTransform(prob2_label, prob3_label),
        )
        self.wait()
        
    def getpsi(self,n,x,L): 
        return np.sqrt(2/10) * math.sin(n * np.pi * x/10)
    def getprob(self,n,x,L): 
        return abs(np.sqrt(2/10) * math.sin(n * np.pi * x/10))**2

class diffenerg(Scene):
    def construct(self):
        Ener=Tex(r"{{\Psi_n(x) \Rightarrow E_n = \frac{\hbar^2 n^2 \pi^2}{2mL^2}").scale(0.8)
        Ener.to_edge(TOP)
        self.play(Write(Ener))
        diffener = Tex(r"{{E_2 - E_1 = \frac{\hbar^2 2^2 \pi^2}{2mL^2} - \frac{\hbar^2 1^2 \pi^2}{2mL^2}").scale(0.8)
        diffener.next_to(Ener, DOWN)
        self.play(Write(diffener))

class integpsi(Scene):
    def construct(self):
        int1=Tex(r"\int_{-\infty}^{\infty}\Psi(x)",r"^*",r"\Psi(x)dx=1").scale(0.8)
        int1.to_edge(TOP)
        self.play(Write(int1))
        self.play(FadeOut(int1[1]))
        self.wait(3)
        int2 = Tex(r"\int_{-\infty}^{\infty}\Psi(x)\Psi(x)dx=","\int_{-\infty}^{0}\Psi(x)\Psi(x)dx+",
                   "\int_{0}^{L}\Psi(x)\Psi(x)dx","+\int_{L}^{\infty}\Psi(x)\Psi(x)dx").scale(0.8)
        #diffener = Tex(r"{{E_2 - E_1 = \frac{\hbar^2 2^2 \pi^2}{2mL^2} - \frac{\hbar^2 1^2 \pi^2}{2mL^2}").scale(0.8)
        int2.next_to(int1, DOWN)
        self.play(Write(int2))
        self.wait(3)
        brace = Brace(int2[1], direction=DOWN)
        eq_text = brace.get_text(r"=0")
        brace2 = Brace(int2[3], direction=DOWN)
        eq2_text = brace2.get_text(r"=0")
        self.play(Write(brace))
        self.play(Write(eq_text))
        self.play(Write(brace2))
        self.play(Write(eq2_text))
        int3 = Tex(r"\int_{0}^{L}\Psi(x)\Psi(x)dx=", r"\int_{0}^{L}A^2\sin^2(\frac{n \pi x}{L})dx+").scale(0.8)
class Hamiltonien(Scene):
    def construct(self):
        hamil=Tex(r"{{\hat{H}(x)}} = \frac{-\hbar^2}{2m}\frac{\partial^2}{\partial x^2}",r"+ {\hat{V}(x)}").scale(0.8)
        self.play(Write(hamil))
        self.wait(3)
        effacer = Cross(hamil[2], stroke_color=RED, stroke_width=6)
        self.play(ShowCreation(effacer))
        #effacer.set_stroke(RED)
        #part1 = SGroup(hamil,effacer)
        #self.play(Write(part1))
        self.wait(2)
        self.play(FadeOut(hamil[2]))
        self.play(FadeOut(effacer))
        self.wait(3)
        self.play(hamil[0:2].animate.shift(UP))
        #hamil.animate.to_edge(UP)
        self.wait(3)
        shroindt=Tex(r"{{\hat{H}(x)\Psi(x)}} = E\Psi(x)").scale(0.8)
        self.play(Write(shroindt))
        self.play(hamil[0:2].animate.shift(UP))
        self.play(shroindt.animate.shift(UP))
        self.wait(3)
        shroindt2 = Tex(r"\frac{-\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\Psi(x)=E\Psi(x)").scale(0.8)
        self.play(
            TransformMatchingTex(
                shroindt.copy(), shroindt2,
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            )
        )
        self.wait(3)
        self.play(FadeOut(hamil))
        self.play(FadeOut(shroindt))
        self.play(shroindt2.animate.shift(UP))
        self.play(shroindt2.animate.shift(UP))
        cosfunc = Tex(r"\frac{\partial }{\partial x} \cos(x) = -\sin(x)").scale(0.8)
        dcosfunc = Tex(r"\frac{\partial^2 }{\partial x^2} \cos(x) = -\cos(x)").scale(0.8)
        self.play(Write(cosfunc))
        self.wait(3)
        self.play(Transform(cosfunc,dcosfunc))
        self.wait(3)
        self.play(FadeOut(cosfunc))
        self.play(dcosfunc.animate.shift(UP))
        dsinfunc = Tex(r"\frac{\partial^2 }{\partial x^2} \sin(x) = -\sin(x)").scale(0.8)

        self.play(Write(dsinfunc))
        self.wait(3)
        gensol = Tex(r"\Psi(x)=A \sin(k_A x) ",r"+ B \cos(k_B x)").scale(0.8)
        gensol.next_to(dsinfunc, DOWN)
        self.play(Write(gensol))
        self.wait(3)
        self.play(FadeOut(dcosfunc))
        self.play(FadeOut(dsinfunc))
        self.play(shroindt2.animate.to_corner(UL))
        self.play(gensol.animate.to_corner(UR))
        self.wait(6)
        self.play(FadeOut(gensol[1]))
        self.wait(6)

class Hamiltonien2(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Surrounding substrings with double braces
            # will ensure that those parts are separated
            # out in the Tex.  For example, here the
            # Tex will have 5 submobjects, corresponding
            # to the strings [A^2, +, B^2, =, C^2]
            Tex(r"{{\hat{H}(x)}} = \frac{-\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + {\hat{V}(x)}"),
            Tex(r"{{\hat{H}(x)}} = {\frac{-\hbar^2}{2m}\frac{\partial^2}{\partial x^2}}"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So both lines below are equivalent
            # to what you'd get by wrapping every instance of "B", "C"
            # "=", "(" and ")" with double braces
            Tex(r"{{\hat{H}(x)\Psi(x)}} = E\Psi(x)}"),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=to_isolate)
        )
        #lines.arrange(DOWN, buff=LARGE_BUFF)


        play_kw = {"run_time": 2}
        self.wait(3)
        self.play(Write(lines[0]))
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.wait(3)
        self.play(Transform(lines[0],lines[1]))
        #self.play(
        #    TransformMatchingTex(
        #        lines[0].copy(), lines[1],
        #        path_arc=90 * DEGREES,
        #    ),
        #    **play_kw
        #)
        self.wait(3)
        #lines.arrange(DOWN, buff=LARGE_BUFF)

        # Now, we could try this again on the next line...
        self.play(Write(lines[2]))
        #self.add(lines[2])
        #self.play(
        #    TransformMatchingTex(lines[1].copy(), lines[2]),
        #    **play_kw
        #)
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        new_line2 = Tex("{{A}}^2 = (C + B)(C - B)", isolate=to_isolate)
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()

class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
        night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

        surfaces = [
            TexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3
        )

        self.play(
            Transform(surface, surfaces[2]),
            # Move camera frame during the transition
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3
        )
        # Add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        # Play around with where the light is
        light_text = Text("You can move around the light source")
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)

        drag_text = Text("Try moving the mouse while pressing d or s")
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text, drag_text))
        self.wait()


class InteractiveDevlopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # This opens an iPython termnial where you can keep writing
        # lines as if they were part of this construct method.
        # In particular, 'square', 'circle' and 'self' will all be
        # part of the local namespace in that terminal.
        self.embed()

        # Try copying and pasting some of the lines below into
        # the interactive shell
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))

        # In the interactive shell, you can just type
        # play, add, remove, clear, wait, save_state and restore,
        # instead of self.play, self.add, self.remove, etc.

        # To interact with the window, type touch().  You can then
        # scroll in the window, or zoom by holding down 'z' while scrolling,
        # and change camera perspective by holding down 'd' while moving
        # the mouse.  Press 'r' to reset to the standard camera position.
        # Press 'q' to stop interacting with the window and go back to
        # typing new commands into the shell.

        # In principle you can customize a scene to be responsive to
        # mouse and keyboard interactions
        always(circle.move_to, self.mouse_point)


class ControlsExample(Scene):
    def setup(self):
        self.textbox = Textbox()
        self.checkbox = Checkbox()
        self.color_picker = ColorSliders()
        self.panel = ControlPanel(
            Text("Text", size=0.5), self.textbox, Line(),
            Text("Show/Hide Text", size=0.5), self.checkbox, Line(),
            Text("Color of Text", size=0.5), self.color_picker
        )
        self.add(self.panel)

    def construct(self):
        text = Text("", size=2)

        def text_updater(old_text):
            assert(isinstance(old_text, Text))
            new_text = Text(self.textbox.get_value(), size=old_text.size)
            # new_text.align_data_and_family(old_text)
            new_text.move_to(old_text)
            if self.checkbox.get_value():
                new_text.set_fill(
                    color=self.color_picker.get_picked_color(),
                    opacity=self.color_picker.get_picked_opacity()
                )
            else:
                new_text.set_opacity(0)
            old_text.become(new_text)

        text.add_updater(text_updater)

        self.add(MotionMobject(text))

        self.textbox.set_value("Manim")
        # self.wait(60)
        # self.embed()


# See https://github.com/3b1b/videos for many, many more
class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Surrounding substrings with double braces
            # will ensure that those parts are separated
            # out in the Tex.  For example, here the
            # Tex will have 5 submobjects, corresponding
            # to the strings [A^2, +, B^2, =, C^2]
            Tex("{{A^2}} + {{B^2}} = {{C^2}}"),
            Tex("{{A^2}} = {{C^2}} - {{B^2}}"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So both lines below are equivalent
            # to what you'd get by wrapping every instance of "B", "C"
            # "=", "(" and ")" with double braces
            Tex("{{A^2}} = (C + B)(C - B)", isolate=to_isolate),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=to_isolate)
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        # Now, we could try this again on the next line...
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        new_line2 = Tex("{{A}}^2 = (C + B)(C - B)", isolate=to_isolate)
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()