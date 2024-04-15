# Robotic Simulation

This is a Python-based physics simulation framework designed to simulate the behavior of objects in a 3D environment, considering forces like gravity, friction, and collisions. Enjoy simulating physics with the framework! 🚀

## Features

- Simulates the behavior of spheres and boxes in a 3D environment.
- Applies gravitational forces to objects based on their mass.
- Detects collisions between objects and resolves them.
- Supports customizable parameters for gravity, friction, and collision detection.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/your-username/physics-simulation.git
    ```

2. Navigate to the project directory:
    ```
    cd physics-simulation
    ```

3. Install dependencies (NumPy):
    ```
    pip install numpy
    ```

## Usage

1. Import the necessary classes from `physics_simulation.py`:
    ```python
    from physics_simulation import PhysicsEngine, Sphere, Box
    ```

2. Create objects to simulate (spheres or boxes) with specified parameters (mass, radius/size, initial position, initial velocity):
    ```python
    sphere = Sphere(mass=1.0, radius=1.0, position=[0, 0, 0], velocity=[0, 0, 0])
    box = Box(mass=2.0, size=[1, 1, 1], position=[2, 0, 0], velocity=[0, 0, 0])
    ```

3. Create a `PhysicsEngine` instance and simulate time steps:
    ```python
    engine = PhysicsEngine(gravity=[0, -9.81, 0])
    dt = 0.01  # Time step (seconds)
    for _ in range(num_steps):
        engine.simulate_step([sphere, box], dt)
    ```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License 2.0. - see the [LICENSE](LICENSE) file for details.


## Version Control

This project utilizes Git for version control. Be sure to commit your changes frequently and follow Git best practices.

## Testing

Unit tests are located in the `tests/` directory. To run the tests, use the following command:
```
pytest
```

## Debugging

Debugging can be performed using print statements or a debugger like pdb. Additionally, logging can be enabled to track the behavior of the simulation.

## Documentation

Documentation for the codebase can be found in the `docs/` directory. It includes explanations of classes, methods, parameters, and usage examples.
