from transformers import pipeline


class SentimentService:

    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert",
        )

    def analyze(
        self,
        title: str,
        description: str | None = None,
    ) -> tuple[str, float]:

        text = title

        if description:
            text += f"\n\n{description}"

        result = self.classifier(
            text,
            truncation=True,
            max_length=512,
        )[0]

        return result["label"].lower()
