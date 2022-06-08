import asyncio

from seeder.scp import main

if __name__ == "__main__":
    import platform

    if platform.system() == "Windows":
        policy = asyncio.WindowsSelectorEventLoopPolicy()  # type: ignore
        asyncio.set_event_loop_policy(policy)  # type: ignore
    asyncio.run(main())
