from semantic_digital_twin.adapters.mjcf import MJCFParser
from multiverse_simulator import MultiverseViewer
from semantic_digital_twin.adapters.multi_sim import MujocoSim
import os
import time

if __name__ == "__main__":
    scene_path = os.path.join(os.path.dirname(__file__), "..", "assets", "apartment_full.xml")
    image_dir = os.path.join(os.path.dirname(__file__), "..", "images")
    world = MJCFParser(scene_path).parse()
    viewer = MultiverseViewer()
    headless = os.environ.get("CI", "false").lower() == "true" # headless in CI environments
    multi_sim = MujocoSim(world=world, viewer=viewer, headless=headless, step_size=1E-3, integrator="IMPLICITFAST")
    multi_sim.start_simulation()

    print("Wait 1s...")
    time.sleep(1)
    print("Everything is ready")

    try:
        for i in range(120):
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop simulation!")
    finally:
        multi_sim.stop_simulation()
