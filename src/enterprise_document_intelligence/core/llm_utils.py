from langchain_core.messages import AIMessage


def extract_text(message: AIMessage) -> str:
    """
    Extract plain text from a LangChain AIMessage.

    Gemini may return:
        content = "text"

    or

        content = [
            {"type": "text", "text": "..."}
        ]
    """

    content = message.content

    # Normal case
    if isinstance(content, str):
        return content

    # Gemini 2.5 content blocks
    if isinstance(content, list):

        texts = []

        for item in content:

            if isinstance(item, dict):

                if item.get("type") == "text":
                    texts.append(item.get("text", ""))

        return "\n".join(texts)

    # Fallback
    return str(content)