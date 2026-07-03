COMPARE_EXTRACTOR_PROMPT = """
You are an enterprise document assistant.

The user wants to compare two topics.

Extract exactly TWO comparison topics.

Examples

Question:
Compare AML regulations with SME regulations.

Left:
AML regulations

Right:
SME regulations

--------------------------

Question:
Compare customer due diligence and fair treatment of consumers.

Left:
Customer Due Diligence

Right:
Fair Treatment of Consumers

--------------------------

Question:

{question}
"""