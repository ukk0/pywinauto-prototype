import os
from time import sleep

import pytest

from page_object import LogCollector

# IDE/terminal must be run as administrator for the test to work
# Run via bash terminal: EXE_PATH='<path_to_exe>' pytest
# OR set correct path as default value below and just run pytest

EXE_PATH = os.getenv("EXE_PATH")


# Starts application and returns the page object model
@pytest.fixture
def collector_app():
    collector = LogCollector(exe_path=EXE_PATH, app_title_re=".*Log Collector.*")
    yield collector
    collector.close_application()


def test_basic_flow(collector_app):
    collector_app.select_collection_profile(profile="None")
    collector_app.toggle_checkbox_on(checkbox_label="PowerShell history")
    collector_app.start_collection()
    collector_app.close_confirmation_popup()
    assert "All files have been collected and archived." in collector_app.log_text()
