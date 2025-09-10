import os
import unittest
from prompt_injection_core.detectors.roleplay import RolePlayDetector

class TestRolePlayDetector(unittest.TestCase):
    def setUp(self):
        self.prompts_path = os.path.join("data", "prompts_roleplay_test_extra.txt")
        with open(self.prompts_path, "r", encoding="utf-8") as f:
            self.prompts = [line.strip() for line in f if line.strip()]
        self.detector = RolePlayDetector()

    def test_prompts_detection(self):
        """Test detection for all prompts in the test file."""
        for prompt in self.prompts:
            detections = self.detector.detect(prompt)
            # Se espera que algunos prompts sean detectados, otros no
            self.assertIsInstance(detections, list)
            # Opcional: verificar que cada detección tenga los atributos esperados
            for d in detections:
                self.assertTrue(hasattr(d, 'vulnerability_type'))
                self.assertTrue(hasattr(d, 'confidence'))
                self.assertTrue(hasattr(d, 'severity'))

if __name__ == "__main__":
    unittest.main()
