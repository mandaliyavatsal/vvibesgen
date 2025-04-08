import os
import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
from app import AImusicGeneratorApp

class TestAImusicGeneratorApp(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = AImusicGeneratorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('app.pipeline')
    def test_generate_music(self, mock_pipeline):
        mock_model = MagicMock()
        mock_pipeline.return_value = mock_model
        mock_model.return_value = b"fake music data"

        self.app.model_directory = "fake_directory"
        self.app.generate_music()

        mock_pipeline.assert_called_once_with('text-to-music', model="fake_directory")
        self.assertEqual(self.app.generated_music, b"fake music data")

    @patch('tkinter.filedialog.askdirectory')
    def test_choose_model_directory(self, mock_askdirectory):
        mock_askdirectory.return_value = "fake_directory"
        self.app.choose_model_directory()
        self.assertEqual(self.app.model_directory, "fake_directory")

    @patch('tkinter.filedialog.asksaveasfilename')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_music(self, mock_open, mock_asksaveasfilename):
        self.app.generated_music = b"fake music data"
        mock_asksaveasfilename.return_value = "fake_path.mp3"

        self.app.save_music()

        mock_open.assert_called_once_with("fake_path.mp3", 'wb')
        mock_open().write.assert_called_once_with(b"fake music data")

    def test_adjust_parameters(self):
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.app.adjust_parameters()
            mock_showinfo.assert_called_once_with("Adjust Parameters", "Adjusting music parameters is not implemented yet.")

    def test_share_music(self):
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.app.share_music()
            mock_showinfo.assert_called_once_with("Share Music", "Sharing music is not implemented yet.")

if __name__ == "__main__":
    unittest.main()
