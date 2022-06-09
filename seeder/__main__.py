import asyncio
import sys

from seeder.user import main as user_main
from seeder.transfer import main as transfer_main
from seeder.scp import main as scp_main
from seeder.yaml_ import main as yaml_main

if __name__ == "__main__":
    import platform

    if platform.system() == "Windows":
        policy = asyncio.WindowsSelectorEventLoopPolicy()  # type: ignore
        asyncio.set_event_loop_policy(policy)  # type: ignore
    if len(sys.argv) < 2:
        print("No action specified.")
        sys.exit(1)
    action = sys.argv[1]
    if action == "user":
        main = user_main
    elif action == "transfer":
        main = transfer_main
    elif action == "scp":
        main = scp_main
    elif action == "yaml":
        main = yaml_main
    else:
        print(f"Unknown action {action}.")
        sys.exit(1)

    asyncio.run(main())
