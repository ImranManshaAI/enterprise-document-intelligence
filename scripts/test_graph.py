from enterprise_document_intelligence.agents.graph import build_graph


QUERIES = [
    "What is customer due diligence?",
    "Compare AML regulations with SME regulations.",
    "Summarize the Fair Treatment of Consumers framework.",
    "Which regulations contradict each other?",
]


def run_query(graph, question):

    result = graph.invoke(
        {
            "question": question,
            "route": "search",
            "documents": [],
            "context": "",
            "answer": "",
            "sources": [],
        }
    )

    print("=" * 100)
    print(question)
    print("=" * 100)

    print(f"Route : {result['route']}")
    print()

    print("Answer:")
    print(result["answer"])

    if result["sources"]:
        print("\nSources:")
        for source in result["sources"]:
            print(f"- {source}")

    print("\n")


def main():

    graph = build_graph()

    for query in QUERIES:
        run_query(graph, query)


if __name__ == "__main__":
    main()