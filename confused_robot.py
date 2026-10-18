from manim import *
import numpy as np

class ConfusedRobot(VGroup):
    def __init__(
        self,
        body_color=PURPLE_B,
        accent_color=None,
        eye_color=WHITE,
        pupil_color=BLACK,
        scale_factor=1.0,
        arm_stroke=18,
        leg_stroke=18,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.body_color = body_color
        self.accent_color = accent_color if accent_color else interpolate_color(body_color, WHITE, 0.35)
        self.eye_color = eye_color
        self.pupil_color = pupil_color
        self.arm_stroke = arm_stroke
        self.leg_stroke = leg_stroke

        self._build_robot()
        self.scale(scale_factor)
        self.save_neutral_pose()

    def _build_robot(self):
        self.body = RoundedRectangle(
            width=1.05, height=1.15, corner_radius=0.18,
            color=self.body_color, fill_color=self.body_color, fill_opacity=1
        )

        self.head = RoundedRectangle(
            width=1.25, height=0.82, corner_radius=0.18,
            color=self.body_color, fill_color=self.body_color, fill_opacity=1
        ).next_to(self.body, UP, buff=0.08)

        self.neck = RoundedRectangle(
            width=0.28, height=0.16, corner_radius=0.05,
            color=self.body_color, fill_color=self.body_color, fill_opacity=1
        ).move_to((self.head.get_bottom() + self.body.get_top()) / 2)

        self.antenna_stem = Line(
            self.head.get_top(),
            self.head.get_top() + UP * 0.35,
            color=self.accent_color,
            stroke_width=5
        )

        self.antenna_ball = Dot(
            self.antenna_stem.get_end(),
            radius=0.08,
            color=self.accent_color
        )

        self.left_eye = Circle(
            radius=0.13,
            color=self.eye_color,
            fill_color=self.eye_color,
            fill_opacity=1
        ).move_to(self.head.get_center() + LEFT * 0.27 + UP * 0.08)

        self.right_eye = Circle(
            radius=0.13,
            color=self.eye_color,
            fill_color=self.eye_color,
            fill_opacity=1
        ).move_to(self.head.get_center() + RIGHT * 0.27 + UP * 0.08)

        self.left_pupil = Dot(
            self.left_eye.get_center(),
            radius=0.05,
            color=self.pupil_color
        )

        self.right_pupil = Dot(
            self.right_eye.get_center(),
            radius=0.05,
            color=self.pupil_color
        )

        self.left_brow = Line(
            self.left_eye.get_center() + LEFT * 0.13 + UP * 0.22,
            self.left_eye.get_center() + RIGHT * 0.13 + UP * 0.22,
            color=WHITE,
            stroke_width=5
        )

        self.right_brow = Line(
            self.right_eye.get_center() + LEFT * 0.13 + UP * 0.22,
            self.right_eye.get_center() + RIGHT * 0.13 + UP * 0.22,
            color=WHITE,
            stroke_width=5
        )

        self.mouth = Line(
            self.head.get_center() + LEFT * 0.12 + DOWN * 0.18,
            self.head.get_center() + RIGHT * 0.12 + DOWN * 0.18,
            color=WHITE,
            stroke_width=5
        )

        left_shoulder = self.body.get_left() + UP * 0.35
        right_shoulder = self.body.get_right() + UP * 0.35

        self.left_arm = Line(
            left_shoulder,
            left_shoulder + LEFT * 0.45 + DOWN * 0.15,
            color=self.body_color,
            stroke_width=self.arm_stroke
        )

        self.right_arm = Line(
            right_shoulder,
            right_shoulder + RIGHT * 0.45 + DOWN * 0.15,
            color=self.body_color,
            stroke_width=self.arm_stroke
        )

        self.left_hand = Circle(
            radius=0.13,
            color=self.accent_color,
            fill_color=self.accent_color,
            fill_opacity=1
        ).move_to(self.left_arm.get_end())

        self.right_hand = Circle(
            radius=0.13,
            color=self.accent_color,
            fill_color=self.accent_color,
            fill_opacity=1
        ).move_to(self.right_arm.get_end())

        left_hip = self.body.get_bottom() + LEFT * 0.25
        right_hip = self.body.get_bottom() + RIGHT * 0.25

        self.left_leg = Line(
            left_hip,
            left_hip + DOWN * 0.42,
            color=self.body_color,
            stroke_width=self.leg_stroke
        )

        self.right_leg = Line(
            right_hip,
            right_hip + DOWN * 0.42,
            color=self.body_color,
            stroke_width=self.leg_stroke
        )

        self.left_foot = RoundedRectangle(
            width=0.42,
            height=0.16,
            corner_radius=0.06,
            color=self.accent_color,
            fill_color=self.accent_color,
            fill_opacity=1
        ).move_to(self.left_leg.get_end() + LEFT * 0.08 + DOWN * 0.03)

        self.right_foot = RoundedRectangle(
            width=0.42,
            height=0.16,
            corner_radius=0.06,
            color=self.accent_color,
            fill_color=self.accent_color,
            fill_opacity=1
        ).move_to(self.right_leg.get_end() + RIGHT * 0.08 + DOWN * 0.03)

        self.add(
            self.left_leg, self.right_leg,
            self.left_foot, self.right_foot,
            self.left_arm, self.right_arm,
            self.left_hand, self.right_hand,
            self.body, self.neck, self.head,
            self.antenna_stem, self.antenna_ball,
            self.left_eye, self.right_eye,
            self.left_pupil, self.right_pupil,
            self.left_brow, self.right_brow,
            self.mouth
        )

    def save_neutral_pose(self):
        self.neutral_left_brow = self.left_brow.copy()
        self.neutral_right_brow = self.right_brow.copy()
        self.neutral_mouth = self.mouth.copy()
        self.neutral_left_arm = self.left_arm.copy()
        self.neutral_right_arm = self.right_arm.copy()
        self.neutral_left_hand = self.left_hand.copy()
        self.neutral_right_hand = self.right_hand.copy()

    def look_at(self, target, shift_amount=0.055):
        if isinstance(target, Mobject):
            target_point = target.get_center()
        else:
            target_point = np.array(target)

        def pupil_target(eye):
            direction = target_point - eye.get_center()
            norm = np.linalg.norm(direction)
            if norm == 0:
                return eye.get_center()
            return eye.get_center() + (direction / norm) * shift_amount

        return AnimationGroup(
            self.left_pupil.animate.move_to(pupil_target(self.left_eye)),
            self.right_pupil.animate.move_to(pupil_target(self.right_eye)),
            lag_ratio=0
        )

    def look_left(self):
        return AnimationGroup(
            self.left_pupil.animate.move_to(self.left_eye.get_center() + LEFT * 0.055),
            self.right_pupil.animate.move_to(self.right_eye.get_center() + LEFT * 0.055),
            lag_ratio=0
        )

    def look_right(self):
        return AnimationGroup(
            self.left_pupil.animate.move_to(self.left_eye.get_center() + RIGHT * 0.055),
            self.right_pupil.animate.move_to(self.right_eye.get_center() + RIGHT * 0.055),
            lag_ratio=0
        )

    def look_up(self):
        return AnimationGroup(
            self.left_pupil.animate.move_to(self.left_eye.get_center() + UP * 0.055),
            self.right_pupil.animate.move_to(self.right_eye.get_center() + UP * 0.055),
            lag_ratio=0
        )

    def raise_eyebrows(self, amount=0.12):
        return AnimationGroup(
            self.left_brow.animate.shift(UP * amount),
            self.right_brow.animate.shift(UP * amount),
            lag_ratio=0
        )

    def furrow_eyebrows(self):
        left_target = self.left_brow.copy().rotate(-18 * DEGREES)
        right_target = self.right_brow.copy().rotate(18 * DEGREES)

        return AnimationGroup(
            Transform(self.left_brow, left_target),
            Transform(self.right_brow, right_target),
            lag_ratio=0
        )

    def confused_face(self):
        left_target = self.left_brow.copy().rotate(18 * DEGREES).shift(UP * 0.03)
        right_target = self.right_brow.copy().rotate(-18 * DEGREES).shift(DOWN * 0.02)

        mouth_target = Line(
            self.head.get_center() + LEFT * 0.16 + DOWN * 0.2,
            self.head.get_center() + RIGHT * 0.16 + DOWN * 0.17,
            color=WHITE,
            stroke_width=5
        )

        return AnimationGroup(
            Transform(self.left_brow, left_target),
            Transform(self.right_brow, right_target),
            Transform(self.mouth, mouth_target),
            lag_ratio=0
        )

    def thinking_face(self):
        mouth_target = Line(
            self.head.get_center() + LEFT * 0.12 + DOWN * 0.20,
            self.head.get_center() + RIGHT * 0.12 + DOWN * 0.20,
            color=WHITE,
            stroke_width=5
        )

        return AnimationGroup(
            self.look_up(),
            self.left_brow.animate.shift(UP * 0.04),
            self.right_brow.animate.shift(UP * 0.04),
            Transform(self.mouth, mouth_target),
            lag_ratio=0
        )

    def happy_face(self):
        mouth_target = Arc(
            radius=0.20,
            start_angle=200 * DEGREES,
            angle=140 * DEGREES,
            color=WHITE,
            stroke_width=5
        ).move_to(self.head.get_center() + DOWN * 0.13)

        return AnimationGroup(
            self.left_brow.animate.shift(UP * 0.04),
            self.right_brow.animate.shift(UP * 0.04),
            Transform(self.mouth, mouth_target),
            lag_ratio=0
        )

    def reset_face(self):
        return AnimationGroup(
            self.left_pupil.animate.move_to(self.left_eye.get_center()),
            self.right_pupil.animate.move_to(self.right_eye.get_center()),
            Transform(self.left_brow, self.neutral_left_brow.copy()),
            Transform(self.right_brow, self.neutral_right_brow.copy()),
            Transform(self.mouth, self.neutral_mouth.copy()),
            lag_ratio=0
        )

    def raise_right_hand(self):
        shoulder = self.body.get_right() + UP * 0.35

        new_arm = Line(
            shoulder,
            shoulder + RIGHT * 0.25 + UP * 0.55,
            color=self.body_color,
            stroke_width=self.arm_stroke
        )

        new_hand = self.right_hand.copy().move_to(new_arm.get_end())

        return AnimationGroup(
            Transform(self.right_arm, new_arm),
            Transform(self.right_hand, new_hand),
            lag_ratio=0
        )

    def raise_left_hand(self):
        shoulder = self.body.get_left() + UP * 0.35

        new_arm = Line(
            shoulder,
            shoulder + LEFT * 0.25 + UP * 0.55,
            color=self.body_color,
            stroke_width=self.arm_stroke
        )

        new_hand = self.left_hand.copy().move_to(new_arm.get_end())

        return AnimationGroup(
            Transform(self.left_arm, new_arm),
            Transform(self.left_hand, new_hand),
            lag_ratio=0
        )

    def point_at(self, target, hand="right"):
        if isinstance(target, Mobject):
            target_point = target.get_center()
        else:
            target_point = np.array(target)

        if hand == "right":
            shoulder = self.body.get_right() + UP * 0.35
            arm = self.right_arm
            hand_obj = self.right_hand
        else:
            shoulder = self.body.get_left() + UP * 0.35
            arm = self.left_arm
            hand_obj = self.left_hand

        direction = target_point - shoulder
        direction = direction / np.linalg.norm(direction)

        end = shoulder + direction * 0.78

        new_arm = Line(
            shoulder,
            end,
            color=self.body_color,
            stroke_width=self.arm_stroke
        )

        new_hand = hand_obj.copy().move_to(end)

        return AnimationGroup(
            Transform(arm, new_arm),
            Transform(hand_obj, new_hand),
            self.look_at(target_point),
            lag_ratio=0
        )

    def reset_arms(self):
        return AnimationGroup(
            Transform(self.left_arm, self.neutral_left_arm.copy()),
            Transform(self.right_arm, self.neutral_right_arm.copy()),
            Transform(self.left_hand, self.neutral_left_hand.copy()),
            Transform(self.right_hand, self.neutral_right_hand.copy()),
            lag_ratio=0
        )

    def small_bounce(self):
        return Succession(
            self.animate.shift(UP * 0.12),
            self.animate.shift(DOWN * 0.12)
        )
    
    def make_speech_bubble(
        self,
        content,
        direction=RIGHT,
        width=2.8,
        height=1.25,
        bubble_color=WHITE,
        text_color=BLACK,
        font_size=30,
        buff=0.25
    ):
        if isinstance(content, str):
            text = Text(content, font_size=font_size, color=text_color)
        else:
            text = content

        bubble = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.18,
            color=bubble_color,
            fill_color=bubble_color,
            fill_opacity=1,
            stroke_width=3
        )

        text.move_to(bubble.get_center())

        # Tail
        if np.allclose(direction, RIGHT):
            bubble.next_to(self.head, RIGHT, buff=buff)
            tail = Polygon(
                bubble.get_left() + DOWN * 0.18,
                bubble.get_left() + DOWN * 0.42,
                self.head.get_right() + RIGHT * 0.05,
                color=bubble_color,
                fill_color=bubble_color,
                fill_opacity=1
            )
        elif np.allclose(direction, LEFT):
            bubble.next_to(self.head, LEFT, buff=buff)
            tail = Polygon(
                bubble.get_right() + DOWN * 0.18,
                bubble.get_right() + DOWN * 0.42,
                self.head.get_left() + LEFT * 0.05,
                color=bubble_color,
                fill_color=bubble_color,
                fill_opacity=1
            )
        elif np.allclose(direction, UP):
            bubble.next_to(self.head, UP, buff=buff)
            tail = Polygon(
                bubble.get_bottom() + LEFT * 0.18,
                bubble.get_bottom() + RIGHT * 0.18,
                self.head.get_top() + UP * 0.05,
                color=bubble_color,
                fill_color=bubble_color,
                fill_opacity=1
            )
        else:
            bubble.next_to(self.head, DOWN, buff=buff)
            tail = Polygon(
                bubble.get_top() + LEFT * 0.18,
                bubble.get_top() + RIGHT * 0.18,
                self.head.get_bottom() + DOWN * 0.05,
                color=bubble_color,
                fill_color=bubble_color,
                fill_opacity=1
            )

        text.move_to(bubble.get_center())

        return VGroup(tail, bubble, text)
    
    def make_thought_bubble(
        self,
        content,
        direction=RIGHT,
        width=2.8,
        height=1.25,
        bubble_color=WHITE,
        text_color=BLACK,
        font_size=30,
        buff=0.35
    ):
        if isinstance(content, str):
            text = Text(content, font_size=font_size, color=text_color)
        else:
            text = content

        bubble = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.28,
            color=bubble_color,
            fill_color=bubble_color,
            fill_opacity=1,
            stroke_width=3
        )

        if np.allclose(direction, RIGHT):
            bubble.next_to(self.head, RIGHT, buff=buff)
            dot1 = Dot(self.head.get_right() + RIGHT * 0.16 + UP * 0.02, radius=0.045, color=bubble_color)
            dot2 = Dot(self.head.get_right() + RIGHT * 0.32 + UP * 0.15, radius=0.065, color=bubble_color)
        elif np.allclose(direction, LEFT):
            bubble.next_to(self.head, LEFT, buff=buff)
            dot1 = Dot(self.head.get_left() + LEFT * 0.16 + UP * 0.02, radius=0.045, color=bubble_color)
            dot2 = Dot(self.head.get_left() + LEFT * 0.32 + UP * 0.15, radius=0.065, color=bubble_color)
        elif np.allclose(direction, UP):
            bubble.next_to(self.head, UP, buff=buff)
            dot1 = Dot(self.head.get_top() + UP * 0.14, radius=0.045, color=bubble_color)
            dot2 = Dot(self.head.get_top() + UP * 0.30 + RIGHT * 0.08, radius=0.065, color=bubble_color)
        else:
            bubble.next_to(self.head, DOWN, buff=buff)
            dot1 = Dot(self.head.get_bottom() + DOWN * 0.14, radius=0.045, color=bubble_color)
            dot2 = Dot(self.head.get_bottom() + DOWN * 0.30 + RIGHT * 0.08, radius=0.065, color=bubble_color)

        text.move_to(bubble.get_center())

        return VGroup(dot1, dot2, bubble, text)