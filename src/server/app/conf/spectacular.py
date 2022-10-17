"""DRF spectacular settings"""

SPECTACULAR_SETTINGS = {
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "TITLE": "API for test sample project for ROI BURO",
    "DESCRIPTION": "API scheme for ROI BURO test project",
    "CONTACT": {
        "name": "Alexey Vasilenko",
    },
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api/v1",
}
