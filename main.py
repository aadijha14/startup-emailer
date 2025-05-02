from workflows.lead_pipeline import lead_pipeline

if __name__ == "__main__":
    idea = "AI-powered inventory management for small businesses"

    result = lead_pipeline.run(idea)

    print("\n✅ Pipeline complete. Summary:\n")
    print(result)