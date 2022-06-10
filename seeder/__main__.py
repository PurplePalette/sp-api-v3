import asyncio
import platform
import sys

from seeder.scp import main as scp_main
from seeder.transfer import main as transfer_main
from seeder.user import main as user_main
from seeder.yaml_ import main as yaml_main

if __name__ == "__main__":
    if platform.system() == "Windows":
        policy = asyncio.WindowsSelectorEventLoopPolicy()  # type: ignore
        asyncio.set_event_loop_policy(policy)  # type: ignore
    if len(sys.argv) < 2:
        print("No action specified.")
        print("Available actions: scp, transfer, user, yaml")
        sys.exit(1)
    action_name = sys.argv[1]
    actions = {
        "transfer": transfer_main,
        "scp": scp_main,
        "user": user_main,
        "yaml": yaml_main
    }

    action = actions.get(action_name)
    if action is None:
        print(f"Unknown action {action}.")
        sys.exit(1)

    asyncio.run(action())
