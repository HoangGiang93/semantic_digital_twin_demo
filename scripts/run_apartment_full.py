from semantic_digital_twin.adapters.mjcf import MJCFParser
from multiverse_simulator import MultiverseViewer
from semantic_digital_twin.adapters.multi_sim import MujocoSim
import os
import time

if __name__ == "__main__":
    scene_path = os.path.join(
        os.path.dirname(__file__), "..", "assets", "apartment_full.xml"
    )
    image_dir = os.path.join(os.path.dirname(__file__), "..", "images")
    world = MJCFParser(scene_path).parse()
    viewer = MultiverseViewer()
    viewer.write_objects = {
        "LeftHand_WristRoot": {
            "position": [1.5, 2.6, 1],
            "quaternion": [0, 1, 0, 0],
        },
        "LeftHand_ThumbTip": {
            "position": [1.5785, 2.59142, 1.0835],
            "quaternion": [-0.653282, 0.653282, 0.270598, 0.270598],
        },
        "LeftHand_IndexTip": {
            "position": [1.665, 2.6, 1.033],
            "quaternion": [0, 1, 0, 0],
        },
        "LeftHand_MiddleTip": {
            "position": [1.669, 2.6, 1.011],
            "quaternion": [0, 1, 0, 0],
        },
        "LeftHand_RingTip": {
            "position": [1.665, 2.6, 0.989],
            "quaternion": [0, 1, 0, 0],
        },
        "LeftHand_PinkyTip": {
            "position": [1.6565, 2.6, 0.967],
            "quaternion": [0, 1, 0, 0],
        },
        "RightHand_WristRoot": {
            "position": [1.5, 2.4, 1],
            "quaternion": [0, 0, 0, 1],
        },
        "RightHand_ThumbTip": {
            "position": [1.5785, 2.40858, 1.0835],
            "quaternion": [0.270598, -0.270598, 0.653282, 0.653282],
        },
        "RightHand_IndexTip": {
            "position": [1.665, 2.4, 1.033],
            "quaternion": [0, 0, 0, 1],
        },
        "RightHand_MiddleTip": {
            "position": [1.669, 2.4, 1.011],
            "quaternion": [0, 0, 0, 1],
        },
        "RightHand_RingTip": {
            "position": [1.665, 2.4, 0.989],
            "quaternion": [0, 0, 0, 1],
        },
        "RightHand_PinkyTip": {
            "position": [1.6565, 2.4, 0.967],
            "quaternion": [1.0, 0.0, 0.0, 0.0],
        },
    }
    headless = (
        os.environ.get("CI", "false").lower() == "true"
    )  # headless in CI environments
    multi_sim = MujocoSim(
        world=world,
        viewer=viewer,
        headless=headless,
        step_size=1e-3,
        integrator="IMPLICITFAST",
    )
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
