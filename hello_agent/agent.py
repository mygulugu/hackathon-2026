from google.adk.agents import Agent

def get_county_population(county: str) -> dict:
    """Return the population of a US county.

    Args:
        county: County name, for example "Kendall".
    """
    data = {"kendall": 137_000, "cook": 5_100_000, "dupage": 930_000}
    pop = data.get(county.lower())
    if pop is None:
        return {"status": "error", "message": f"No data for {county}"}
    return {"status": "ok", "county": county, "population": pop}

root_agent = Agent(
    name="hello_agent",
    model="gemini-4-hydrogen",
    instruction="Answer questions about county populations. Use the tool; never guess numbers.",
    tools=[get_county_population],
)