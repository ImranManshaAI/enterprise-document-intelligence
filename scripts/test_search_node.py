from enterprise_document_intelligence.agents.nodes import search_node


state = {
    "question": "What are customer due diligence requirements?",
    "documents": [],
    "answer": "",
    "sources": [],
}

result = search_node(state)

print("=" * 80)
print("Retrieved Documents:", len(result["documents"]))
print("=" * 80)

for source in result["sources"]:
    print(source)