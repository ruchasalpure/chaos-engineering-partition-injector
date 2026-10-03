from crewai import Agent

chaos_engineering_partition_injector = Agent(
    role="Chaos Engineering Partition Injector",
    goal="Deliver high-precision autonomous Chaos Engineering Partition Injector operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
