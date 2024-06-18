import os
from enum import Enum

ASANA_TOKEN = os.environ.get("ASANA_TOKEN")
ASANA_PROJECT_ID = "1207538772343223"

ASANA_SITE_LINK_FIELD_ID = "1207542759237693"
ASANA_REPORT_LINK_FIELD_ID = "1207542720788419"
ASANA_ISSUE_DESCRIPTION_FIELD_ID = "1207542642401235"

ASANA_REPORT_TYPE_FIELD_ID = "1207543086662142"

ASANA_OPT_FIELDS = [
    "actual_time_minutes",
    "approval_status",
    "assignee",
    "assignee.name",
    "assignee_section",
    "assignee_section.name",
    "assignee_status",
    "completed",
    "completed_at",
    "completed_by",
    "completed_by.name",
    "created_at",
    "created_by",
    "custom_fields",
    "custom_fields.asana_created_field",
    "custom_fields.created_by",
    "custom_fields.created_by.name",
    "custom_fields.currency_code",
    "custom_fields.custom_label",
    "custom_fields.custom_label_position",
    "custom_fields.date_value",
    "custom_fields.date_value.date",
    "custom_fields.date_value.date_time",
    "custom_fields.description",
    "custom_fields.display_value",
    "custom_fields.enabled",
    "custom_fields.enum_options",
    "custom_fields.enum_options.color",
    "custom_fields.enum_options.enabled",
    "custom_fields.enum_options.name",
    "custom_fields.enum_value",
    "custom_fields.enum_value.color",
    "custom_fields.enum_value.enabled",
    "custom_fields.enum_value.name",
    "custom_fields.format",
    "custom_fields.has_notifications_enabled",
    "custom_fields.id_prefix",
    "custom_fields.is_formula_field",
    "custom_fields.is_global_to_workspace",
    "custom_fields.is_value_read_only",
    "custom_fields.multi_enum_values",
    "custom_fields.multi_enum_values.color",
    "custom_fields.multi_enum_values.enabled",
    "custom_fields.multi_enum_values.name",
    "custom_fields.name",
    "custom_fields.number_value",
    "custom_fields.people_value",
    "custom_fields.people_value.name",
    "custom_fields.precision",
    "custom_fields.representation_type",
    "custom_fields.resource_subtype",
    "custom_fields.text_value",
    "custom_fields.type",
    "dependencies",
    "dependents",
    "due_at",
    "due_on",
    "external",
    "external.data",
    "followers",
    "followers.name",
    "hearted",
    "hearts",
    "hearts.user",
    "hearts.user.name",
    "html_notes",
    "is_rendered_as_separator",
    "liked",
    "likes",
    "likes.user",
    "likes.user.name",
    "memberships",
    "memberships.project",
    "memberships.project.name",
    "memberships.section",
    "memberships.section.name",
    "modified_at",
    "name",
    "notes",
    "num_hearts",
    "num_likes",
    "num_subtasks",
    "parent",
    "parent.created_by",
    "parent.name",
    "parent.resource_subtype",
    "permalink_url",
    "projects",
    "projects.name",
    "resource_subtype",
    "start_at",
    "start_on",
    "tags",
    "tags.name",
    "workspace",
    "workspace.name",
]


class AsanaReportType(Enum):
    WDIV_FEEDBACK = "1207543086662143"
    WCIVF_FEEDBACK = "1207543086662144"
    WDIV_BUG_REPORT = "1207543086662145"
    USER = "1207543086662146"
    COUNCIL = "1207543086662147"
