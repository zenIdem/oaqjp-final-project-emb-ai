from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        test={
            "I am glad this happened":"joy",
            "I am really mad about this" : "anger",
            "I feel disgusted just hearing about this":"disgust",
            "I am so sad about this":"sadness",
            "I am really afraid that this will happen":"fear"}
        for chiave, valore in test.items():
            risu=emotion_detector(chiave)
            self.assertEqual(risu["dominant_emotion"],valore)
if __name__ == '__main__':
    unittest.main()