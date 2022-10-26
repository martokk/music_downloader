from typing import Any, NoReturn

import sys
from collections.abc import Callable
from pathlib import Path

from loguru import logger
from PyQt5.QtWidgets import QApplication
from workflow_manager.action_script import ActionScript
from workflow_manager.config import Config
from workflow_manager.workflow_manager import WorkflowManager

from music_downloader import version
from music_downloader.pyqt5_ui import Ui_MainWindow

logger.add("log.log", level="TRACE", rotation="50 MB")

CONFIG = Config(
    app_name=f"Music Downloader v{version}",
    statusbar_text="App designed by v3services",
    about_text="App designed by v3services.",
    pos_x=0,
    pos_y=0,
    height=1200,
    width=800,
)


class MusicDownloaderActionScript(ActionScript):
    def script(self, **kwargs: object) -> str:
        logger.info(f"Starting: {self.__class__.__name__}.script()")

        return f"Hello World. {kwargs=}"


class MusicDownloaderWorkflowManager(WorkflowManager):
    def __init__(self) -> None:
        self.ui = Ui_MainWindow()  # Imports QtDesigner UI
        self.config: Config = CONFIG
        super().__init__()

    # Callbacks
    def save_to_button_clicked(self) -> None:
        self.ui.save_to_line_edit.setText(self._get_directory())

    def download_button_clicked(self) -> None:
        # Define Script & Input
        script_cls: Callable[..., Any] = MusicDownloaderActionScript
        url = self.ui.url_line_edit.text()
        save_to_directory = Path(self.ui.save_to_line_edit.text())

        # Validate & Run Script
        if self.inputs_are_valid(url=url, save_to_directory=save_to_directory):
            self.run_action_script(
                script_cls=script_cls, url=url, save_to_directory=save_to_directory
            )

    # Connections
    def connect_buttons(self):
        """Connects UI buttons the the callback function."""
        super().connect_buttons()
        self.ui.save_to_button.clicked.connect(self.save_to_button_clicked)
        self.ui.download_button.clicked.connect(self.download_button_clicked)

    # Input Validations
    def validate_inputs(self, **kwargs: object) -> str | None:
        """
        Validation on required inputs. ie. Ensure file exists, ensure value is int, etc.

        Return None if passes all validations.
        Return str with error if does NOT pass validation.
        """
        if not kwargs.get("url"):
            return "url can not be empty."
        if not kwargs.get("save_to_directory"):
            return "save_to_directory can not be empty."
        return None


def main() -> NoReturn:
    app = QApplication(sys.argv)
    _ = MusicDownloaderWorkflowManager()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
