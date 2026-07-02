from enterprise_document_intelligence.core.llm import get_llm


def main():

    llm = get_llm()

    response = llm.invoke(
        "Say hello in one sentence."
    )

    print(response.content)


if __name__ == "__main__":
    main()