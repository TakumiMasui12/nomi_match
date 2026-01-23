from django.db import models

# 幹事テーブル
class Organizer(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    login_id = models.CharField(
        max_length=64,
        unique=True,
        null=False
    )
    password_hash = models.CharField(
        max_length=128,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

# イベントテーブル
class Events(models.Model):
    mode_choices = (
        ("offline", "オフライン"),
        ("online", "オンライン"),
        ("undecided", "未定"),
    )
    decision_mode_choices = (
        ("organizer", "幹事"),
        ("majority", "参加者"),
    )
    status_choices = (
        ("draft", "下書き"),
        ("active", "開催中"),
        ("decided", "決定済み"),
        ("closed", "終了"),
    )

    id = models.BigAutoField(
        primary_key=True,
    )
    organizer_id = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=128,
        null=False
    )
    mode = models.CharField(
        max_length=16,
        null=False,
        choices=mode_choices
    )
    budget_hint = models.CharField(
        max_length=64,
        null=False
    )
    area = models.CharField(
        max_kength=128
    )
    genre_tags = models.JSONField(
        null=False
    )
    constraints = models.JSONField(
        null=False
    )
    decision_mode = models.CharField(
        max_length=16,
        null=False,
        choices=decision_mode_choices
    )
    poll_genre_enabled = models.BooleanField(
        default=True,
        null=False
    )
    poll_store_enabled = models.BooleanField(
        default=True,
        null=False
    )
    invite_token = models.CharField(
        max_length=64,
        unique=True,
        null=False
    )
    status = models.CharField(
        max_length=16,
        null=False,
        default="draft"
        choices=status_choices
    )
    created_at = models.DateTimeField(
        null=False
    )
    updated_at = models.DateTimeField(
        null=False
    )

# 公開範囲テーブル
class EventVisibilitySettings(models.Model):
    event_id = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    show_participant_names = models.BooleanField(
        default=True,
        null=False,
    )
    show_event_info = models.BooleanField(
        null=False,
        default=True,
    )
    show_availability_summary_to_participants = models.BooleanField(
        null=False,
        default=True,
    )
    created_at = models.DateTimeField(
        null=False
    )
    updated_at = models.DateTimeField(
        null=False
    )

# 参加者テーブル
class ParticipantIdentities(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    participant_token = models.CharField(
        max_length=64,
        unique=True,
        null=False
    )
    created_at = models.DateTimeField(
        null=False
    )
    updated_at = models.DateTimeField()

# イベント参加者テーブル
class EventParticipants(models.Model):
    can_drink_choices = (
        ("yes", "飲酒"),
        ("no", "ノンアルコール"),
        ("any", "どちらでもよい"),
    )
    smoking_choices = (
        ("yes", "喫煙"),
        ("no", "禁煙"),
        ("any", "どちらでもよい"),
    )

    event_id = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        null=False
    )
    participant_identity_id = models.ForeignKey(
        ParticipantIdentities,
        on_delete=models.CASCADE,
        null=False
    )
    display_name = models.CharField(
        max_length=32,
        null=False
    )
    budget_cap = models.IntegerField()
    allergies = models.CharField()
    can_drink = models.CharField(
        choices=can_drink_choices,
        max_length=8,
    )
    smoking = models.CharField(
        choices=smoking_choices,
        max_length=8,
    )
    joined_at = models.DateTimeField(
        null=False
    )

# 日程候補テーブル
class ScheduleSlots(models.Model):
    created_by_choices = (
        ("organizer", "幹事"),
        ("participant", "参加者"),
    )

    id = models.BigAutoField(
        primary_key=True,
        null=False,
    )
    event_id = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        null=False
    )
    start_at = models.DateTimeField(
        null=False
    )
    end_at = models.DateTimeField(
        null=False
    )
    created_by = models.CharField(
        max_length=12,
        null=False
        choices=created_by_choices,
    )
    created_by_participant_identity_id = models.ForeignKey(
        ParticipantIdentities,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        null=False
    )

# 日程回答テーブル
class Availabilities(models.Model):
    status_choices = (
        ("ok", "参加可能"),
        ("ng", "参加不可"),
        ("other", "その他"),
    )

    event_id = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        null=False
    )
    slot_id = models.ForeignKey(
        ScheduleSlots,
        on_delete=models.CASCADE,
        null=False
    )
    participant_identity_id = models.ForeignKey(
        ParticipantIdentities,
        on_delete=models.CASCADE,
        null=False
    )
    status = models.CharField(
        max_length=8,
        null=False,
        choices=status_choices
    )
    note = models.CharField(
        max_length=256
    )
    updated_at = models.DateTimeField(
        null=False
    )