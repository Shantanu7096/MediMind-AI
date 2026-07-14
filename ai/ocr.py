"""
MediMind AI
OCR Engine v2.0
"""

import cv2
import easyocr
import numpy as np


class OCRScanner:

    # Load EasyOCR only once
    reader = easyocr.Reader(
        ['en'],
        gpu=False
    )

    @staticmethod
    def preprocess(image_path):
        """
        Improve image quality before OCR.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise Exception(
                "Unable to read image."
            )

        # Convert to grayscale
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        # Remove noise
        gray = cv2.medianBlur(
            gray,
            3
        )

        # Increase contrast
        gray = cv2.equalizeHist(
            gray
        )

        # Adaptive Threshold
        processed = cv2.adaptiveThreshold(

            gray,

            255,

            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,

            cv2.THRESH_BINARY,

            31,

            11

        )

        return processed

    @staticmethod
    def extract_text(image_path):
        """
        Extract text from image.
        """

        image = OCRScanner.preprocess(
            image_path
        )

        result = OCRScanner.reader.readtext(

            image,

            paragraph=True,

            detail=0

        )

        text = "\n".join(result)

        return text.strip()

    @staticmethod
    def confidence(image_path):
        """
        Returns OCR confidence.
        """

        image = OCRScanner.preprocess(
            image_path
        )

        result = OCRScanner.reader.readtext(
            image
        )

        if not result:
            return 0

        score = 0

        for item in result:

            score += item[2]

        return round(
            (score / len(result)) * 100,
            2
        )