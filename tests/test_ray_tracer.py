import unittest
from optics_randomizer import ray_tracer

class TestRayTracer(unittest.TestCase):

    def test_init(self):
        lens_system = [{"center_x": 0, "center_y": 0, "thickness": 1}]
        rt = ray_tracer.RayTracer(lens_system)
        self.assertEqual(rt.lens_system, lens_system)

    def test_intersect(self):
        ray = {"x": 1, "y": 2}
        rt = ray_tracer.RayTracer([])
        self.assertAlmostEqual(rt.intersect(ray), 0.25)

    def test_trace(self):
        lens_system = [{"center_x": 0, "center_y": 0, "thickness": 1}]
        rt = ray_tracer.RayTracer(lens_system)
        rt.ray["x"] = 10
        rt.ray["y"] = 20
        result = rt.trace()
        self.assertEqual(result["x"], lens_system[0]["center_x"])
        self.assertEqual(result["y"], lens_system[0]["center_y"])

if __name__ == "__main__":
    unittest.main()
