from enterprise_document_intelligence.services.router import RouterService


QUERIES = [
    "What is customer due diligence?",
    "Compare AML regulations with SME regulations.",
    "Summarize the Fair Treatment of Consumers framework.",
    "Which regulations contradict each other?",
]


def main():

    router = RouterService()

    for query in QUERIES:

        print("=" * 80)
        print(query)
        print("-" * 80)

        route = router.route(query)

        print(route)
        print()


if __name__ == "__main__":
    main()