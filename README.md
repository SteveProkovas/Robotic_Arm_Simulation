# Robotic Simulation

This project encompasses a Python-based framework designed to simulate the dynamics and kinematics of robotic arms. With this framework, you can explore the behavior of robotic arms in various scenarios, aiding in analysis and development. Dive in and simulate your robotic systems!

## Features

- Forward dynamics calculations using Lagrangian mechanics approach.
- Inverse kinematics solver for determining joint configurations.
- Singularity detection to identify critical arm configurations.
- Physics simulation engine for modeling object interactions in 3D space.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SteveProkovas/Robotic_Arm_Simulation.git
    cd robotic-simulation
    ```

2. Install dependencies (NumPy and SymPy):

    ```bash
    pip install numpy sympy
    ```

## Usage

### Dynamics Solver

```python
from dynamics import DynamicsSolver

# Example usage
solver = DynamicsSolver(arm_geometry)
# Perform forward dynamics calculations
joint_torques = solver.forward_dynamics(joint_angles, joint_velocities, joint_accelerations, external_forces)
```

### Kinematics Solver

```python
from kinematics import KinematicsSolver

# Example usage
solver = KinematicsSolver(arm_geometry)
# Perform inverse kinematics calculations
solution = solver.inverse_kinematics_solver(desired_position)
```

### Physics Engine

```python
from physics import PhysicsEngine, Sphere, Box

# Example usage
engine = PhysicsEngine(gravity=[0, -9.81, 0], grid_size=10)
dt = 0.01  # Time step (seconds)
for _ in range(num_steps):
    engine.simulate_step([sphere, box], dt)
```

## Contributing

Contributions are welcomed! Whether it's fixing bugs, adding features, or enhancing documentation, your contributions make this project better for everyone. Feel free to open issues or pull requests.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Version Control

Git is used for version control. Remember to follow Git best practices and commit your changes frequently.

## Testing

Unit tests are included in the `tests/` directory. Run the tests using:

```bash
pytest
```

## Debugging

Debugging can be achieved using print statements or debuggers like pdb. Additionally, logging can be enabled to track the behavior of the simulation.

## Documentation

Explore documentation in the `docs/` directory. It provides insights into classes, methods, parameters, and usage examples.
